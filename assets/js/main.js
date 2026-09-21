/* Miami Beach Bikes & Tours — interactions
   Parallax hero, scroll reveals, sticky nav, mobile menu,
   fleet/tour filtering, counters. No dependencies. */
(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- Sticky nav + mobile toggle ---- */
  var nav = document.querySelector('.nav');
  if (nav) {
    var onScroll = function () { nav.classList.toggle('is-stuck', window.scrollY > 8); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });

    var toggle = nav.querySelector('.nav__toggle');
    if (toggle) {
      toggle.addEventListener('click', function () {
        var open = nav.classList.toggle('is-open');
        document.body.classList.toggle('menu-open', open);
        toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      });
      var close = function () {
        if (!nav.classList.contains('is-open')) return;
        nav.classList.remove('is-open');
        document.body.classList.remove('menu-open');
        toggle.setAttribute('aria-expanded', 'false');
      };
      nav.querySelectorAll('.nav__link').forEach(function (a) {
        a.addEventListener('click', close);
      });
      // an open menu covers the page, so give it the two ways out people
      // already expect: tap anywhere outside it, or press Escape
      document.addEventListener('click', function (ev) {
        // ev.target is the bar itself when the tap lands on its scrim,
        // which is a pseudo-element and so has no node of its own
        if (!nav.contains(ev.target) || ev.target === nav) close();
      });
      document.addEventListener('keydown', function (ev) {
        if (ev.key === 'Escape') close();
      });
    }
  }

  /* ---- Scroll reveal ---- */
  var revealables = document.querySelectorAll('[data-reveal]');
  if (revealables.length) {
    if (reduce || !('IntersectionObserver' in window)) {
      revealables.forEach(function (el) { el.classList.add('is-in'); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
      revealables.forEach(function (el) { io.observe(el); });
    }
  }

  /* ---- Hero parallax ---- */
  var media = document.querySelector('.hero__media');
  if (media && !reduce) {
    var ticking = false;
    var move = function () {
      var y = window.scrollY;
      if (y < window.innerHeight * 1.2) media.style.transform = 'translate3d(0,' + (y * 0.18) + 'px,0)';
      ticking = false;
    };
    window.addEventListener('scroll', function () {
      if (!ticking) { ticking = true; window.requestAnimationFrame(move); }
    }, { passive: true });
  }

  /* ---- Counters ---- */
  var nums = document.querySelectorAll('[data-count]');
  if (nums.length && 'IntersectionObserver' in window) {
    var co = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target, target = parseFloat(el.getAttribute('data-count')),
            suffix = el.getAttribute('data-suffix') || '', dur = 1400, t0 = null;
        if (reduce) { el.textContent = target + suffix; co.unobserve(el); return; }
        var tick = function (ts) {
          if (!t0) t0 = ts;
          var p = Math.min((ts - t0) / dur, 1), eased = 1 - Math.pow(1 - p, 3);
          var v = target * eased;
          el.textContent = (target % 1 ? v.toFixed(1) : Math.round(v)) + suffix;
          if (p < 1) requestAnimationFrame(tick);
        };
        requestAnimationFrame(tick);
        co.unobserve(el);
      });
    }, { threshold: 0.4 });
    nums.forEach(function (n) { co.observe(n); });
  }

  /* ---- Chip filtering (fleet + tours) ---- */
  document.querySelectorAll('[data-filter-group]').forEach(function (group) {
    var targetSel = group.getAttribute('data-filter-target');
    var items = document.querySelectorAll(targetSel + ' [data-cat]');
    group.querySelectorAll('.chip').forEach(function (chip) {
      chip.addEventListener('click', function () {
        group.querySelectorAll('.chip').forEach(function (c) { c.classList.remove('is-active'); });
        chip.classList.add('is-active');
        var f = chip.getAttribute('data-filter');
        items.forEach(function (item) {
          var show = f === 'all' || item.getAttribute('data-cat').split(' ').indexOf(f) > -1;
          item.style.display = show ? '' : 'none';
        });
      });
    });
  });

  /* ---- Finder bar -> rentals page with query ---- */
  var finder = document.querySelector('[data-finder]');
  if (finder) {
    finder.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var data = new FormData(finder), params = new URLSearchParams();
      data.forEach(function (v, k) { if (v) params.set(k, v); });
      var ride = data.get('ride') || 'all';
      window.location.href = (ride === 'tour' ? 'tours.html' : 'rentals.html') + '?' + params.toString();
    });
  }

  /* ---- Apply ?ride= filter on load ---- */
  var qs = new URLSearchParams(window.location.search).get('ride');
  if (qs) {
    var chip = document.querySelector('.chip[data-filter="' + qs + '"]');
    if (chip) chip.click();
  }

  /* ---- Current year ---- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  /* ---- Open/closed status (shop hours 9:00–20:00 ET, daily) ---- */
  document.querySelectorAll('[data-open-status]').forEach(function (el) {
    var now = new Date();
    var et = new Date(now.toLocaleString('en-US', { timeZone: 'America/New_York' }));
    var h = et.getHours();
    var open = h >= 9 && h < 20;
    var T = (window.ASSIST_CONFIG && window.ASSIST_CONFIG.t) || {};
    el.textContent = open ? (T.open_now || 'Open now · until 8 PM')
                          : (T.closed_now || 'Closed · opens 9 AM');
    el.style.color = open ? '#136b45' : '#9a5b00';   // readable on the tan bar
  });

  /* ---- Header height: the nav sits under the address bar ----
     Both are sticky, so the nav's `top` has to be the address bar's real
     height — which changes with the font size, the language and whether the
     opening hours are showing. Measured here instead of guessed in CSS. */
  var topbar = document.querySelector('.topbar');
  if (topbar) {
    var setTopbarH = function () {
      document.documentElement.style.setProperty(
        '--topbar-h', Math.round(topbar.getBoundingClientRect().height) + 'px');
    };
    setTopbarH();
    window.addEventListener('resize', setTopbarH, { passive: true });
    if ('ResizeObserver' in window) new ResizeObserver(setTopbarH).observe(topbar);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(setTopbarH);
  }

  /* ---- Language dropdown ----
     <details> opens and closes itself, but it has no notion of "somewhere
     else" — left alone it stays open behind whatever you click next. */
  var langdrop = document.querySelector('.langdrop');
  if (langdrop) {
    document.addEventListener('click', function (ev) {
      if (!langdrop.contains(ev.target)) langdrop.open = false;
    });
    document.addEventListener('keydown', function (ev) {
      if (ev.key === 'Escape' && langdrop.open) {
        langdrop.open = false;
        var s = langdrop.querySelector('summary');
        if (s) s.focus();
      }
    });
  }

  /* ---- Compact header once you start reading ----
     The pinned header costs 130px of an 844px phone screen. Past the first
     screenful it folds to a slim bar and gives most of that back; scrolling
     up brings it straight back, because that is when people reach for it.

     Names here are deliberately their own: `ticking` and `onScroll` already
     exist in this scope for the parallax and the stuck-nav shadow, and
     sharing the flag meant whichever listener ran first claimed it and the
     other never got a frame. */
  var hdrLastY = 0, hdrTicking = false;
  var hdrScroll = function () {
    var y = window.scrollY || 0;
    var down = y > hdrLastY;
    if (y > 180 && down) document.body.classList.add('is-scrolled');
    else if (!down || y < 90) document.body.classList.remove('is-scrolled');
    hdrLastY = y;
    hdrTicking = false;
  };
  window.addEventListener('scroll', function () {
    if (!hdrTicking) { hdrTicking = true; requestAnimationFrame(hdrScroll); }
  }, { passive: true });

  /* ---- Every page opens at the top ----
     Browsers restore the previous scroll position on a back/forward and, on
     some, when following a link to a page you have already seen. Landing
     halfway down a page you just clicked into reads as a broken link. */
  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
  if (!window.location.hash) {
    // after layout, so a late-loading image cannot drag the page down with it
    requestAnimationFrame(function () { window.scrollTo(0, 0); });
  }
})();
