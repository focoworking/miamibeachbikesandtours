# -*- coding: utf-8 -*-
"""HTML shell: head (SEO/AEO/GEO/LLM), nav, footer."""
import json
import json as _json
from i18n import t as _t, pack as _pack
from data import (BIZ, SITE, BOOKING_URL, WHATSAPP_URL, LANGS, POI, MODES,
                  INTERESTS, DURATIONS, EXTEND_BLOCKS, EXTEND_RATES, PAY_METHODS)

NAV = [
    ("rentals.html", "nav_rentals"),
    ("tours.html", "nav_tours"),
    ("adventures.html", "nav_adventures"),
    ("live-route.html", "nav_live"),
    ("routes.html", "nav_routes"),
    ("shop.html", "nav_shop"),
    ("about.html", "nav_about"),
    ("faq.html", "nav_faq"),
    ("contact.html", "nav_contact"),
]

ADDRESS_LD = {
    "@type": "PostalAddress",
    "streetAddress": BIZ["street"],
    "addressLocality": BIZ["city"],
    "addressRegion": BIZ["region"],
    "postalCode": BIZ["zip"],
    "addressCountry": BIZ["country"],
}

LOCALBUSINESS_LD = {
    "@context": "https://schema.org",
    "@type": ["BicycleStore", "TouristInformationCenter"],
    "@id": SITE + "/#business",
    "name": BIZ["name"],
    "alternateName": ["Miami Beach Bikes Rentals & Tours", "Miami Beach Bike Rental",
                      "South Beach Bike Rental", "South Florida Trikke"],
    "url": SITE + "/",
    "telephone": BIZ["phone"],
    "email": BIZ["email"],
    "priceRange": BIZ["price_range"],
    "currenciesAccepted": "USD",
    "paymentAccepted": "Cash, Credit Card, Debit Card, Apple Pay, Google Pay",
    "image": SITE + "/assets/img/hero-southbeach.svg",
    "logo": SITE + "/assets/img/logo-mark.svg",
    "address": ADDRESS_LD,
    "geo": {"@type": "GeoCoordinates", "latitude": BIZ["lat"], "longitude": BIZ["lng"]},
    "hasMap": "https://www.google.com/maps/search/?api=1&query=" + BIZ["lat"] + "," + BIZ["lng"],
    "openingHoursSpecification": [{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "opens": "09:00", "closes": "20:00",
    }],
    "areaServed": [{"@type": "Place", "name": a} for a in BIZ["areas"]],
    "knowsLanguage": ["en", "es", "pt"],
    "slogan": BIZ["tagline"],
    "potentialAction": {
        "@type": "ReserveAction",
        "target": {"@type": "EntryPoint", "urlTemplate": BOOKING_URL,
                   "actionPlatform": ["http://schema.org/DesktopWebPlatform",
                                      "http://schema.org/MobileWebPlatform"]},
        "result": {"@type": "Reservation", "name": "Rental or tour booking"},
    },
    "description": ("Bicycle, fat tire, electric bike, electric tandem, Trikke, Segway, tricycle and rollerblade "
                    "rentals in South Beach, plus guided Segway tours of Ocean Drive, Star Island, the Art Deco "
                    "District and Millionaire's Row, Everglades airboat adventures, Key West day trips, Miami city "
                    "tours, jet skis, parasailing and helicopter rides."),
    "makesOffer": [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n}} for n in
        ["Bicycle rental", "Electric bike rental", "Fat tire bike rental", "Trikke rental",
         "Segway guided tour", "Rollerblade rental", "Tricycle rental", "Tandem bike rental",
         "Everglades airboat adventure", "Key West day trip", "Miami city tour",
         "Jet ski rental", "Parasailing", "Helicopter ride", "Bicycle and e-bike repair",
         "Segway sales", "Trikke sales", "Electric bike sales", "Segway parts and accessories",
         "Longboard rental", "Luggage storage"]],
    "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.8",
                        "reviewCount": "131", "bestRating": "5"},
    "amenityFeature": [
        {"@type": "LocationFeatureSpecification", "name": "Free Wi-Fi", "value": True},
        {"@type": "LocationFeatureSpecification", "name": "Restroom", "value": True},
        {"@type": "LocationFeatureSpecification", "name": "Hotel delivery", "value": True},
        {"@type": "LocationFeatureSpecification", "name": "On-site repair shop", "value": True},
        {"@type": "LocationFeatureSpecification", "name": "Luggage storage", "value": True},
        {"@type": "LocationFeatureSpecification", "name": "Authorized Segway dealer", "value": True},
    ],
}

