/* ============================================================
   LIVE ROUTE — a virtual tour guide for South Beach
   Pick how you move, how long you have and what you like;
   it builds a route from the shop and walks you through it.
   No backend, no API key: Geolocation + Haversine + Google Maps links.
   ============================================================ */
(function () {
  'use strict';

  var POI = window.LR_POI || [];
  var MODES = window.LR_MODES || [];
  var START = POI.filter(function (p) { return p.id === 'shop'; })[0];
  if (!START) return;

  var state = {
    mode: 'cruiser',
    minutes: 120,
    interests: [],
    route: [],
    live: false,
    idx: 0,
    watchId: null,
  };

  /* ---------- geo maths ---------- */
  var R = 6371; // km
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

  function compass(deg) {
    return ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'][Math.round(deg / 45) % 8];
  }

  function km(v) { return v < 1 ? Math.round(v * 1000) + ' m' : v.toFixed(1) + ' km'; }
  function mi(v) { return (v * 0.621371).toFixed(1) + ' mi'; }

  /* ---------- route building ----------
     Nearest-neighbour from the shop over the POIs that match the chosen
     interests, stopping once the time budget (riding + lingering) runs out.
     Riding time is padded 35% for lights, crossings and actually looking. */
  function speedOf(id) {
    for (var i = 0; i < MODES.length; i++) if (MODES[i].id === id) return MODES[i].speed;
    return 12;
  }

  function buildRoute() {
    var speed = speedOf(state.mode);
    var budget = state.minutes;
    var pool = POI.filter(function (p) {
      if (p.id === 'shop') return false;
      if (!state.interests.length) return true;
      return p.tags.some(function (t) { return state.interests.indexOf(t) > -1; });
    });

    // skates and walking stay off the causeways
    if (state.mode === 'skate' || state.mode === 'walk') {
      pool = pool.filter(function (p) {
        return ['macarthur', 'belleisle', 'fontainebleau', 'faena'].indexOf(p.id) === -1;
      });
    }

    var route = [], here = START, used = 0;
    while (pool.length) {
      // nearest unvisited
      var best = null, bestD = Infinity;
      for (var i = 0; i < pool.length; i++) {
        var d = distKm(here, pool[i]);
        if (d < bestD) { bestD = d; best = i; }
      }
      var next = pool[best];
      var ride = (bestD / speed) * 60 * 1.35;
      var back = (distKm(next, START) / speed) * 60 * 1.35;
      // keep enough time to get home
      if (used + ride + next.mins + back > budget) break;
      used += ride + next.mins;
      route.push({ poi: next, legKm: bestD, legMins: Math.max(1, Math.round(ride)) });
      here = next;
      pool.splice(best, 1);
    }

    var backKm = distKm(here, START);
    route.push({
      poi: START, legKm: backKm,
      legMins: Math.max(1, Math.round((backKm / speed) * 60 * 1.35)), isReturn: true,
    });
    state.route = route;
    return route;
  }

  /* ---------- rendering ---------- */
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };

  function mapsUrl(stops) {
    var pts = stops.map(function (s) { return s.lat + ',' + s.lng; });
    return 'https://www.google.com/maps/dir/' + encodeURI(pts.join('/'));
  }

  function renderRoute() {
    var route = buildRoute();
    var out = $('#lr-result');
    if (!out) return;

    var stops = route.filter(function (r) { return !r.isReturn; });
    if (!stops.length) {
      out.innerHTML = '<div class="lr-empty"><h3>Not enough time for that combination</h3>' +
        '<p>Add more minutes, pick a faster ride, or widen what you are interested in ' +
        'and we will build you something.</p></div>';
      return;
    }

    var totalKm = route.reduce(function (a, r) { return a + r.legKm; }, 0);
    var totalMins = route.reduce(function (a, r) { return a + r.legMins + (r.poi.mins || 0); }, 0);
    var allPts = [START].concat(stops.map(function (s) { return s.poi; })).concat([START]);

    var html = '' +
      '<div class="lr-summary">' +
      '  <div class="lr-summary__stat"><b>' + stops.length + '</b><span>stops</span></div>' +
      '  <div class="lr-summary__stat"><b>' + km(totalKm) + '</b><span>' + mi(totalKm) + '</span></div>' +
      '  <div class="lr-summary__stat"><b>' + Math.round(totalMins) + '</b><span>minutes</span></div>' +
      '  <div class="lr-summary__actions">' +
      '    <button class="btn btn--sm" id="lr-start">Start live guide</button>' +
      '    <a class="btn btn--sm btn--ocean" href="' + mapsUrl(allPts) + '" target="_blank" rel="noopener">Open in Maps</a>' +
      '  </div>' +
      '</div>' +
      '<ol class="lr-stops">';

    route.forEach(function (r, i) {
      var p = r.poi;
      html += '' +
        '<li class="lr-stop' + (r.isReturn ? ' lr-stop--end' : '') + '" data-stop="' + i + '">' +
        '  <div class="lr-stop__num">' + (r.isReturn ? '&#127937;' : (i + 1)) + '</div>' +
        '  <div class="lr-stop__body">' +
        '    <h3>' + p.name + (r.isReturn ? ' <span class="lr-stop__tag">back to the shop</span>' : '') + '</h3>' +
        '    <p class="lr-stop__sub">' + (r.isReturn ? 'Drop off, or keep it another hour' : p.sub) + '</p>' +
        '    <p class="lr-stop__meta">' +
        '      <span>&#128205; ' + p.addr + '</span>' +
        '      <span>&#128678; ' + km(r.legKm) + '</span>' +
        '      <span>&#9201;&#65039; ' + r.legMins + ' min ride</span>' +
        (p.mins && !r.isReturn ? '      <span>&#128065;&#65039; ' + p.mins + ' min here</span>' : '') +
        '    </p>' +
        (r.isReturn ? '' : '    <p class="lr-stop__story">' + p.story + '</p>') +
        '    <a class="lr-stop__nav" href="https://www.google.com/maps/dir/?api=1&destination=' +
        p.lat + ',' + p.lng + '" target="_blank" rel="noopener">Navigate to this stop &rarr;</a>' +
        '  </div>' +
        '</li>';
    });
    html += '</ol>';
    out.innerHTML = html;
    out.hidden = false;

    var startBtn = $('#lr-start');
    if (startBtn) startBtn.addEventListener('click', startLive);
  }

  /* ---------- live mode ---------- */
  function startLive() {
    var panel = $('#lr-live');
    if (!panel) return;
    state.live = true;
    state.idx = 0;
    panel.hidden = false;
    panel.scrollIntoView({ behavior: 'smooth', block: 'start' });
    paintLive(null);

    if (!navigator.geolocation) {
      $('#lr-live-gps').textContent = 'This browser will not share your location — use the Maps link instead.';
      return;
    }
    $('#lr-live-gps').textContent = 'Finding you…';
    state.watchId = navigator.geolocation.watchPosition(
      function (pos) {
        paintLive({ lat: pos.coords.latitude, lng: pos.coords.longitude });
      },
      function (err) {
        $('#lr-live-gps').textContent =
          err.code === 1
            ? 'Location permission denied. You can still follow the stops below.'
            : 'Could not get a fix — buildings block GPS. Follow the stops below.';
      },
      { enableHighAccuracy: true, maximumAge: 5000, timeout: 20000 }
    );
  }

  function stopLive() {
    state.live = false;
    if (state.watchId !== null) {
      navigator.geolocation.clearWatch(state.watchId);
      state.watchId = null;
    }
    var panel = $('#lr-live');
    if (panel) panel.hidden = true;
  }

  function paintLive(me) {
    var stop = state.route[state.idx];
    if (!stop) return;
    var p = stop.poi;
    $('#lr-live-name').textContent = p.name;
    $('#lr-live-sub').textContent = stop.isReturn ? 'Last leg — back to 14th Street' : p.sub;
    $('#lr-live-story').textContent = stop.isReturn
      ? 'Drop the bike off, or tell us you want another hour.'
      : p.story;
    $('#lr-live-count').textContent = 'Stop ' + (state.idx + 1) + ' of ' + state.route.length;
    $('#lr-live-nav').href =
      'https://www.google.com/maps/dir/?api=1&destination=' + p.lat + ',' + p.lng;

    if (me) {
      var d = distKm(me, p);
      var dir = compass(bearing(me, p));
      $('#lr-live-gps').innerHTML =
        '<strong>' + km(d) + '</strong> away · head <strong>' + dir + '</strong>';
      // arrived: within 45 m, move on
      if (d < 0.045 && state.idx < state.route.length - 1) {
        state.idx++;
        var el = $('#lr-live');
        el.classList.add('is-arrived');
        setTimeout(function () { el.classList.remove('is-arrived'); }, 1600);
        paintLive(me);
      }
    }
  }

  /* ---------- controls ---------- */
  function wire() {
    $$('[data-lr-mode]').forEach(function (b) {
      b.addEventListener('click', function () {
        $$('[data-lr-mode]').forEach(function (x) { x.classList.remove('is-on'); });
        b.classList.add('is-on');
        state.mode = b.getAttribute('data-lr-mode');
        var cta = $('#lr-mode-cta');
        var m = MODES.filter(function (x) { return x.id === state.mode; })[0];
        if (cta && m) {
          cta.innerHTML = m.blurb + (m.cta
            ? ' <a href="' + m.cta + '">Get one &rarr;</a>' : '');
        }
      });
    });
    $$('[data-lr-mins]').forEach(function (b) {
      b.addEventListener('click', function () {
        $$('[data-lr-mins]').forEach(function (x) { x.classList.remove('is-on'); });
        b.classList.add('is-on');
        state.minutes = parseInt(b.getAttribute('data-lr-mins'), 10);
      });
    });
    $$('[data-lr-tag]').forEach(function (b) {
      b.addEventListener('click', function () {
        var t = b.getAttribute('data-lr-tag');
        var i = state.interests.indexOf(t);
        if (i > -1) { state.interests.splice(i, 1); b.classList.remove('is-on'); }
        else { state.interests.push(t); b.classList.add('is-on'); }
      });
    });
    var go = $('#lr-go');
    if (go) go.addEventListener('click', function () {
      stopLive();
      renderRoute();
      var r = $('#lr-result');
      if (r) r.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
    var end = $('#lr-live-end');
    if (end) end.addEventListener('click', stopLive);
    var skip = $('#lr-live-next');
    if (skip) skip.addEventListener('click', function () {
      if (state.idx < state.route.length - 1) { state.idx++; paintLive(null); }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', wire);
  } else { wire(); }
})();
