/* ============================================================
   THE ASSISTANT
   A full-screen panel that opens over any page and keeps its own
   flow, so nothing mixes with the page behind it.

   Two tools:
     1. Live Route  — build a self-guided route, then follow it live.
     2. Extend      — look up a rental by ticket number and add time.

   No dependencies. Everything below runs in the browser.

   ---- INTEGRATION ----------------------------------------------
   Rental lookup and payment are the two places this needs a real
   backend. Both are isolated in ASSIST_CONFIG so they can be wired
   without touching the UI:

     lookupUrl : GET {ref} -> rental JSON. Leave null for demo mode.
     payUrl    : where checkout hands off. Receives ref, block, method.

   Until lookupUrl is set the panel runs in demo mode, says so on
   screen, and only resolves the sample tickets in DEMO_RENTALS.
   ---------------------------------------------------------------- */
(function () {
  'use strict';

  var CFG = window.ASSIST_CONFIG || {};
  var T = CFG.t || {};
  function tr(k, fb) { return T[k] || fb || k; }

  /* A short tick on selection. Gloved or one-handed, the buzz confirms the
     tap without the rider having to look down again. */
  function tick(ms) {
    try { if (navigator.vibrate) navigator.vibrate(ms || 12); } catch (e) {}
  }
  var POI = window.LR_POI || [];
  var MODES = window.LR_MODES || [];
  var INTERESTS = window.LR_INTERESTS || [];
  var DURATIONS = window.LR_DURATIONS || [];
  var EX = window.LR_EXTEND || {};
  var START = POI.filter(function (p) { return p.id === 'shop'; })[0];

  var DEMO_RENTALS = {
    'MBB-4417': { ref: 'MBB-4417', name: 'Danielle R.', family: 'cruiser',
      item: 'Beach Cruiser', qty: 2, dueISO: null, dueInMins: 48 },
    'MBB-2098': { ref: 'MBB-2098', name: 'Marco V.', family: 'ebike',
      item: 'Electric Bike', qty: 1, dueISO: null, dueInMins: 155 },
    'MBB-7731': { ref: 'MBB-7731', name: 'The Okonkwo family', family: 'kids',
      item: 'Kids Bike + Baby Seat', qty: 3, dueISO: null, dueInMins: -20 },
  };

  var state = {
    open: false, tool: null, view: null,
    mode: 'cruiser', minutes: 120, interests: [],
    route: [], liveIdx: 0, watchId: null,
    rental: null, block: null, method: null,
    lastFocus: null,
  };

  /* ================= geo maths ================= */
  var R = 6371;
  function rad(d) { return d * Math.PI / 180; }
  function distKm(a, b) {
    var dLat = rad(b.lat - a.lat), dLng = rad(b.lng - a.lng);
    var s = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
      Math.cos(rad(a.lat)) * Math.cos(rad(b.lat)) *
      Math.sin(dLng / 2) * Math.sin(dLng / 2);
    return 2 * R * Math.asin(Math.sqrt(s));
  }
  function bearing(a, b) {
    var y = Math.sin(rad(b.lng - a.lng)) * Math.cos(rad(b.lat));
    var x = Math.cos(rad(a.lat)) * Math.sin(rad(b.lat)) -
      Math.sin(rad(a.lat)) * Math.cos(rad(b.lat)) * Math.cos(rad(b.lng - a.lng));
    return (Math.atan2(y, x) * 180 / Math.PI + 360) % 360;
  }
  function compass(d) { return ['N','NE','E','SE','S','SW','W','NW'][Math.round(d/45)%8]; }
  function km(v) { return v < 1 ? Math.round(v * 1000) + ' m' : v.toFixed(1) + ' km'; }
  function mi(v) { return (v * 0.621371).toFixed(1) + ' mi'; }
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  /* ================= route engine ================= */
  function speedOf(id) {
    for (var i = 0; i < MODES.length; i++) if (MODES[i].id === id) return MODES[i].speed;
    return 12;
  }
  function buildRoute() {
    if (!START) return [];
    var speed = speedOf(state.mode), budget = state.minutes;
    var pool = POI.filter(function (p) {
      if (p.id === 'shop') return false;
      if (!state.interests.length) return true;
      return p.tags.some(function (t) { return state.interests.indexOf(t) > -1; });
    });
    if (state.mode === 'skate' || state.mode === 'walk') {
      pool = pool.filter(function (p) {
        return ['macarthur', 'belleisle', 'fontainebleau', 'faena'].indexOf(p.id) === -1;
      });
    }
    var route = [], here = START, used = 0;
    while (pool.length) {
      var best = null, bestD = Infinity;
      for (var i = 0; i < pool.length; i++) {
        var d = distKm(here, pool[i]);
        if (d < bestD) { bestD = d; best = i; }
      }
      var next = pool[best];
      var ride = (bestD / speed) * 60 * 1.35;
      var back = (distKm(next, START) / speed) * 60 * 1.35;
      if (used + ride + next.mins + back > budget) break;
      used += ride + next.mins;
      route.push({ poi: next, legKm: bestD, legMins: Math.max(1, Math.round(ride)) });
      here = next; pool.splice(best, 1);
    }
    var backKm = distKm(here, START);
    route.push({ poi: START, legKm: backKm,
      legMins: Math.max(1, Math.round((backKm / speed) * 60 * 1.35)), isReturn: true });
    state.route = route;
    return route;
  }
  function mapsUrl(pts) {
    return 'https://www.google.com/maps/dir/' +
      encodeURI(pts.map(function (p) { return p.lat + ',' + p.lng; }).join('/'));
  }

  /* ================= panel shell ================= */
  var el = {};
  function build() {
    if (el.root) return;
    var root = document.createElement('div');
    root.className = 'as';
    root.id = 'assistant';
    root.setAttribute('role', 'dialog');
    root.setAttribute('aria-modal', 'true');
    root.setAttribute('aria-label', 'Miami Beach Bikes ' + tr('as_title'));
    root.hidden = true;
    root.innerHTML = '' +
      '<div class="as__scrim" data-as-close></div>' +
      '<div class="as__panel">' +
      '  <header class="as__bar">' +
      '    <button class="as__back" type="button" hidden>&larr;</button>' +
      '    <span class="as__title">' + tr('as_title') + '</span>' +
      '    <button class="as__close" type="button" data-as-close aria-label="' + tr('as_close') + '">&times;</button>' +
      '  </header>' +
      '  <div class="as__body"></div>' +
      '</div>';
    document.body.appendChild(root);
    el.root = root;
    el.panel = root.querySelector('.as__panel');
    el.body = root.querySelector('.as__body');
    el.title = root.querySelector('.as__title');
    el.back = root.querySelector('.as__back');

    root.addEventListener('click', function (e) {
      if (e.target.hasAttribute('data-as-close')) close();
    });
    el.back.addEventListener('click', goBack);
    document.addEventListener('keydown', function (e) {
      if (!state.open) return;
      if (e.key === 'Escape') close();
      if (e.key === 'Tab') trap(e);
    });
  }

  function trap(e) {
    var f = el.panel.querySelectorAll(
      'a[href],button:not([disabled]),input,select,textarea,[tabindex]:not([tabindex="-1"])');
    f = [].slice.call(f).filter(function (n) { return n.offsetParent !== null; });
    if (!f.length) return;
    var first = f[0], last = f[f.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  }

  function open(tool) {
    build();
    state.lastFocus = document.activeElement;
    state.open = true;
    el.root.hidden = false;
    document.body.classList.add('as-open');
    requestAnimationFrame(function () { el.root.classList.add('is-in'); });
    go(tool || 'home');
  }

  function close() {
    if (!el.root) return;
    stopLive();
    state.open = false;
    el.root.classList.remove('is-in');
    document.body.classList.remove('as-open');
    setTimeout(function () { if (!state.open) el.root.hidden = true; }, 260);
    if (state.lastFocus && state.lastFocus.focus) state.lastFocus.focus();
  }

  var stack = [];
  function go(view, push) {
    if (push !== false && state.view) stack.push(state.view);
    state.view = view;
    el.back.hidden = !stack.length;
    var v = VIEWS[view];
    if (!v) return;
    el.title.textContent = v.title;
    el.body.innerHTML = v.html();
    el.body.scrollTop = 0;
    if (v.wire) v.wire();
    var focusable = el.body.querySelector('button,a[href],input');
    if (focusable) focusable.focus({ preventScroll: true });
  }
  function goBack() {
    var prev = stack.pop();
    if (prev) go(prev, false);
    el.back.hidden = !stack.length;
  }

  /* ================= views ================= */
  var VIEWS = {};

  VIEWS.home = {
    title: tr('as_home'),
    html: function () {
      return '' +
        '<div class="as-home">' +
        '  <button class="as-tool" data-go="lr-mode">' +
        '    <span class="as-tool__ico">&#128205;</span>' +
        '    <span class="as-tool__txt"><b>' + tr('tool_live') + '</b>' +
        '      <em>' + tr('tool_live_sub') + '</em></span>' +
        '    <span class="as-tool__go">&rarr;</span>' +
        '  </button>' +
        '  <button class="as-tool" data-go="ex-lookup">' +
        '    <span class="as-tool__ico">&#9203;</span>' +
        '    <span class="as-tool__txt"><b>' + tr('tool_extend') + '</b>' +
        '      <em>' + tr('tool_extend_sub') + '</em></span>' +
        '    <span class="as-tool__go">&rarr;</span>' +
        '  </button>' +
        '  <a class="as-tool" href="' + (CFG.bookUrl || '#') + '" target="_blank" rel="noopener">' +
        '    <span class="as-tool__ico">&#128666;</span>' +
        '    <span class="as-tool__txt"><b>' + tr('tool_book') + '</b>' +
        '      <em>' + tr('tool_book_sub') + '</em></span>' +
        '    <span class="as-tool__go">&rarr;</span>' +
        '  </a>' +
        '  <a class="as-tool as-tool--quiet" href="tel:' + (CFG.phone || '') + '">' +
        '    <span class="as-tool__ico">&#128222;</span>' +
        '    <span class="as-tool__txt"><b>' + tr('tool_call') + '</b>' +
        '      <em>' + esc(CFG.phonePretty || '') + ' &middot; ' + tr('tool_call_sub') + '</em></span>' +
        '    <span class="as-tool__go">&rarr;</span>' +
        '  </a>' +
        '</div>';
    },
    wire: function () {
      el.body.querySelectorAll('[data-go]').forEach(function (b) {
        b.addEventListener('click', function () { go(b.getAttribute('data-go')); });
      });
    },
  };

  /* ---------- Book: stay on the site ---------- */
  VIEWS.book = {
    title: tr('book_title'),
    html: function () {
      var L = CFG.links || {};
      function row(href, ico, title, sub) {
        return '<a class="as-tool" href="' + href + '">' +
          '<span class="as-tool__ico">' + ico + '</span>' +
          '<span class="as-tool__txt"><b>' + title + '</b><em>' + sub + '</em></span>' +
          '<span class="as-tool__go">&rarr;</span></a>';
      }
      return '<div class="as-home">' +
        row(L.rentals || 'rentals.html', '&#128690;', tr('book_rentals'), tr('book_rentals_sub')) +
        row(L.tours || 'tours.html', '&#128205;', tr('book_tours'), tr('book_tours_sub')) +
        row(L.adventures || 'adventures.html', '&#127754;', tr('book_adv'), tr('book_adv_sub')) +
        '<button class="as-tool" data-go="ex-lookup">' +
        '  <span class="as-tool__ico">&#9203;</span>' +
        '  <span class="as-tool__txt"><b>' + tr('tool_extend') + '</b><em>' +
        tr('tool_extend_sub') + '</em></span>' +
        '  <span class="as-tool__go">&rarr;</span></button>' +
        '<a class="as-tool as-tool--quiet" href="' + (CFG.bookUrl || '#') +
        '" target="_blank" rel="noopener">' +
        '  <span class="as-tool__ico">&#128179;</span>' +
        '  <span class="as-tool__txt"><b>' + tr('book_online') + '</b><em>' +
        tr('book_online_sub') + '</em></span>' +
        '  <span class="as-tool__go">&rarr;</span></a>' +
        '</div>';
    },
    wire: function () {
      el.body.querySelectorAll('[data-go]').forEach(function (b) {
        b.addEventListener('click', function () { go(b.getAttribute('data-go')); });
      });
    },
  };

  /* ---------- Live Route: step 1 ---------- */
  VIEWS['lr-mode'] = {
    title: tr('lr_step').replace('%d', 1),
    html: function () {
      var opts = MODES.map(function (m) {
        return '<button class="as-tile' + (m.id === state.mode ? ' is-on' : '') +
          '" data-mode="' + m.id + '"><span class="as-tile__ico">' + m.icon +
          '</span><span class="as-tile__name">' + esc(m.short || m.name) + '</span></button>';
      }).join('');
      return '<div class="as-step">' +
        '<p class="as-q">' + tr('lr_q_mode') + '</p>' +
        '<div class="as-tiles">' + opts + '</div>' +
        '<p class="as-note" id="as-mode-note"></p>' +
        '</div>';
    },
    wire: function () {
      function note() {
        var m = MODES.filter(function (x) { return x.id === state.mode; })[0];
        var n = el.body.querySelector('#as-mode-note');
        if (m && n) n.innerHTML = esc(m.blurb) +
          (m.cta ? ' <a class="as-inline" href="' + m.cta + '">' + tr('btn_book') + ' &rarr;</a>' : '');
      }
      el.body.querySelectorAll('[data-mode]').forEach(function (b) {
        b.addEventListener('click', function () {
          el.body.querySelectorAll('[data-mode]').forEach(function (x) { x.classList.remove('is-on'); });
          b.classList.add('is-on');
          state.mode = b.getAttribute('data-mode');
          note();
          tick();
          // one tap, one step: no Next button to reach for
          setTimeout(function () { go('lr-time'); }, 240);
        });
      });
      note();
    },
  };

  /* ---------- Live Route: step 2 ---------- */
  VIEWS['lr-time'] = {
    title: tr('lr_step').replace('%d', 2),
    html: function () {
      var opts = DURATIONS.map(function (d) {
        return '<button class="as-tile as-tile--text' + (d.mins === state.minutes ? ' is-on' : '') +
          '" data-mins="' + d.mins + '"><span class="as-tile__big">' +
          (d.mins < 60 ? d.mins : (d.mins / 60)) + '</span><span class="as-tile__name">' +
          (d.mins < 60 ? tr('lr_mins') : (d.mins >= 240 ? esc(d.name) : tr('unit_hours'))) +
          '</span></button>';
      }).join('');
      return '<div class="as-step">' +
        '<p class="as-q">' + tr('lr_q_time') + '</p>' +
        '<div class="as-tiles as-tiles--2">' + opts + '</div>' +
        '<p class="as-note">' + tr('lr_time_note') + '</p>' +
        '</div>';
    },
    wire: function () {
      el.body.querySelectorAll('[data-mins]').forEach(function (b) {
        b.addEventListener('click', function () {
          el.body.querySelectorAll('[data-mins]').forEach(function (x) { x.classList.remove('is-on'); });
          b.classList.add('is-on');
          state.minutes = parseInt(b.getAttribute('data-mins'), 10);
          tick();
          setTimeout(function () { go('lr-tags'); }, 240);
        });
      });
    },
  };

  /* ---------- Live Route: step 3 ---------- */
  VIEWS['lr-tags'] = {
    title: tr('lr_step').replace('%d', 3),
    html: function () {
      var opts = INTERESTS.map(function (t) {
        var on = state.interests.indexOf(t[0]) > -1;
        return '<button class="as-pick' + (on ? ' is-on' : '') +
          '" data-tag="' + t[0] + '"><span class="as-pick__ico">' + t[2] + '</span>' +
          '<span class="as-pick__t">' + esc(t[1]) + '</span></button>';
      }).join('');
      return '<div class="as-step">' +
        '<p class="as-q">' + tr('lr_q_tags') + '</p>' +
        '<div class="as-picks">' + opts + '</div>' +
        '<p class="as-note">' + tr('lr_tags_note') + '</p>' +
        '</div>' +
        '<div class="as-dock"><button class="btn btn--block" data-next>' + tr('lr_build') + '</button></div>';
    },
    wire: function () {
      el.body.querySelectorAll('[data-tag]').forEach(function (b) {
        b.addEventListener('click', function () {
          var t = b.getAttribute('data-tag'), i = state.interests.indexOf(t);
          if (i > -1) { state.interests.splice(i, 1); b.classList.remove('is-on'); }
          else { state.interests.push(t); b.classList.add('is-on'); }
          tick();
        });
      });
      el.body.querySelector('[data-next]').addEventListener('click', function () { go('lr-route'); });
    },
  };

  /* ---------- Live Route: the plan ---------- */
  VIEWS['lr-route'] = {
    title: tr('lr_your'),
    html: function () {
      var route = buildRoute();
      var stops = route.filter(function (r) { return !r.isReturn; });
      if (!stops.length) {
        return '<div class="as-empty"><h3>' + tr('lr_empty_t') + '</h3>' +
          '<p>' + tr('lr_empty_p') + '</p>' +
          '<button class="btn" data-restart>' + tr('lr_change') + '</button></div>';
      }
      var totalKm = route.reduce(function (a, r) { return a + r.legKm; }, 0);
      var totalMins = route.reduce(function (a, r) { return a + r.legMins + (r.poi.mins || 0); }, 0);
      var pts = [START].concat(stops.map(function (s) { return s.poi; })).concat([START]);

      var list = route.map(function (r, i) {
        var p = r.poi;
        return '<li class="as-stop' + (r.isReturn ? ' as-stop--end' : '') + '">' +
          '<span class="as-stop__n">' + (r.isReturn ? '&#127937;' : (i + 1)) + '</span>' +
          '<span class="as-stop__b">' +
          '<b>' + esc(p.name) + '</b>' +
          '<em>' + esc(r.isReturn ? tr('lr_back_shop') : p.sub) + '</em>' +
          '<span class="as-stop__m">' + km(r.legKm) + ' &middot; ' + r.legMins + ' min' +
          (p.mins && !r.isReturn ? ' &middot; ' + p.mins + ' ' + tr('lr_there') : '') + '</span>' +
          (r.isReturn ? '' : '<span class="as-stop__s">' + esc(p.story) + '</span>') +
          '</span></li>';
      }).join('');

      return '<div class="as-sum">' +
        '<div><b>' + stops.length + '</b><span>' + tr('lr_stops') + '</span></div>' +
        '<div><b>' + km(totalKm) + '</b><span>' + mi(totalKm) + '</span></div>' +
        '<div><b>' + Math.round(totalMins) + '</b><span>' + tr('lr_mins') + '</span></div>' +
        '</div>' +
        '<ol class="as-stops">' + list + '</ol>' +
        '<div class="as-dock as-dock--split">' +
        '  <a class="btn btn--sm btn--ocean" href="' + mapsUrl(pts) + '" target="_blank" rel="noopener">' + tr('lr_maps') + '</a>' +
        '  <button class="btn btn--sm" data-live>' + tr('lr_start') + '</button>' +
        '</div>';
    },
    wire: function () {
      var r = el.body.querySelector('[data-restart]');
      if (r) r.addEventListener('click', function () { stack = []; go('lr-mode', false); });
      var l = el.body.querySelector('[data-live]');
      if (l) l.addEventListener('click', function () { state.liveIdx = 0; go('lr-live'); });
    },
  };

  /* ---------- Live Route: live ---------- */
  VIEWS['lr-live'] = {
    title: tr('lr_guide'),
    html: function () {
      return '<div class="as-live" id="as-live">' +
        '<div class="as-live__head"><span class="as-live__dot"></span>' +
        '<span id="as-live-count"></span></div>' +
        '<h3 id="as-live-name">&mdash;</h3>' +
        '<p class="as-live__sub" id="as-live-sub"></p>' +
        '<p class="as-live__gps" id="as-live-gps">' + tr('lr_finding') + '</p>' +
        '<p class="as-live__story" id="as-live-story"></p>' +
        '</div>' +
        '<div class="as-dock as-dock--split">' +
        '  <a class="btn btn--sm btn--sun" id="as-live-nav" href="#" target="_blank" rel="noopener">' + tr('lr_nav') + '</a>' +
        '  <button class="btn btn--sm btn--ghost" id="as-live-next">' + tr('lr_here') + ' &rarr;</button>' +
        '</div>';
    },
    wire: function () {
      paintLive(null);
      el.body.querySelector('#as-live-next').addEventListener('click', function () {
        if (state.liveIdx < state.route.length - 1) { state.liveIdx++; paintLive(null); }
      });
      startLive();
    },
  };

  function startLive() {
    var gps = document.getElementById('as-live-gps');
    if (!navigator.geolocation) {
      if (gps) gps.textContent = tr('lr_nogeo');
      return;
    }
    state.watchId = navigator.geolocation.watchPosition(
      function (pos) { paintLive({ lat: pos.coords.latitude, lng: pos.coords.longitude }); },
      function (err) {
        if (!gps) return;
        gps.textContent = err.code === 1
          ? tr('lr_denied')
          : tr('lr_nofix');
      },
      { enableHighAccuracy: true, maximumAge: 5000, timeout: 20000 });
  }
  function stopLive() {
    if (state.watchId !== null && navigator.geolocation) {
      navigator.geolocation.clearWatch(state.watchId);
    }
    state.watchId = null;
  }
  function paintLive(me) {
    var stop = state.route[state.liveIdx];
    if (!stop) return;
    var p = stop.poi, q = function (id) { return document.getElementById(id); };
    if (!q('as-live-name')) return;
    q('as-live-name').textContent = p.name;
    q('as-live-sub').textContent = stop.isReturn ? tr('lr_last_leg') : p.sub;
    q('as-live-story').textContent = stop.isReturn
      ? tr('lr_drop') : p.story;
    q('as-live-count').textContent = tr('lr_stop_of').replace('%d', state.liveIdx + 1).replace('%d', state.route.length);
    q('as-live-nav').href = 'https://www.google.com/maps/dir/?api=1&destination=' + p.lat + ',' + p.lng;
    if (me) {
      var d = distKm(me, p);
      q('as-live-gps').innerHTML = '<strong>' + km(d) + '</strong> ' + tr('lr_away') + ' <strong>' +
        compass(bearing(me, p)) + '</strong>';
      if (d < 0.045 && state.liveIdx < state.route.length - 1) {
        state.liveIdx++;
        var box = q('as-live');
        if (box) { box.classList.add('is-arrived'); setTimeout(function () { box.classList.remove('is-arrived'); }, 1600); }
        paintLive(me);
      }
    }
  }

  /* ================= Extend: lookup ================= */
  VIEWS['ex-lookup'] = {
    title: tr('ex_title'),
    html: function () {
      return '<div class="as-step">' +
        '<p class="as-q">' + tr('ex_q') + '</p>' +
        '<p class="as-note">' + tr('ex_note') + '</p>' +
        '<form class="as-form" id="as-ex-form">' +
        '  <label class="as-field"><span>' + tr('ex_label') + '</span>' +
        '    <input id="as-ref" name="ref" autocomplete="off" autocapitalize="characters" ' +
        '           spellcheck="false" placeholder="MBB-4417" required></label>' +
        '  <p class="as-err" id="as-ex-err" hidden></p>' +
        '  <button class="btn btn--block" type="submit">' + tr('ex_find') + '</button>' +
        '</form>' +
        (CFG.lookupUrl ? '' :
          '<p class="as-demo"><b>' + tr('ex_demo') + '</b> ' + tr('ex_demo_p') +
          ' <code>MBB-4417</code>, <code>MBB-2098</code>, <code>MBB-7731</code>.</p>') +
        '<p class="as-note">' + tr('ex_cantfind') + ' <a href="tel:' + (CFG.phone || '') + '">' +
        esc(CFG.phonePretty || '') + '</a> ' + tr('ex_cantfind2') + '</p>' +
        '</div>';
    },
    wire: function () {
      el.body.querySelector('#as-ex-form').addEventListener('submit', function (e) {
        e.preventDefault();
        var ref = el.body.querySelector('#as-ref').value.trim().toUpperCase();
        var err = el.body.querySelector('#as-ex-err');
        err.hidden = true;
        lookup(ref).then(function (r) {
          state.rental = r; state.block = null; state.method = null;
          go('ex-rental');
        }).catch(function (m) {
          err.textContent = m;
          err.hidden = false;
        });
      });
    },
  };

  function lookup(ref) {
    return new Promise(function (resolve, reject) {
      if (!ref) return reject(tr('ex_typefirst'));
      if (CFG.lookupUrl) {
        fetch(CFG.lookupUrl.replace('{ref}', encodeURIComponent(ref)), {
          headers: { 'Accept': 'application/json' },
        }).then(function (res) {
          if (!res.ok) throw new Error('not found');
          return res.json();
        }).then(resolve).catch(function () {
          reject(tr('ex_notfound'));
        });
        return;
      }
      setTimeout(function () {
        var r = DEMO_RENTALS[ref];
        if (r) resolve(r);
        else reject('No rental found for ' + esc(ref) + '. In demo mode try MBB-4417.');
      }, 420);
    });
  }

  function dueText(mins) {
    if (mins < 0) return { txt: tr('ex_overdue') + ' ' + Math.abs(mins) + ' min', cls: 'is-late' };
    if (mins < 60) return { txt: tr('ex_due_in') + ' ' + mins + ' min', cls: 'is-soon' };
    var h = Math.floor(mins / 60), m = mins % 60;
    return { txt: tr('ex_due_in') + ' ' + h + ' h' + (m ? ' ' + m + ' min' : ''), cls: '' };
  }

  /* ================= Extend: the rental ================= */
  VIEWS['ex-rental'] = {
    title: tr('ex_yours'),
    html: function () {
      var r = state.rental;
      var rates = EX.rates[r.family] || {};
      var due = dueText(r.dueInMins);
      var blocks = EX.blocks.map(function (b) {
        var price = rates[b.id];
        var dis = price === null || price === undefined;
        return '<button class="as-block' + (dis ? ' is-off' : '') +
          (state.block === b.id ? ' is-on' : '') + '" data-block="' + b.id + '"' +
          (dis ? ' disabled' : '') + '>' +
          '<b>' + esc(b.label) + '</b>' +
          '<span>' + (dis ? tr('price_call') : '$' + price * r.qty) + '</span>' +
          (r.qty > 1 && !dis ? '<em>$' + price + ' &times; ' + r.qty + '</em>' : '') +
          '</button>';
      }).join('');
      return '<div class="as-rental">' +
        '<div class="as-rental__head">' +
        '  <span class="as-rental__ref">' + esc(r.ref) + '</span>' +
        '  <span class="as-rental__due ' + due.cls + '">' + due.txt + '</span>' +
        '</div>' +
        '<h3>' + esc(r.item) + (r.qty > 1 ? ' &times; ' + r.qty : '') + '</h3>' +
        '<p class="as-rental__name">' + esc(r.name) + '</p>' +
        (r.dueInMins < 0
          ? '<p class="as-warn">' + tr('ex_warn') + '</p>' : '') +
        '</div>' +
        '<div class="as-step">' +
        '<p class="as-q">' + tr('ex_howlong') + '</p>' +
        '<div class="as-blocks">' + blocks + '</div>' +
        '</div>' +
        '<div class="as-dock"><button class="btn btn--block" data-next disabled>' + tr('ex_choose_pay') + '</button></div>';
    },
    wire: function () {
      var next = el.body.querySelector('[data-next]');
      el.body.querySelectorAll('[data-block]').forEach(function (b) {
        b.addEventListener('click', function () {
          el.body.querySelectorAll('[data-block]').forEach(function (x) { x.classList.remove('is-on'); });
          b.classList.add('is-on');
          state.block = b.getAttribute('data-block');
          next.disabled = false;
          tick();
        });
      });
      next.addEventListener('click', function () { if (state.block) go('ex-pay'); });
    },
  };

  /* ================= Extend: pay ================= */
  function extPrice() {
    var r = state.rental, rates = EX.rates[r.family] || {};
    var p = rates[state.block];
    return p == null ? null : p * r.qty;
  }
  function blockLabel() {
    var b = EX.blocks.filter(function (x) { return x.id === state.block; })[0];
    return b ? b.label : '';
  }

  VIEWS['ex-pay'] = {
    title: tr('ex_pay_title'),
    html: function () {
      var r = state.rental, total = extPrice();
      var methods = EX.pay.map(function (m) {
        return '<button class="as-pay' + (state.method === m.id ? ' is-on' : '') +
          '" data-pay="' + m.id + '">' +
          '<span class="as-pay__ico">' + m.icon + '</span>' +
          '<span class="as-pay__t"><b>' + esc(m.name) + '</b><em>' + esc(m.note) + '</em></span>' +
          '</button>';
      }).join('');
      return '<div class="as-recap">' +
        '<div><span>' + tr('ex_rental') + '</span><b>' + esc(r.item) + (r.qty > 1 ? ' &times; ' + r.qty : '') + '</b></div>' +
        '<div><span>' + tr('ex_ticket') + '</span><b>' + esc(r.ref) + '</b></div>' +
        '<div><span>' + tr('ex_ext') + '</span><b>' + esc(blockLabel()) + '</b></div>' +
        '<div class="as-recap__total"><span>' + tr('ex_total') + '</span><b>' +
        (total == null ? tr('ex_quoted') : '$' + total) + '</b></div>' +
        '</div>' +
        '<div class="as-step">' +
        '<p class="as-q">' + tr('ex_how_pay') + '</p>' +
        '<div class="as-pays">' + methods + '</div>' +
        '<p class="as-note as-note--lock">&#128274; ' + tr('ex_secure') + '</p>' +
        '</div>' +
        '<div class="as-dock"><button class="btn btn--block" data-pay-go disabled>' + tr('ex_continue') + '</button></div>';
    },
    wire: function () {
      var go2 = el.body.querySelector('[data-pay-go]');
      el.body.querySelectorAll('[data-pay]').forEach(function (b) {
        b.addEventListener('click', function () {
          el.body.querySelectorAll('[data-pay]').forEach(function (x) { x.classList.remove('is-on'); });
          b.classList.add('is-on');
          state.method = b.getAttribute('data-pay');
          go2.disabled = false;
          tick();
        });
      });
      go2.addEventListener('click', function () {
        if (!state.method) return;
        var url = CFG.payUrl;
        if (url) {
          var q = 'ref=' + encodeURIComponent(state.rental.ref) +
            '&block=' + encodeURIComponent(state.block) +
            '&method=' + encodeURIComponent(state.method);
          window.open(url + (url.indexOf('?') > -1 ? '&' : '?') + q, '_blank', 'noopener');
        }
        go('ex-done');
      });
    },
  };

  VIEWS['ex-done'] = {
    title: tr('ex_almost'),
    html: function () {
      var wired = !!CFG.payUrl;
      return '<div class="as-done">' +
        '<div class="as-done__ico">' + (wired ? '&#128179;' : '&#128222;') + '</div>' +
        '<h3>' + (wired ? tr('ex_finish') : tr('ex_callit')) + '</h3>' +
        '<p>' + (wired
          ? tr('ex_finish_p')
          : tr('ex_callit_p')) + '</p>' +
        '<div class="as-done__recap">' + esc(state.rental.ref) + ' &middot; ' +
        esc(blockLabel()) + (extPrice() == null ? '' : ' &middot; $' + extPrice()) + '</div>' +
        '<a class="btn btn--block" href="tel:' + (CFG.phone || '') + '">' + tr('btn_call') + ' ' +
        esc(CFG.phonePretty || '') + '</a>' +
        '<button class="btn btn--block btn--ghost" style="margin-top:.7rem;border-color:var(--line);color:var(--ink)" data-as-close>' + tr('ex_done') + '</button>' +
        '</div>';
    },
  };

  /* ================= boot ================= */
  function boot() {
    document.querySelectorAll('[data-assistant]').forEach(function (b) {
      b.addEventListener('click', function (e) {
        e.preventDefault();
        open(b.getAttribute('data-assistant') || 'home');
      });
    });
    // deep link: #assistant, #assistant=ex-lookup
    var h = window.location.hash;
    if (h.indexOf('#assistant') === 0) {
      var t = h.split('=')[1];
      open(t || 'home');
    }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();

  window.Assistant = { open: open, close: close };
})();