WEBSITE_LD = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "@id": SITE + "/#website",
    "url": SITE + "/",
    "name": BIZ["name"],
    "inLanguage": "en-US",
    "publisher": {"@id": SITE + "/#business"},
    "potentialAction": {
        "@type": "SearchAction",
        "target": {"@type": "EntryPoint", "urlTemplate": SITE + "/rentals.html?ride={search_term_string}"},
        "query-input": "required name=search_term_string",
    },
}


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "</script>"


def breadcrumbs(items):
    """items: [(name, url_path)] — url_path relative, '' for home."""
    return ld({
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + "/" + u}
            for i, (n, u) in enumerate(items)
        ],
    })


def _attr(v, field):
    """Guard for anything that lands inside an HTML attribute.

    A stray quote or an angle bracket here does not fail loudly — it silently
    swallows the rest of <head> and dumps the raw markup on the page. That is
    exactly how live-route.html and shop.html ended up printing their JSON-LD
    to visitors, so the generator now refuses instead of shipping it.
    """
    v = "" if v is None else str(v)
    if "<" in v or ">" in v:
        raise ValueError("markup in the %s attribute: %r" % (field, v[:80]))
    return v.replace("&", "&amp;").replace('"', "&quot;")


def head(page, title, desc, keywords, extra_ld="", og_img="hero-southbeach", lang="en"):
    title = str(title)
    desc, keywords = _attr(desc, "description"), _attr(keywords, "keywords")
    skip = _t("skip", lang)
    lang_meta = next((l for l in LANGS if l["code"] == lang), LANGS[0])
    prefix = "../" if lang != "en" else ""
    alts = "".join(
        '<link rel="alternate" hreflang="%s" href="%s/%s%s">' % (
            l["code"], SITE, l["dir"], page) for l in LANGS)
    alts += '<link rel="alternate" hreflang="x-default" href="%s/%s">' % (SITE, page)
    canonical_path = lang_meta["dir"] + page
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<link rel="canonical" href="{SITE}/{canonical_path}">
{alts}
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<meta name="author" content="{BIZ['name']}">
<meta name="theme-color" content="#0aa2c0">

<!-- GEO: local + map signals -->
<meta name="geo.region" content="US-FL">
<meta name="geo.placename" content="Miami Beach, Florida">
<meta name="geo.position" content="{BIZ['lat']};{BIZ['lng']}">
<meta name="ICBM" content="{BIZ['lat']}, {BIZ['lng']}">
<meta name="business:contact_data:street_address" content="{BIZ['street']}">
<meta name="business:contact_data:locality" content="{BIZ['city']}">
<meta name="business:contact_data:region" content="{BIZ['region']}">
<meta name="business:contact_data:postal_code" content="{BIZ['zip']}">
<meta name="business:contact_data:country_name" content="United States">
<meta name="business:contact_data:phone_number" content="{BIZ['phone']}">

<!-- Open Graph / Twitter -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BIZ['name']}">
<meta property="og:locale" content="{lang_meta['locale']}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}/{canonical_path}">
<meta property="og:image" content="{SITE}/assets/img/{og_img}.svg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/assets/img/{og_img}.svg">

<!-- LLM / AI answer-engine hints -->
<meta name="ai-content-declaration" content="human-curated business information">
<link rel="alternate" type="text/plain" href="{SITE}/llms.txt" title="llms.txt">

