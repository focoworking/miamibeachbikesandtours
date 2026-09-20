# -*- coding: utf-8 -*-
"""HTML shell: head (SEO/AEO/GEO/LLM), nav, footer."""
import json
from data import BIZ, SITE

NAV = [
    ("rentals.html", "Rentals"),
    ("tours.html", "Tours"),
    ("routes.html", "Routes"),
    ("about.html", "About"),
    ("faq.html", "FAQ"),
    ("contact.html", "Contact"),
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
    "alternateName": ["Miami Beach Bike Rental", "South Beach Bike Rental"],
    "url": SITE + "/",
    "telephone": BIZ["phone"],
    "email": BIZ["email"],
    "priceRange": BIZ["price_range"],
    "currenciesAccepted": "USD",
    "paymentAccepted": "Cash, Credit Card, Debit Card, Apple Pay, Google Pay",
    "image": SITE + "/assets/img/hero-southbeach.svg",
    "logo": SITE + "/assets/img/favicon.svg",
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
    "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.8",
                        "reviewCount": "131", "bestRating": "5"},
    "amenityFeature": [
        {"@type": "LocationFeatureSpecification", "name": "Free Wi-Fi", "value": True},
        {"@type": "LocationFeatureSpecification", "name": "Restroom", "value": True},
        {"@type": "LocationFeatureSpecification", "name": "Hotel delivery", "value": True},
        {"@type": "LocationFeatureSpecification", "name": "On-site repair shop", "value": True},
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


def head(page, title, desc, keywords, extra_ld="", og_img="hero-southbeach"):
    canonical = SITE + "/" + page
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<link rel="canonical" href="{canonical}">
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
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/img/{og_img}.svg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/assets/img/{og_img}.svg">

<!-- LLM / AI answer-engine hints -->
<meta name="ai-content-declaration" content="human-curated business information">
<link rel="alternate" type="text/plain" href="{SITE}/llms.txt" title="llms.txt">

<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/img/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
{ld(LOCALBUSINESS_LD)}
{ld(WEBSITE_LD)}
{extra_ld}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''


def nav(current):
    left = NAV[:3]
    right = NAV[3:]
    def links(items):
        out = []
        for u, n in items:
            cur = ' aria-current="page"' if u == current else ''
            out.append('<a class="nav__link" href="%s"%s>%s</a>' % (u, cur, n))
        return "".join(out)
    return f'''
<div class="topbar"><div class="wrap topbar__in">
  <span>📍 {BIZ['street']}, {BIZ['city']} {BIZ['zip']}</span>
  <span><b data-open-status>Open every day 9 AM – 8 PM</b></span>
  <a href="tel:{BIZ['phone']}">📞 {BIZ['phone_pretty']}</a>
</div></div>
<header class="nav">
  <nav class="wrap nav__in" aria-label="Main">
    <button class="nav__toggle" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    <div class="nav__group">{links(left)}</div>
    <a class="brand" href="index.html" aria-label="{BIZ['name']} home">
      <span class="brand__mark">Miami Beach <span>Bikes &amp; Tours</span></span>
      <span class="brand__sub">South Beach · Since 2009</span>
    </a>
    <div class="nav__group nav__group--right">{links(right)}
      <a class="btn btn--sm" href="contact.html#book">Book now</a>
    </div>
  </nav>
</header>
<main id="main">
'''


def footer():
    return f'''
</main>
<a class="btn fab" href="tel:{BIZ['phone']}">📞 Call &amp; book</a>
<footer class="footer">
  <div class="wrap footer__grid">
    <div>
      <a class="brand" href="index.html">
        <span class="brand__mark">Miami Beach <span>Bikes &amp; Tours</span></span>
        <span class="brand__sub">South Beach · Since 2009</span>
      </a>
      <p style="margin-top:1.1rem;max-width:34ch">Bikes, e-bikes, Segways, skates and guided tours, one block from Ocean Drive. {BIZ['tagline']}</p>
      <div class="badge-row">
        <span class="badge">★ 4.8 · 131 reviews</span>
        <span class="badge">🛠️ On-site repairs</span>
      </div>
    </div>
    <div>
      <h4>Ride</h4>
      <ul>
        <li><a href="rentals.html">Bike rentals</a></li>
        <li><a href="rentals.html?ride=electric">Electric bikes</a></li>
        <li><a href="rentals.html?ride=segways">Segways</a></li>
        <li><a href="rentals.html?ride=skates">Rollerblades</a></li>
        <li><a href="rentals.html?ride=family">Family &amp; kids</a></li>
      </ul>
    </div>
    <div>
      <h4>Explore</h4>
      <ul>
        <li><a href="tours.html">All tours</a></li>
        <li><a href="tours.html?ride=segway">Segway tours</a></li>
        <li><a href="routes.html">South Beach routes</a></li>
        <li><a href="about.html">Our story</a></li>
        <li><a href="faq.html">FAQ</a></li>
      </ul>
    </div>
    <div>
      <h4>Visit</h4>
      <ul>
        <li>{BIZ['street']}<br>{BIZ['city']}, {BIZ['region']} {BIZ['zip']}</li>
        <li><a href="tel:{BIZ['phone']}">{BIZ['phone_pretty']}</a></li>
        <li><a href="mailto:{BIZ['email']}">{BIZ['email']}</a></li>
        <li>{BIZ['hours_pretty']}</li>
      </ul>
    </div>
  </div>
  <div class="wrap footer__bottom">
    <span>© <span data-year></span> {BIZ['legal']}. All rights reserved.</span>
    <span>Bikes · E-bikes · Segways · Skates · Trikes · Tours · South Beach, Florida</span>
  </div>
</footer>
<script src="assets/js/main.js" defer></script>
</body>
</html>'''