<link rel="icon" href="{prefix}assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{prefix}assets/img/logo-mark.svg">
<link rel="mask-icon" href="{prefix}assets/img/logo-emblem.svg" color="#9b2ff2">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}assets/css/style.css">
{ld(LOCALBUSINESS_LD)}
{ld(WEBSITE_LD)}
{extra_ld}
</head>
<body>
<a class="skip" href="#main">{skip}</a>
'''


def nav(current, lang="en", page=None):
    page = page or current or "index.html"
    prefix = "../" if lang != "en" else ""
    left = NAV[:4]
    right = NAV[4:]
    lang_links = "".join(
        '<a class="lang%s" href="%s%s" hreflang="%s" lang="%s"%s>%s</a>' % (
            " is-on" if l["code"] == lang else "",
            ("../" if lang != "en" else "") + l["dir"], page, l["code"], l["code"],
            ' aria-current="true"' if l["code"] == lang else "", l["short"])
        for l in LANGS)
    lang_short = next((l["short"] for l in LANGS if l["code"] == lang), "EN")
    langdrop_links = "".join(
        '<li><a href="%s%s" hreflang="%s" lang="%s"%s>%s</a></li>' % (
            ("../" if lang != "en" else "") + l["dir"], page, l["code"], l["code"],
            ' aria-current="true"' if l["code"] == lang else "", l["name"])
        for l in LANGS)

    def links(items):
        out = []
        for u, n in items:
            cur = ' aria-current="page"' if u == current else ''
            out.append('<a class="nav__link" href="%s"%s>%s</a>' % (u, cur, _t(n, lang)))
        return "".join(out)
    return f'''
<div class="topbar"><div class="wrap topbar__in">
  <span class="topbar__addr">📍 {BIZ['street']}, {BIZ['city']} {BIZ['zip']}</span>
  <span class="topbar__hours"><b data-open-status>{_t("hours_line", lang)}</b></span>
  <a class="topbar__tel" href="tel:{BIZ['phone']}">📞 {BIZ['phone_pretty']}</a>
  <div class="langs" role="group" aria-label="{_t("lang_label", lang)}">{lang_links}</div>
</div></div>
<header class="nav">
  <nav class="wrap nav__in" aria-label="Main">
    <button class="nav__toggle" aria-label="{_t("nav_menu", lang)}" aria-expanded="false"><span></span><span></span><span></span></button>
    <details class="langdrop">
      <summary aria-label="{_t("nav_lang", lang)}">{lang_short}<svg viewBox="0 0 12 8" width="11" height="8" aria-hidden="true"><path d="M1 1.5 6 6.5l5-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></summary>
      <ul class="langdrop__menu">{langdrop_links}</ul>
    </details>
    <div class="nav__group">{links(left)}</div>
    <a class="brand" href="index.html" aria-label="{BIZ['name']} home">
      <img class="brand__logo" src="{prefix}assets/img/logo-mark.svg" width="52" height="52"
           alt="" loading="eager" decoding="async">
      <span class="brand__text">
        <span class="brand__mark">Miami Beach <span>Bikes</span></span>
        <span class="brand__sub">Rentals &amp; Tours</span>
      </span>
    </a>
    <div class="nav__group nav__group--right">{links(right)}</div>
    <button class="btn btn--sm nav__book" type="button" data-assistant="book">{_t("nav_book", lang)}</button>
  </nav>
</header>
<main id="main">
'''


def footer(lang="en", poi=None, modes=None, interests=None, durations=None):
    poi = POI if poi is None else poi
    modes = MODES if modes is None else modes
    interests = INTERESTS if interests is None else interests
    durations = DURATIONS if durations is None else durations
    T = _pack(lang)
    t_live = T["bar_live"]
    t_book = T["bar_book"]
    prefix = "../" if lang != "en" else ""
    _j = lambda o: _json.dumps(o, ensure_ascii=False, separators=(",", ":"))
    booking = _j(BOOKING_URL)
    phone = _j(BIZ["phone"])
    phone_pretty = _j(BIZ["phone_pretty"])
    poi_j = _j(poi)
    modes_j = _j(modes)
    interests_j = _j(interests)
    durations_j = _j(durations)
    blocks = _j(EXTEND_BLOCKS)
    rates = _j(EXTEND_RATES)
    pay = _j(PAY_METHODS)
    ui = _j(T)
    lang_links = "".join(
        '<li><a href="%s%s" hreflang="%s"%s>%s</a></li>'
        % ("../" if lang != "en" else "", l["dir"] + "index.html", l["code"],
           ' aria-current="true"' if l["code"] == lang else "", l["name"])
        for l in LANGS)
    langcode = _j(lang)
    langdir = _j(prefix)
    return f'''
</main>
<nav class="actionbar" aria-label="Quick actions">
  <a class="actionbar__btn actionbar__btn--wa" href="{WHATSAPP_URL}" target="_blank" rel="noopener">
    <svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.05L2 22l5.1-1.33A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.18-1.14l-.3-.18-3.03.79.81-2.95-.2-.31A8.2 8.2 0 1 1 12 20.2Zm4.5-6.14c-.25-.13-1.46-.72-1.69-.8-.22-.08-.39-.13-.55.13-.16.25-.63.8-.77.96-.14.17-.28.19-.53.06a6.7 6.7 0 0 1-3.35-2.93c-.25-.44.25-.4.72-1.35.08-.17.04-.31-.02-.44-.06-.13-.55-1.34-.76-1.83-.2-.48-.4-.41-.55-.42h-.47a.9.9 0 0 0-.65.3 2.75 2.75 0 0 0-.86 2.05c0 1.2.88 2.37 1 2.53.12.17 1.72 2.63 4.17 3.69 1.55.67 2.16.72 2.94.61.47-.07 1.46-.6 1.66-1.18.21-.58.21-1.07.15-1.18-.06-.1-.23-.17-.48-.3Z"/></svg>
    <span>WhatsApp</span>
  </a>
  <button class="actionbar__btn actionbar__btn--live" type="button" data-assistant="lr-mode">
    <span class="actionbar__ico">
      <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 20 3 17V4l6 3 6-3 6 3v13l-6 3-6-3Z"/><path d="M9 7v13M15 4v13"/></svg>
      <span class="actionbar__dot" aria-hidden="true"></span>
    </span>
    <span>{t_live}</span>
  </button>
  <button class="actionbar__btn actionbar__btn--book" type="button" data-assistant="book">
    <span class="actionbar__ico">
      <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4.5" width="18" height="16" rx="3"/><path d="M8 2.5v4M16 2.5v4M3 10h18M9 15l2 2 4-4"/></svg>
    </span>
    <span>{t_book}</span>
  </button>
</nav>
<button class="as-fab" type="button" data-assistant="home">
  <span class="as-fab__dot" aria-hidden="true"></span> Assistant
</button>
<footer class="footer">
  <div class="wrap footer__grid">
    <div>
      <a class="brand" href="index.html">
        <img class="brand__logo" src="{prefix}assets/img/logo-emblem.svg" width="64" height="64" alt="" loading="lazy">
        <span class="brand__text">
          <span class="brand__mark">Miami Beach <span>Bikes</span></span>
          <span class="brand__sub">Rentals &amp; Tours</span>
        </span>
      </a>
      <p style="margin-top:1.1rem;max-width:34ch">{T["f_tagline"]}</p>
      <div class="badge-row">
        <span class="badge">★ {T["f_reviews"]}</span>
        <span class="badge">🛠️ {T["f_repairs"]}</span>
      </div>
      <address class="footer__addr">
        <a href="https://www.google.com/maps/search/?api=1&amp;query={BIZ['lat']},{BIZ['lng']}" target="_blank" rel="noopener">{BIZ['street']}<br>{BIZ['city']}, {BIZ['region']} {BIZ['zip']}</a>
        <a href="tel:{BIZ['phone']}">{BIZ['phone_pretty']}</a>
        <a href="mailto:{BIZ['email']}">{BIZ['email']}</a>
        <span>{T["hours_pretty"]}</span>
      </address>
    </div>
    <div>
      <h4>{T["f_rent"]}</h4>
      <ul>
        <li><a href="rentals.html?ride=bikes">{T["fl_bikes"]}</a></li>
        <li><a href="rentals.html#fat-tire-bike">{T["fl_fat"]}</a></li>
        <li><a href="rentals.html?ride=electric">{T["fl_electric"]}</a></li>
        <li><a href="rentals.html?ride=trikke">{T["fl_trikke"]}</a></li>
        <li><a href="rentals.html?ride=segways">{T["fl_segway"]}</a></li>
        <li><a href="rentals.html?ride=skates">{T["fl_skates"]}</a></li>
        <li><a href="rentals.html?ride=family">{T["fl_family"]}</a></li>
        <li><a href="rentals.html#fleet-grid">{T["fl_rates"]}</a></li>
      </ul>
    </div>
    <div>
      <h4>{T["f_tourshead"]}</h4>
      <ul>
        <li><a href="tours.html">{T["fl_alltours"]}</a></li>
        <li><a href="tours.html?ride=segway">{T["fl_segtours"]}</a></li>
        <li><a href="tours.html?ride=bike">{T["fl_biketours"]}</a></li>
        <li><a href="tours.html?ride=free">{T["fl_free"]}</a></li>
        <li><a href="tours.html?ride=night">{T["fl_night"]}</a></li>
        <li><a href="adventures.html#everglades-airboat-adventure">{T["fl_glades"]}</a></li>
        <li><a href="adventures.html#key-west-day-trip">{T["fl_keywest"]}</a></li>
        <li><a href="adventures.html?ride=water">{T["fl_water"]}</a></li>
      </ul>
    </div>
    <div>
      <h4>{T["f_shop"]}</h4>
      <ul>
        <li><a href="shop.html#segway-sales">{T["fl_buyseg"]}</a></li>
        <li><a href="shop.html#trikke-sales">{T["fl_buytrikke"]}</a></li>
        <li><a href="shop.html#ebike-sales">{T["fl_buyebike"]}</a></li>
        <li><a href="shop.html#segway-accessories">{T["fl_parts"]}</a></li>
        <li><a href="shop.html#repairs-service">{T["fl_repairs"]}</a></li>
      </ul>
      <h4 style="margin-top:2rem">{T["f_langs"]}</h4>
      <ul class="footer__langs">{lang_links}</ul>
    </div>
    <div>
      <h4>{T["f_plan"]}</h4>
      <ul>
        <li><a href="live-route.html">{T["fl_live"]}</a></li>
        <li><a href="index.html#landmarks">{T["fl_landmarks"]}</a></li>
        <li><a href="routes.html">{T["fl_routes"]}</a></li>
        <li><a href="faq.html">{T["fl_faq"]}</a></li>
        <li><a href="about.html">{T["fl_about"]}</a></li>
        <li><a href="contact.html">{T["fl_contact"]}</a></li>
        <li><a href="{BOOKING_URL}" target="_blank" rel="noopener">{T["f_bookonline"]}</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap footer__bottom">
    <span>© <span data-year></span> {BIZ['legal']}. {T["f_rights"]}</span>
    <span class="footer__by">Powered by <a href="https://focoworking.com/discover/" target="_blank" rel="noopener">FOCOworking Miami</a> &middot; Marketing Solutions</span>
  </div>
</footer>
<script>
window.ASSIST_CONFIG={{
  /* Wire these two to go live. Until lookupUrl is set the panel runs in
     demo mode and says so on screen. */
  lookupUrl:null,      /* e.g. "/api/rental/{{ref}}" -> rental JSON */
  payUrl:null,         /* e.g. your hosted checkout; gets ref, block, method */
  bookUrl:{booking},
  phone:{phone},
  phonePretty:{phone_pretty},
  lang:{langcode},
  links:{{rentals:"rentals.html",tours:"tours.html",adventures:"adventures.html"}},
  t:{ui}
}};
window.LR_POI={poi_j};
window.LR_MODES={modes_j};
window.LR_INTERESTS={interests_j};
window.LR_DURATIONS={durations_j};
window.LR_EXTEND={{blocks:{blocks},rates:{rates},pay:{pay}}};
</script>
<script src="{prefix}assets/js/main.js" defer></script>
<script src="{prefix}assets/js/assistant.js" defer></script>
</body>
</html>'''
