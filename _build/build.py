# -*- coding: utf-8 -*-
"""Builds every static page from data.py + shell.py. Run: python3 _build/build.py"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import (BIZ, SITE, BOOKING_URL, FLEET, TOURS, ADVENTURES, SHOP, ROUTES,
                  FAQ, REVIEWS, POI, MODES, INTERESTS, DURATIONS)
import data
import shell
from shell import head, nav, footer, ld, breadcrumbs, ADDRESS_LD
from i18n import t as _t, pack as _pack
import content as _content
from data import LANGS, WHATSAPP_URL

LANG = "en"   # rebound once per language pass in __main__


def head(*a, **kw):
    kw.setdefault("lang", LANG)
    return shell.head(*a, **kw)


def nav(current, page=None):
    return shell.nav(current, lang=LANG, page=page or current)


def footer():
    return shell.footer(lang=LANG, poi=POI, modes=MODES,
                        interests=INTERESTS, durations=DURATIONS)


def T(key):
    return _t(key, LANG)


ROUTE_COVER = {
    # six routes were all showing the same map illustration; each one now
    # leads with the landmark it is actually named after
    "the-beachwalk-classic": "poi-beachwalk14",
    "art-deco-neon-loop": "poi-colony",
    "star-island-&-the-causeway": "poi-macarthur",
    "venetian-islands-sunset": "poi-belleisle",
    "wynwood-mural-run": "tour-ebike-wynwood",
    "north-beach-&-boardwalk": "poi-faena",
}


def route_cover(r, slug=None):
    """Illustration for a route card, keyed off the English name so it
    survives translation."""
    key = slug or r.get("slug") or r["name"].lower().replace(" ", "-").replace("'", "")
    return ROUTE_COVER.get(key, "routes-map")


def poi_cover(p):
    """The cover image for a landmark.

    Default: the illustration drawn for that exact place. If the client fills
    in STREETVIEW_KEY, every card switches to an official Google Street View
    still at the landmark's own coordinates — which is the licensed way to put
    a real photograph of these places on a commercial site. Scraping the same
    image out of Google Maps is not.
    """
    key = getattr(data, "STREETVIEW_KEY", "")
    if key:
        return ("https://maps.googleapis.com/maps/api/streetview?size=1200x750"
                "&location=%s,%s&fov=78&pitch=6&source=outdoor&key=%s"
                % (p["lat"], p["lng"], key))
    return "%sassets/img/poi-%s.svg" % ("../" if LANG != "en" else "", p["id"])


def use_language(code):
    """Rebind LANG and swap every catalogue for its localised copy."""
    global LANG, FLEET, TOURS, ADVENTURES, SHOP, ROUTES, FAQ, POI
    global MODES, INTERESTS, DURATIONS, REVIEWS
    LANG = code
    loc = _content.localise(data, code)
    FLEET = loc["FLEET"]; TOURS = loc["TOURS"]; ADVENTURES = loc["ADVENTURES"]
    SHOP = loc["SHOP"]; ROUTES = loc["ROUTES"]; FAQ = loc["FAQ"]; POI = loc["POI"]
    MODES = loc["MODES"]; INTERESTS = loc["INTERESTS"]; DURATIONS = loc["DURATIONS"]
    REVIEWS = loc["REVIEWS"]

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def write(name, html):
    open(os.path.join(ROOT, name), "w", encoding="utf-8").write(html)
    print("  ->", name, len(html) // 1024, "KB")

# ---------------------------------------------------------------- components
BOOK_ATTRS = 'href="%s" target="_blank" rel="noopener"' % BOOKING_URL
CALL_ATTRS = 'href="tel:%s"' % BIZ["phone"]


def offer(price, url):
    """Schema.org Offer. Price is omitted when the operator has not published one."""
    o = {"@type": "Offer", "priceCurrency": "USD",
         "availability": "https://schema.org/InStock",
         "url": url, "seller": {"@id": SITE + "/#business"}}
    if price is not None:
        o["price"] = str(price)
    else:
        o["availability"] = "https://schema.org/InStoreOnly"
    return o


def price_tag(price, unit_label):
    """Money block. Items with no published price ask for a call instead."""
    if price is None:
        return ('<span class="price price--ask">' + T("u_ask") +
                '<small>%s</small></span>' % unit_label)
    return '<span class="price">$%s<small>%s</small></span>' % (price, unit_label)


def book_btn(price, extra="btn--ocean", label="Book"):
    if price is None:
        return '<a class="btn btn--sm %s" %s>Call to book</a>' % (extra, CALL_ATTRS)
    return '<a class="btn btn--sm %s" %s>%s</a>' % (extra, BOOK_ATTRS, label)


def money(v):
    return "Call for price" if v is None else "$%s" % v


def img(slug, alt, cls=""):
    return ('<img src="assets/img/%s.svg" alt="%s" width="1200" height="900" '
            'loading="lazy" decoding="async"%s>') % (slug, alt, (' class="%s"' % cls) if cls else "")

def fleet_card(p, delay=0):
    meta = "".join("<span>✓ %s</span>" % m for m in p["meta"])
    tagcls = "card__tag card__tag--hot" if p["tag"] in ("Most booked", "Go further") else "card__tag"
    return f'''
<article class="card" data-cat="{p['cat']}" data-reveal data-delay="{delay}" id="{p['slug']}">
  <div class="card__media"><span class="{tagcls}">{p['tag']}</span>{img(p['img'], p['name'] + ' rental in South Beach, Miami Beach')}</div>
  <div class="card__body">
    <h3>{p['name']}</h3>
    <div class="card__meta">{meta}</div>
    <p>{p['hook']}</p>
    <div class="card__foot">
      {price_tag(p['price'], 'per ' + p['unit'])}
      {book_btn(p['price'])}
    </div>
  </div>
</article>'''

def tour_card(t, delay=0):
    meta = "".join("<span>✓ %s</span>" % m for m in t["meta"])
    return f'''
<article class="card" data-cat="{t['cat']}" data-reveal data-delay="{delay}" id="{t['slug']}">
  <div class="card__media"><span class="card__tag">{t['tag']}</span>{img(t['img'], t['name'] + ' in Miami Beach')}</div>
  <div class="card__body">
    <h3>{t['name']}</h3>
    <div class="card__meta">{meta}</div>
    <p>{t['hook']}</p>
    <p class="note"><strong>Stops:</strong> {" · ".join(t['stops'])}</p>
    <div class="card__foot">
      {price_tag(t['price'], ((T("u_from") + ' · ') if t['price'] else '') + t['dur_pretty'])}
      {book_btn(t['price'], extra='')}
    </div>
  </div>
</article>'''

def faq_block(items):
    out = ['<div class="faq">']
    for q, a in items:
        out.append(f'<details data-reveal><summary>{q}</summary><p>{a}</p></details>')
    out.append("</div>")
    return "".join(out)

def faq_ld(items):
    return ld({"@context": "https://schema.org", "@type": "FAQPage",
               "mainEntity": [{"@type": "Question", "name": q,
                               "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]})

def speakable():
    return ld({"@context": "https://schema.org", "@type": "WebPage",
               "speakable": {"@type": "SpeakableSpecification",
                             "cssSelector": [".hero h1", ".hero__sub", ".answer-box", ".faq summary", ".faq p"]}})

def reviews_section():
    cards = "".join(f'''
<figure class="review" data-reveal data-delay="{i%3+1}">
  <div class="review__stars">★★★★★</div>
  <blockquote>{q}</blockquote>
  <figcaption>{who}</figcaption>
</figure>''' for i, (q, who) in enumerate(REVIEWS))
    return f'''
<section class="sec band-sand">
  <div class="wrap">
    <div class="center" data-reveal>
      <span class="eyebrow">Riders talking</span>
      <h2>4.8 stars from 131 riders</h2>
      <p class="lead">Families, couples, cruise-ship day-trippers and locals who just need a tune-up.</p>
    </div>
    <div class="grid grid--3" style="margin-top:3rem">{cards}</div>
  </div>
</section>'''

def cta_section(title, text, primary=None, external=True):
    if primary is None:
        primary, external = ("Book online", BOOKING_URL), True
    tgt = ' target="_blank" rel="noopener"' if external and primary[1].startswith("http") else ""
    return f'''
<section class="sec--tight" style="padding-bottom:clamp(4rem,8vw,7rem)">
  <div class="wrap">
    <div class="cta-band" data-reveal>
      <span class="eyebrow eyebrow--light">Ready when you are</span>
      <h2>{title}</h2>
      <p class="lead" style="color:rgba(255,255,255,.92);margin-inline:auto">{text}</p>
      <div class="btn-row btn-row--center" style="margin-top:1.6rem">
        <a class="btn btn--dark" href="{primary[1]}"{tgt}>{primary[0]}</a>
        <a class="btn btn--ghost" href="tel:{BIZ['phone']}">Call {BIZ['phone_pretty']}</a>
      </div>
    </div>
  </div>
</section>'''

def answer_box(question, answer):
    """AEO: explicit, extractable question/answer pair near the top of a page."""
    return f'''
<section class="sec--tight">
  <div class="wrap">
    <div class="tile answer-box" data-reveal>
      <h2>{question}</h2>
      <p>{answer}</p>
    </div>
  </div>
</section>'''

def marquee():
    words = ["Beach cruisers", "Fat tire bikes", "Electric bikes", "Electric tandems", "Trikkes",
             "Segway tours", "Side-by-sides", "Rollerblades", "Kids bikes", "Everglades airboats",
             "Key West day trips", "Jet skis", "Parasailing", "Helicopter rides", "Hotel delivery",
             "Same-day repairs", "Happy hour 1\u20134 PM"]
    row = "".join("<span>%s</span>" % w for w in words)
    return f'<div class="marquee" aria-hidden="true"><div class="marquee__track">{row}{row}</div></div>'

# ---------------------------------------------------------------- pages
def _data_faq_en():
    return data.FAQ


HOME_FAQ_KEYS = [
    "Where can I rent a bike in South Beach?",
    "How much does it cost to rent a bike in Miami Beach?",
    "How much are the Segway tours?",
    "What is the happy hour special?",
    "What is Live Route?",
    "Can I extend my rental without coming back to the shop?",
    "What else do you book besides bikes and Segways?",
]
_HOME_FAQ_IDX = [i for i, f in enumerate(_data_faq_en()) if f[0] in HOME_FAQ_KEYS]


def home_faq():
    """The seven questions the home page answers.

    Picked by position, not by English text: this used to be evaluated once at
    import time against the English catalogue, so every translated home page
    shipped the English answers.
    """
    return [FAQ[i] for i in _HOME_FAQ_IDX if i < len(FAQ)]


def page_index():
    extra = "".join([
        speakable(),
        faq_ld(home_faq()),
        breadcrumbs([("Home", "")]),
        ld({"@context": "https://schema.org", "@type": "ItemList",
            "name": "Rentals and tours in Miami Beach",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": p["name"],
                 "url": SITE + "/rentals.html#" + p["slug"]} for i, p in enumerate(FLEET)] +
                [{"@type": "ListItem", "position": len(FLEET) + i + 1, "name": t["name"],
                  "url": SITE + "/tours.html#" + t["slug"]} for i, t in enumerate(TOURS)] +
                [{"@type": "ListItem", "position": len(FLEET) + len(TOURS) + i + 1, "name": a["name"],
                  "url": SITE + "/adventures.html#" + a["slug"]} for i, a in enumerate(ADVENTURES)]}),
    ])
    h = head("index.html",
             T("t.index"),
             T("d.index"),
             "miami beach bike rental, south beach bike rental, segway tour miami, electric bike rental miami beach, "
             "rollerblade rental south beach, miami beach bike tours, ocean drive bike rental, "
             "segway dealer miami, trikke miami beach, free bike tour wynwood",
             extra)
    fleet = "".join(fleet_card(p, i % 4 + 1) for i in range(len(FLEET)) for p in [FLEET[i]])
    tours = "".join(tour_card(t, i % 3 + 1) for i, t in enumerate(TOURS[:3]))
    adventures = "".join(tour_card(a, i % 3 + 1) for i, a in enumerate(ADVENTURES[:3]))
    routes = "".join(f'''
<article class="tile tile--shot" data-reveal data-delay="{i%3+1}">
  <span class="tile__shot"><img src="assets/img/{route_cover(r)}.svg" alt="" width="1200" height="750" loading="lazy" decoding="async"></span>
  <h3>{r['name']}</h3>
  <div class="card__meta"><span>{r['km']}</span><span>{r['time']}</span><span>{r['level']}</span></div>
  <p>{r['desc']}</p>
</article>''' for i, r in enumerate(ROUTES[:3]))

    landmark_ids = ("espanola", "lummus", "versace", "newworld",
                    "boardwalk", "southpointepier", "faena", "fontainebleau")
    by_id = {p["id"]: p for p in POI}
    landmarks = "".join(f'''
<a class="lm" href="live-route.html#stop-{lp['id']}" data-reveal data-delay="{i%4+1}">
  <span class="lm__media"><img src="{poi_cover(lp)}" alt="{lp['name']} — {lp['sub']}" width="1200" height="750" loading="lazy" decoding="async"></span>
  <span class="lm__body"><b>{lp['name']}</b><span>{lp['sub']}</span></span>
</a>''' for i, lp in enumerate(by_id[k] for k in landmark_ids if k in by_id))

    return h + nav("index.html") + f'''
<section class="hero">
  <div class="hero__media">{img("hero-southbeach", "Sunset over the palm trees and Art Deco skyline of South Beach, Miami Beach")}</div>
  <div class="hero__scrim"></div>
  <div class="wrap hero__in">
    <span class="eyebrow eyebrow--light">South Beach · 233 14th Street</span>
    <h1>{T("h.hero1")}<br><em>{T("h.hero2")}</em></h1>
    <p class="hero__sub">{T("h.hero_sub_a")}<span class="hero__sub--long">{T("h.hero_sub_long")}</span><span class="hero__sub--short">{T("h.hero_sub_short")}</span></p>
    <div class="hero__cta">
      <a class="btn" href="rentals.html">{T("h.cta_rent")}</a>
      <a class="btn btn--ghost" href="tours.html">{T("h.cta_tours")}</a>
    </div>

  </div>
  
</section>

<div class="wrap finder">
  <form class="finder__card" data-finder data-reveal aria-label="Find your ride">
    <div class="finder__field">
      <label for="f-ride">What do you want to ride?</label>
      <select id="f-ride" name="ride">
        <option value="all">Anything with wheels</option>
        <option value="bikes">Bikes &amp; cruisers</option>
        <option value="electric">Electric bikes</option>
        <option value="segways">Segways</option>
        <option value="skates">Rollerblades</option>
        <option value="family">Family &amp; kids</option>
        <option value="tour">Guided tour</option>
      </select>
    </div>
    <div class="finder__field">
      <label for="f-when">When</label>
      <input id="f-when" name="when" type="date">
    </div>
    <div class="finder__field">
      <label for="f-long">How long</label>
      <select id="f-long" name="duration">
        <option>1 hour</option><option>2 hours</option><option>4 hours</option>
        <option selected>24 hours</option><option>1 week</option><option>1 month</option>
      </select>
    </div>
    <div class="finder__field">
      <label for="f-riders">Riders</label>
      <select id="f-riders" name="riders">
        <option>1 rider</option><option selected>2 riders</option><option>3–4 riders</option>
        <option>5–8 riders</option><option>Group 9+</option>
      </select>
    </div>
    <button class="btn btn--ocean" type="submit">Find it</button>
  </form>
</div>

<section class="sec--tight" style="padding-top:2.2rem;padding-bottom:0">
  <div class="wrap">
    <div class="trust" data-reveal>
      <span class="trust__i">&#9733; {T("tr.reviews")}</span>
      <span class="trust__i">&#128690; {T("tr.included")}</span>
      <span class="trust__i">&#127976; {T("tr.delivery")}</span>
      <span class="trust__i">&#9200; {T("tr.happy")}</span>
      <span class="trust__i">&#127912; {T("tr.freetours")}</span>
    </div>
  </div>
</section>

{marquee()}

{answer_box(T("ab.index_q"), T("ab.index_a"))}

<section class="sec band-ocean">
  <div class="wrap split">
    <div data-reveal>
      <span class="eyebrow eyebrow--light">New &middot; free for everyone</span>
      <h2 style="color:#fff">Live Route: a tour guide in your pocket</h2>
      <p class="lead">Tell it how you are moving, how long you have and what you like. It builds a route from our door on Washington and 14th through the South Beach worth seeing &mdash; Espa&ntilde;ola Way, the Versace Mansion, the Lummus lifeguard towers, South Pointe &mdash; then guides you stop by stop while you ride, using your phone's location.</p>
      <div class="badge-row">
        <span class="badge">&#128694; 6 ways to travel</span>
        <span class="badge">&#9201;&#65039; 30 min to half a day</span>
        <span class="badge">&#128205; 23 landmarks</span>
      </div>
      <div class="btn-row" style="margin-top:1.6rem">
        <a class="btn btn--sun" href="live-route.html">Build my route</a>
        <a class="btn btn--ghost" href="live-route.html#plan">See how it works</a>
      </div>
    </div>
    <div class="split__media" data-reveal data-delay="2">{img("routes-map", "Live Route map of iconic South Beach stops")}</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="center" data-reveal>
      <span class="eyebrow">The fleet</span>
      <h2>Pick your wheels</h2>
      <p class="lead">Every rental comes with a helmet, a lock, cold water and a printed route map. Rent from one hour to sixty days.</p>
    </div>
    <div class="chips" data-filter-group data-filter-target="#fleet-grid" style="margin-top:2.2rem" role="tablist">
      <button class="chip is-active" data-filter="all">All</button>
      <button class="chip" data-filter="bikes">Bikes</button>
      <button class="chip" data-filter="electric">Electric</button>
      <button class="chip" data-filter="trikke">Trikke</button>
      <button class="chip" data-filter="segways">Segways</button>
      <button class="chip" data-filter="skates">Skates</button>
      <button class="chip" data-filter="family">Family</button>
    </div>
    <div class="grid grid--3" id="fleet-grid">{fleet}</div>
    <div class="center" style="margin-top:2.6rem"><a class="btn btn--ocean" href="rentals.html">All rentals &amp; full price list</a></div>
  </div>
</section>

<section class="sec band-dark">
  <div class="wrap split">
    <div data-reveal>
      <span class="eyebrow eyebrow--light">Guided tours</span>
      <h2 style="color:#fff">Someone who actually knows the island</h2>
      <p class="lead">Our guides grew up on this sand. One hour on Ocean Drive for $49, or 2.5 hours up Millionaire\u2019s Row for $89 — you get the neon, the mansions and the stories behind them, at a pace that works for grandparents and fourteen-year-olds alike.</p>
      <div class="stats" style="margin:2rem 0">
        <div class="stat"><div class="stat__n" data-count="12">0</div><div class="stat__l">Tours &amp; trips</div></div>
        <div class="stat"><div class="stat__n" data-count="49" data-suffix="$">0</div><div class="stat__l">Segway tour from</div></div>
        <div class="stat"><div class="stat__n" data-count="4.8">0</div><div class="stat__l">Rating</div></div>
      </div>
      <a class="btn btn--sun" href="tours.html">Browse every tour</a>
    </div>
    <div class="split__media" data-reveal data-delay="2">{img("tour-segway-deco", "Guided Segway tour passing the Art Deco hotels of Ocean Drive")}</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="center" data-reveal>
      <span class="eyebrow">Most booked</span>
      <h2>Start with one of these three</h2>
    </div>
    <div class="grid grid--3" style="margin-top:2.6rem">{tours}</div>
  </div>
</section>

<section class="sec band-ocean">
  <div class="wrap">
    <div class="center" data-reveal>
      <span class="eyebrow eyebrow--light">Beyond the island</span>
      <h2 style="color:#fff">Airboats, the Keys, jet skis and a helicopter</h2>
      <p class="lead">Book the whole of South Florida at the same counter where you pick up your bike. Most day trips include hotel pickup.</p>
    </div>
    <div class="grid grid--3" style="margin-top:3rem">{adventures}</div>
    <div class="center" style="margin-top:2.6rem"><a class="btn btn--sun" href="adventures.html">All adventures &amp; day trips</a></div>
  </div>
</section>

<section class="sec band-sand">
  <div class="wrap">
    <div class="center" data-reveal>
      <span class="eyebrow">How it works</span>
      <h2>Wheels under you in ten minutes</h2>
    </div>
    <div class="steps" style="margin-top:3rem">
      <div class="step" data-reveal data-delay="1"><h3>Pick your ride</h3><p>Choose online, call us, or just walk in — we are one block off Ocean Drive and we keep spare bikes for walk-ups all day.</p></div>
      <div class="step" data-reveal data-delay="2"><h3>Get fitted</h3><p>Seat height, helmet, lock and a two-minute safety brief. Segway riders get a full training session on the spot.</p></div>
      <div class="step" data-reveal data-delay="3"><h3>Take the map</h3><p>We mark the best route for your time, your legs and the day's wind, and we stay reachable by phone while you ride.</p></div>
      <div class="step" data-reveal data-delay="4"><h3>Roll back in</h3><p>Return to the shop or leave it at your hotel — for 24-hour rentals in South Beach we come and get it, free.</p></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap split split--flip">
    <div class="split__media" data-reveal>{img("routes-map", "Map of cycling routes across South Beach and Miami Beach")}</div>
    <div data-reveal data-delay="2">
      <span class="eyebrow">Free route guides</span>
      <h2>Where to actually ride</h2>
      <p class="lead">South Beach is flat, compact and laced with protected bike lanes plus a car-free Beachwalk that runs the length of the sand. These are the routes we hand our own friends.</p>
      <div class="grid" style="gap:1rem;margin-top:1.6rem">{routes}</div>
      <a class="btn btn--ocean" style="margin-top:1.6rem" href="routes.html">All six routes</a>
    </div>
  </div>
</section>

<section class="sec band-sand" id="landmarks">
  <div class="wrap">
    <div class="center" data-reveal>
      <span class="eyebrow">{T("lm.eyebrow")}</span>
      <h2>{T("lm.h2")}</h2>
      <p class="lead">{T("lm.lead")}</p>
    </div>
    <div class="lm-grid">{landmarks}</div>
    <div class="center" style="margin-top:2.4rem" data-reveal>
      <a class="btn btn--ocean" href="live-route.html">{T("lm.cta")}</a>
    </div>
  </div>
</section>

{reviews_section()}

<section class="sec">
  <div class="wrap">
    <div class="center" data-reveal>
      <span class="eyebrow">Good to know</span>
      <h2>Questions, answered</h2>
    </div>
    <div style="margin-top:2.6rem">{faq_block(home_faq())}</div>
    <div class="center" style="margin-top:2rem"><a class="btn btn--sm btn--ocean" href="faq.html">Read all FAQs</a></div>
  </div>
</section>

{cta_section("Your bike is already waiting on 14th Street",
 "Walk in any day between 9 AM and 8 PM, or reserve ahead and we will have it fitted and ready when you arrive.")}
''' + footer()


def page_rentals():
    rows = ""
    for p in FLEET:
        for label, price in p["rates"]:
            rows += f"<tr><td><strong>{p['name']}</strong></td><td>{label}</td><td>{money(price) if price else 'Ask at the shop'}</td></tr>"
    products_ld = ld({
        "@context": "https://schema.org", "@type": "ItemList", "name": "Bike and vehicle rentals in Miami Beach",
        "itemListElement": [{
            "@type": "ListItem", "position": i + 1,
            "item": {
                "@type": "Product", "name": p["name"], "description": p["hook"],
                "image": SITE + "/assets/img/" + p["img"] + ".svg",
                "url": SITE + "/rentals.html#" + p["slug"],
                "brand": {"@type": "Brand", "name": BIZ["name"]},
                "offers": offer(p["price"], SITE + "/rentals.html#" + p["slug"]),
            }} for i, p in enumerate(FLEET)]})
    extra = "".join([speakable(), products_ld,
                     faq_ld([f for f in FAQ if f[0] in
                             ("How much does it cost to rent a bike in Miami Beach?",
                              "What is the happy hour special?", "What is a Trikke?",
                              "What is included with a rental?", "How long can I keep the bike?",
                              "Do you deliver bikes to my hotel?")]),
                     breadcrumbs([("Home", ""), ("Rentals", "rentals.html")])])
    h = head("rentals.html",
             T("t.rentals"),
             T("d.rentals"),
             "bike rental miami beach prices, fat tire bike rental south beach, electric bike rental south beach, "
             "trikke rental miami, electric tandem rental miami beach, side by side bike rental, "
             "rollerblade rental miami beach, kids bike rental miami beach",
             extra, og_img="fleet-cruiser")
    cards = "".join(fleet_card(p, i % 3 + 1) for i, p in enumerate(FLEET))
    return h + nav("rentals.html") + f'''
<section class="phead">
  <div class="wrap phead__in" data-reveal>
    <p class="crumbs"><a href="index.html">Home</a> · Rentals</p>
    <h1 style="font-size:clamp(2.3rem,5.5vw,4.2rem)">{T("p.rentals_h")}</h1>
    <p class="lead">{T("p.rentals_lead")}</p>
  </div>
</section>

{answer_box(T("ab.rentals_q"), T("ab.rentals_a"))}

<section class="sec">
  <div class="wrap">
    <div class="chips" data-filter-group data-filter-target="#fleet-grid" role="tablist">
      <button class="chip is-active" data-filter="all">All</button>
      <button class="chip" data-filter="bikes">Bikes</button>
      <button class="chip" data-filter="electric">Electric</button>
      <button class="chip" data-filter="trikke">Trikke</button>
      <button class="chip" data-filter="segways">Segways</button>
      <button class="chip" data-filter="skates">Skates</button>
      <button class="chip" data-filter="family">Family</button>
    </div>
    <div class="grid grid--3" id="fleet-grid">{cards}</div>
  </div>
</section>

<section class="sec band-sand">
  <div class="wrap">
    <div class="center" data-reveal>
      <span class="eyebrow">No surprises</span>
      <h2>Full price list</h2>
      <p class="lead">All prices in US dollars. The longer you ride, the less it costs — a week runs about the same as three single days.</p>
    </div>
    <div class="table-wrap" style="margin-top:2.4rem" data-reveal>
      <table>
        <caption class="sr-only">Rental rates for bikes, electric bikes, Segways, skates and tricycles in Miami Beach</caption>
        <thead><tr><th scope="col">Ride</th><th scope="col">Duration</th><th scope="col">Price</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
    <p class="note center" style="margin-top:1.2rem">Monthly and seasonal rates available on request. Group of 6 or more? Call {BIZ['phone_pretty']} for group pricing.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap grid grid--4">
    <div class="tile" data-reveal data-delay="1"><div class="tile__ico">🏨</div><h3>Hotel delivery</h3><p>Free across South Beach on rentals of 24 hours or more. Mid-Beach, North Beach and Downtown by flat fee.</p></div>
    <div class="tile" data-reveal data-delay="2"><div class="tile__ico">🛠️</div><h3>Repair shop</h3><p>Flats, brakes, gears, batteries and full tune-ups for bikes, e-bikes and scooters. Most walk-ins same day.</p></div>
    <div class="tile" data-reveal data-delay="3"><div class="tile__ico">👨‍👩‍👧‍👦</div><h3>Family gear</h3><p>Baby seats, trailers, training wheels and tandems, so nobody stays behind at the hotel.</p></div>
    <div class="tile" data-reveal data-delay="4"><div class="tile__ico">⏳</div><h3>Extend from your phone</h3><p>Running long? Open the assistant, enter your ticket number and add an hour, a day or a week \u2014 paid on your phone, no ride back. <button class="tile__link" type="button" data-assistant="ex-lookup">Extend a rental &rarr;</button></p></div>
  </div>
</section>

{reviews_section()}
{cta_section("Reserve your wheels for tomorrow morning",
 "Tell us the day, the hours and how many of you there are. We will have everything fitted and waiting at 233 14th Street.")}
''' + footer()


def page_tours():
    tour_lds = [ld({
        "@context": "https://schema.org", "@type": "TouristTrip",
        "name": t["name"], "description": t["hook"],
        "url": SITE + "/tours.html#" + t["slug"],
        "image": SITE + "/assets/img/" + t["img"] + ".svg",
        "touristType": "Families, couples, groups",
        "provider": {"@id": SITE + "/#business"},
        "itinerary": {"@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1,
             "item": {"@type": "TouristAttraction", "name": s,
                      "address": {"@type": "PostalAddress", "addressLocality": "Miami Beach",
                                  "addressRegion": "FL", "addressCountry": "US"}}}
            for i, s in enumerate(t["stops"])]},
        "offers": offer(t["price"], SITE + "/tours.html#" + t["slug"]),
    }) for t in TOURS]
    extra = "".join([speakable(), breadcrumbs([("Home", ""), ("Tours", "tours.html")]),
                     faq_ld([f for f in FAQ if f[0] in
                             ("How old do you have to be to ride a Segway or a Trikke?",
                              "How much are the Segway tours?", "What is a Trikke?",
                              "Do I need to book in advance?", "What is your cancellation policy?")])] + tour_lds)
    h = head("tours.html",
             T("t.tours"),
             T("d.tours"),
             "segway tour miami beach, art deco segway tour, ocean drive segway tour, star island segway tour, "
             "millionaires row tour miami, night tour miami beach, south beach segway tour price",
             extra, og_img="tour-segway-deco")
    cards = "".join(tour_card(t, i % 3 + 1) for i, t in enumerate(TOURS))
    opts = ""
    for t in TOURS:
        for label, price in t["options"]:
            opts += f"<tr><td><strong>{t['name']}</strong></td><td>{label}</td><td>{money(price)}</td></tr>"
    return h + nav("tours.html") + f'''
<section class="phead">
  <div class="wrap phead__in" data-reveal>
    <p class="crumbs"><a href="index.html">Home</a> · Tours</p>
    <h1 style="font-size:clamp(2.3rem,5.5vw,4.2rem)">{T("p.tours_h")}</h1>
    <p class="lead">{T("p.tours_lead")}</p>
  </div>
</section>

{answer_box(T("ab.tours_q"), T("ab.tours_a"))}

<section class="sec">
  <div class="wrap">
    <div class="chips" data-filter-group data-filter-target="#tour-grid" role="tablist">
      <button class="chip is-active" data-filter="all">All tours</button>
      <button class="chip" data-filter="segway">Segway</button>
      <button class="chip" data-filter="bike">Bike</button>
      <button class="chip" data-filter="electric">E-bike</button>
      <button class="chip" data-filter="trikke">Trikke</button>
      <button class="chip" data-filter="free">{T("u_free")}</button>
      <button class="chip" data-filter="short">Short</button>
      <button class="chip" data-filter="night">Night</button>
      <button class="chip" data-filter="private">Private</button>
    </div>
    <div class="grid grid--3" id="tour-grid">{cards}</div>
  </div>
</section>

<section class="sec band-dark">
  <div class="wrap">
    <div class="center" data-reveal>
      <span class="eyebrow eyebrow--light">Included on every tour</span>
      <h2 style="color:#fff">You bring sunscreen. We bring the rest.</h2>
    </div>
    <div class="grid grid--4" style="margin-top:3rem">
      <div class="tile" data-reveal data-delay="1"><div class="tile__ico">🎓</div><h3>Training first</h3><p>Nobody rolls out until they are comfortable. Segway riders get a full supervised practice session.</p></div>
      <div class="tile" data-reveal data-delay="2"><div class="tile__ico">🪖</div><h3>Helmet &amp; gear</h3><p>Fitted helmet, water and a radio-free small group so you can actually hear the guide.</p></div>
      <div class="tile" data-reveal data-delay="3"><div class="tile__ico">📸</div><h3>Photo stops</h3><p>Built into every route — Ocean Drive, the Star Island gate and South Pointe Pier at minimum.</p></div>
      <div class="tile" data-reveal data-delay="4"><div class="tile__ico">🗣️</div><h3>English &amp; Spanish</h3><p>Guides switch between English, Spanish and Portuguese. Private groups on request.</p></div>
    </div>
  </div>
</section>

<section class="sec band-sand">
  <div class="wrap">
    <div class="center" data-reveal><span class="eyebrow">Tour pricing</span><h2>Every departure &amp; price</h2></div>
    <div class="table-wrap" style="margin-top:2.4rem" data-reveal>
      <table>
        <caption class="sr-only">Guided tour options and prices in Miami Beach</caption>
        <thead><tr><th scope="col">Tour</th><th scope="col">Option</th><th scope="col">Price per person</th></tr></thead>
        <tbody>{opts}</tbody>
      </table>
    </div>
    <p class="note center" style="margin-top:1.2rem">Segway tours run on fixed departure times, require a minimum of two riders and must be booked ahead. No deposit is taken at booking or in store. Private and corporate groups welcome — call {BIZ['phone_pretty']}.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap"><div class="center" data-reveal><span class="eyebrow">Before you book</span><h2>Tour questions</h2></div>
  <div style="margin-top:2.4rem">{faq_block([f for f in FAQ if f[0] in ("How much are the Segway tours?", "What guided tours do you run?", "Some tours do not show a price. Why?", "How old do you have to be to ride a Segway or a Trikke?", "What is a Trikke?", "Do I need to book in advance?", "What is your cancellation policy?")])}</div></div>
</section>

{cta_section("Pick a departure and we will hold your spot",
 "Tours fill fastest between December and April and on weekends. Reserve by phone, email or at the shop.")}
''' + footer()


def page_adventures():
    adv_lds = [ld({
        "@context": "https://schema.org", "@type": "TouristTrip",
        "name": a["name"], "description": a["hook"],
        "url": SITE + "/adventures.html#" + a["slug"],
        "image": SITE + "/assets/img/" + a["img"] + ".svg",
        "touristType": "Families, couples, groups",
        "provider": {"@id": SITE + "/#business"},
        "itinerary": {"@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1,
             "item": {"@type": "TouristAttraction", "name": s}}
            for i, s in enumerate(a["stops"])]},
        "offers": offer(a["price"], SITE + "/adventures.html#" + a["slug"]),
    }) for a in ADVENTURES]
    extra = "".join([speakable(), breadcrumbs([("Home", ""), ("Adventures", "adventures.html")]),
                     faq_ld([f for f in FAQ if f[0] in
                             ("What else do you book besides bikes and Segways?",
                              "Some tours do not show a price. Why?",
                              "Do I need to book in advance?",
                              "What is your cancellation policy?")])] + adv_lds)
    h = head("adventures.html",
             T("t.adventures"),
             T("d.adventures"),
             "everglades airboat tour miami, key west day trip from miami, jet ski rental miami beach, "
             "parasailing south beach, miami helicopter tour, miami city tour",
             extra, og_img="tour-parasail")
    cards = "".join(tour_card(a, i % 3 + 1) for i, a in enumerate(ADVENTURES))
    opts = ""
    for a in ADVENTURES:
        for label, price in a["options"]:
            opts += f"<tr><td><strong>{a['name']}</strong></td><td>{label}</td><td>{money(price)}</td></tr>"
    return h + nav("adventures.html") + f'''
<section class="phead">
  <div class="wrap phead__in" data-reveal>
    <p class="crumbs"><a href="index.html">Home</a> &middot; Adventures</p>
    <h1 style="font-size:clamp(2.3rem,5.5vw,4.2rem)">{T("p.adv_h")}</h1>
    <p class="lead">{T("p.adv_lead")}</p>
  </div>
</section>

{answer_box(T("ab.adv_q"), T("ab.adv_a"))}

<section class="sec">
  <div class="wrap">
    <div class="chips" data-filter-group data-filter-target="#adv-grid" role="tablist">
      <button class="chip is-active" data-filter="all">Everything</button>
      <button class="chip" data-filter="water">On the water</button>
      <button class="chip" data-filter="nature">Nature</button>
      <button class="chip" data-filter="city">City</button>
      <button class="chip" data-filter="air">In the air</button>
      <button class="chip" data-filter="day">Day trips</button>
    </div>
    <div class="grid grid--3" id="adv-grid">{cards}</div>
  </div>
</section>

<section class="sec band-dark">
  <div class="wrap">
    <div class="center" data-reveal>
      <span class="eyebrow eyebrow--light">One counter, the whole of South Florida</span>
      <h2 style="color:#fff">Book it where you rent your bike</h2>
      <p class="lead">We have been sending people to the Everglades and the Keys for as long as we have been renting cruisers. Same shop, same phone number, same people if anything goes sideways.</p>
    </div>
    <div class="grid grid--4" style="margin-top:3rem">
      <div class="tile" data-reveal data-delay="1"><div class="tile__ico">&#128652;</div><h3>Hotel pickup</h3><p>Day trips and adventures include pickup across South Beach and Mid-Beach. Tell us the hotel, we handle the rest.</p></div>
      <div class="tile" data-reveal data-delay="2"><div class="tile__ico">&#128666;</div><h3>No deposit</h3><p>Segway PT tours require no deposit at booking or in store. Everything else is pre-paid in US dollars.</p></div>
      <div class="tile" data-reveal data-delay="3"><div class="tile__ico">&#128172;</div><h3>Three languages</h3><p>English, Spanish and Portuguese at the counter and, on most departures, with the guide too.</p></div>
      <div class="tile" data-reveal data-delay="4"><div class="tile__ico">&#128100;</div><h3>A human answers</h3><p>Between 9 AM and 8 PM, every day, {BIZ['phone_pretty']} reaches the shop. Not a call centre.</p></div>
    </div>
  </div>
</section>

<section class="sec band-sand">
  <div class="wrap">
    <div class="center" data-reveal><span class="eyebrow">Adventure pricing</span><h2>Every option &amp; price</h2></div>
    <div class="table-wrap" style="margin-top:2.4rem" data-reveal>
      <table>
        <caption class="sr-only">Adventure and day trip options and prices</caption>
        <thead><tr><th scope="col">Adventure</th><th scope="col">Option</th><th scope="col">Price per person</th></tr></thead>
        <tbody>{opts}</tbody>
      </table>
    </div>
    <p class="note center" style="margin-top:1.2rem">Departures are seasonal and weather-dependent. Named storms are always refunded or rescheduled. Call {BIZ['phone_pretty']} for today's availability.</p>
  </div>
</section>

{cta_section("Airboat in the morning, cruiser in the afternoon",
 "Book the adventure and the bike in the same conversation. We will line up the times so nothing overlaps.")}
''' + footer()


def shop_card(p, delay=0):
    meta = "".join("<span>✓ %s</span>" % m for m in p["meta"])
    lines = "".join("<li>%s</li>" % lbl for lbl, _ in p["rates"])
    return f'''
<article class="card" data-cat="{p['cat']}" data-reveal data-delay="{delay}" id="{p['slug']}">
  <div class="card__media"><span class="card__tag">{p['tag']}</span>{img(p['img'], p['name'] + ' for sale in Miami Beach')}</div>
  <div class="card__body">
    <h3>{p['name']}</h3>
    <div class="card__meta">{meta}</div>
    <p>{p['hook']}</p>
    <ul class="speclist">{lines}</ul>
    <div class="card__foot">
      {price_tag(p['price'], 'per ' + p['unit'])}
      {book_btn(p['price'], extra='btn--ocean')}
    </div>
  </div>
</article>'''


def page_shop():
    shop_ld = ld({
        "@context": "https://schema.org", "@type": "ItemList",
        "name": "Segway, Trikke and bicycle sales, parts and service in Miami Beach",
        "itemListElement": [{
            "@type": "ListItem", "position": i + 1,
            "item": {
                "@type": "Product", "name": p["name"], "description": p["hook"],
                "image": SITE + "/assets/img/" + p["img"] + ".svg",
                "url": SITE + "/shop.html#" + p["slug"],
                "brand": {"@type": "Brand", "name": "Segway" if "Segway" in p["name"] else BIZ["name"]},
                "offers": offer(p["price"], SITE + "/shop.html#" + p["slug"]),
            }} for i, p in enumerate(SHOP)]})
    dealer_ld = ld({
        "@context": "https://schema.org", "@type": "Service",
        "name": "Segway sales and service in Miami",
        "serviceType": "Authorized Segway dealership",
        "provider": {"@id": SITE + "/#business"},
        "areaServed": [{"@type": "Place", "name": a} for a in BIZ["areas"]],
        "hasOfferCatalog": {
            "@type": "OfferCatalog", "name": "Segway, Trikke and bicycle sales",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Product", "name": p["name"]}}
                for p in SHOP]},
    })
    extra = "".join([speakable(), shop_ld, dealer_ld,
                     breadcrumbs([("Home", ""), ("Shop", "shop.html")]),
                     faq_ld([f for f in FAQ if f[0] in
                             ("Do you sell Segways and Trikkes?",
                              "Do you repair bikes, e-bikes and scooters?",
                              "Can I try a Segway or Trikke before buying one?")])])
    h = head("shop.html",
             T("t.shop"),
             T("d.shop"),
             "segway dealer miami, buy segway miami, trikke for sale miami, "
             "electric bike shop miami beach, segway i2 parts, bike repair miami beach, "
             "authorized segway dealer florida",
             extra, og_img="fleet-segway")
    cards = "".join(shop_card(p, i % 3 + 1) for i, p in enumerate(SHOP))
    return h + nav("shop.html") + f'''
<section class="phead">
  <div class="wrap phead__in" data-reveal>
    <p class="crumbs"><a href="index.html">Home</a> &middot; Shop</p>
    <h1 style="font-size:clamp(2.3rem,5.5vw,4.2rem)">{T("p.shop_h")}</h1>
    <p class="lead">{T("p.shop_lead")}</p>
  </div>
</section>

{answer_box(T("ab.shop_q"), T("ab.shop_a"))}

<section class="sec">
  <div class="wrap">
    <div class="chips" data-filter-group data-filter-target="#shop-grid" role="tablist">
      <button class="chip is-active" data-filter="all">Everything</button>
      <button class="chip" data-filter="segway">Segway</button>
      <button class="chip" data-filter="trikke">Trikke</button>
      <button class="chip" data-filter="bikes">Bikes</button>
      <button class="chip" data-filter="parts">Parts</button>
      <button class="chip" data-filter="service">Service</button>
    </div>
    <div class="grid grid--3" id="shop-grid">{cards}</div>
  </div>
</section>

<section class="sec band-dark">
  <div class="wrap split">
    <div data-reveal>
      <span class="eyebrow eyebrow--light">Why buy here</span>
      <h2 style="color:#fff">Ride it for an hour before you spend a cent</h2>
      <p class="lead">Nobody should buy a Segway or a Trikke from a photograph. Rent the exact model, take it down Ocean Drive, and if you buy it we put the rental toward the purchase. We have been servicing these machines on this street since 2009 — so the warranty work happens here too, not in a box back to the factory.</p>
      <div class="badge-row">
        <span class="badge">&#9989; Factory authorized</span>
        <span class="badge">&#128295; In-house service</span>
        <span class="badge">&#128666; South Florida delivery</span>
      </div>
      <a class="btn btn--sun" style="margin-top:1.6rem" href="tel:{BIZ['phone']}">Call about a model</a>
    </div>
    <div class="split__media" data-reveal data-delay="2">{img("fleet-segway", "Segway personal transporter for sale at the Miami Beach shop")}</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="center" data-reveal><span class="eyebrow">The workshop</span><h2>We fix what we sell &mdash; and what we didn't</h2>
    <p class="lead">Walk in with a flat, a dead battery or a Segway that will not calibrate. Most jobs are done the same day.</p></div>
    <div class="grid grid--4" style="margin-top:2.8rem">
      <div class="tile" data-reveal data-delay="1"><div class="tile__ico">&#128678;</div><h3>Flats &amp; tyres</h3><p>Tubes, tyres, puncture repair and wheel truing on bikes, e-bikes and trikes.</p></div>
      <div class="tile" data-reveal data-delay="2"><div class="tile__ico">&#9881;&#65039;</div><h3>Brakes &amp; gears</h3><p>Cable and hydraulic brakes, derailleur setup, full drivetrain tune-ups.</p></div>
      <div class="tile" data-reveal data-delay="3"><div class="tile__ico">&#128267;</div><h3>Batteries</h3><p>E-bike and Segway battery diagnostics, replacement cells and charger testing.</p></div>
      <div class="tile" data-reveal data-delay="4"><div class="tile__ico">&#128736;&#65039;</div><h3>Segway service</h3><p>Authorized warranty work, calibration, tyres, and the full i2 parts range in stock.</p></div>
    </div>
  </div>
</section>

{cta_section("Tell us what you are looking for",
 "Models, availability and pricing change with the season. One phone call and we will tell you exactly what is on the floor today.",
 ("Call " + BIZ["phone_pretty"], "tel:" + BIZ["phone"]), external=False)}
''' + footer()


def page_live_route():
    """LIVE ROUTE — the virtual tour guide."""
    stops_ld = ld({
        "@context": "https://schema.org", "@type": "ItemList",
        "name": "Iconic South Beach stops on the Live Route virtual guide",
        "numberOfItems": len([p for p in POI if p["id"] != "shop"]),
        "itemListElement": [{
            "@type": "ListItem", "position": i + 1,
            "item": {
                "@type": "TouristAttraction", "name": p["name"],
                "description": p["story"],
                "address": {"@type": "PostalAddress", "streetAddress": p["addr"],
                            "addressLocality": "Miami Beach", "addressRegion": "FL",
                            "postalCode": "33139", "addressCountry": "US"},
                "geo": {"@type": "GeoCoordinates", "latitude": p["lat"], "longitude": p["lng"]},
                "hasMap": "https://www.google.com/maps/search/?api=1&query=%s,%s" % (p["lat"], p["lng"]),
            }} for i, p in enumerate(p for p in POI if p["id"] != "shop")]})

    app_ld = ld({
        "@context": "https://schema.org", "@type": "WebApplication",
        "name": "Live Route — South Beach virtual tour guide",
        "url": SITE + "/live-route.html",
        "applicationCategory": "TravelApplication",
        "operatingSystem": "Any modern web browser",
        "browserRequirements": "Requires JavaScript and, for live mode, location permission",
        "isAccessibleForFree": True,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "featureList": [
            "Choose how you travel: on foot, cruiser, electric bike, Segway, Trikke or skates",
            "Choose how long you have: 30 minutes to half a day",
            "Choose what you like: Art Deco, beach, food, photo spots, mansions, art, nature",
            "Builds an ordered route from 233 14th Street and back",
            "Live mode follows your location and announces each stop",
            "Opens the whole route in Google Maps",
        ],
        "provider": {"@id": SITE + "/#business"},
    })

    trip_ld = ld({
        "@context": "https://schema.org", "@type": "TouristTrip",
        "name": "Live Route: self-guided South Beach tour",
        "description": ("A free self-guided route from 233 14th Street, Miami Beach, through the "
                        "most iconic spots in South Beach, built around how you travel, how long "
                        "you have and what you want to see."),
        "url": SITE + "/live-route.html",
        "provider": {"@id": SITE + "/#business"},
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD",
                   "availability": "https://schema.org/InStock"},
        "itinerary": {"@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1,
             "item": {"@type": "TouristAttraction", "name": p["name"]}}
            for i, p in enumerate(p for p in POI if p["id"] != "shop")]},
    })

    extra = "".join([speakable(), app_ld, trip_ld, stops_ld,
                     breadcrumbs([("Home", ""), ("Live Route", "live-route.html")]),
                     faq_ld([f for f in FAQ if f[0] in
                             ("What is Live Route?",
                              "Do I need a bike to use Live Route?",
                              "Does Live Route cost anything?")])])

    h = head("live-route.html",
             T("t.live"),
             T("d.live"),
             "self guided tour south beach, free walking tour miami beach, "
             "south beach art deco self guided tour, miami beach audio guide, "
             "what to see in south beach, virtual tour guide miami beach",
             extra, og_img="routes-map")

    modes = "".join(
        '<button type="button" class="lr-opt%s" data-lr-mode="%s">'
        '<span class="lr-opt__ico">%s</span><span class="lr-opt__name">%s</span></button>'
        % (" is-on" if m["id"] == "cruiser" else "", m["id"], m["icon"], m["name"])
        for m in MODES)
    durs = "".join(
        '<button type="button" class="lr-opt lr-opt--sm%s" data-lr-mins="%d">%s</button>'
        % (" is-on" if d["mins"] == 120 else "", d["mins"], d["name"])
        for d in DURATIONS)
    tags = "".join(
        '<button type="button" class="lr-opt lr-opt--sm" data-lr-tag="%s">'
        '<span class="lr-opt__ico">%s</span>%s</button>' % (t, ico, label)
        for t, label, ico in INTERESTS)

    # every stop is also rendered as static HTML, so it indexes without JS
    stop_cards = "".join(f'''
<article class="lr-index__item" id="stop-{p['id']}">
  <figure class="lr-index__media">
    <img src="{poi_cover(p)}" alt="{p['name']} — {p['sub']}" width="1200" height="750" loading="lazy" decoding="async">
  </figure>
  <div class="lr-index__body">
    <h3>{p['name']}</h3>
    <p class="lr-index__sub">{p['sub']} &middot; {p['addr']}</p>
    <p>{p['story']}</p>
    <a class="lr-index__map" href="https://www.google.com/maps/search/?api=1&amp;query={p['lat']},{p['lng']}" target="_blank" rel="noopener">{T("u_openmaps")} &rarr;</a>
  </div>
</article>''' for p in POI if p["id"] != "shop")

    return h + nav("live-route.html") + f'''
<section class="phead phead--live">
  <div class="wrap phead__in" data-reveal>
    <p class="crumbs"><a href="index.html">Home</a> &middot; Live Route</p>
    <span class="lr-badge">{T("p.live_badge")}</span>
    <h1 style="font-size:clamp(2.3rem,5.5vw,4.2rem)">{T("p.live_h")}</h1>
    <p class="lead">{T("p.live_lead")}</p>
  </div>
</section>

{answer_box(T("ab.live_q"), T("ab.live_a"))}

<section class="sec" id="plan">
  <div class="wrap">
    <div class="lr-launch" data-reveal>
      <div class="lr-launch__ico" aria-hidden="true">&#128205;</div>
      <h2>Open the assistant</h2>
      <p class="lead">Three questions and it builds your route. It opens in its own window so the plan stays in one place while you ride — nothing mixed in with the rest of the site.</p>
      <div class="lr-launch__steps">
        <span><b>1</b> How you move</span>
        <span><b>2</b> How long you have</span>
        <span><b>3</b> What you like</span>
      </div>
      <button class="btn btn--block" type="button" data-assistant="lr-mode">Build my route</button>
      <p class="note" style="margin-top:.9rem">Free &middot; no app &middot; no sign-up &middot; works in any phone browser</p>
    </div>
  </div>
</section>

<section class="sec band-dark">
  <div class="wrap">
    <div class="center" data-reveal>
      <span class="eyebrow eyebrow--light">How it works</span>
      <h2 style="color:#fff">A guide in your pocket, not a group to keep up with</h2>
    </div>
    <div class="steps" style="margin-top:3rem">
      <div class="step" data-reveal data-delay="1"><h3>Pick your three</h3><p>Vehicle, time, interests. Six ways to travel, four time budgets, ten things to be into — the combinations land in the hundreds.</p></div>
      <div class="step" data-reveal data-delay="2"><h3>We order the stops</h3><p>It takes the landmarks that match, orders them by what is actually nearest, and only keeps what fits your clock — including the ride back to us.</p></div>
      <div class="step" data-reveal data-delay="3"><h3>Ride it live</h3><p>Live mode uses your phone's location to show the distance and direction to the next stop, and flips over when you arrive.</p></div>
      <div class="step" data-reveal data-delay="4"><h3>Or just open Maps</h3><p>One tap sends the whole loop to Google Maps for turn-by-turn, if you would rather have a voice in your ear.</p></div>
    </div>
  </div>
</section>

<section class="sec band-sand">
  <div class="wrap">
    <div class="center" data-reveal>
      <span class="eyebrow">Every stop on the map</span>
      <h2>{T("lr_places") % len([p for p in POI if p["id"] != "shop"])}</h2>
      <p class="lead">Written by people who ride past them every day — not scraped from a listings site.</p>
    </div>
    <div class="lr-index" style="margin-top:2.6rem">{stop_cards}</div>
  </div>
</section>

{cta_section("No bike? The route still works on foot",
 "Walking covers the deco strip fine. For South Pointe, the Venetian Islands or Wynwood you will want wheels — we are at the start line either way.")}
''' + footer()


def page_routes():
    cards = "".join(f'''
<article class="card" data-reveal data-delay="{i%3+1}">
  <div class="card__media"><span class="card__tag">{r['level']}</span>{img(route_cover(r), r['name'] + " cycling route in Miami Beach")}</div>
  <div class="card__body">
    <h3>{r['name']}</h3>
    <div class="card__meta"><span>📏 {r['km']}</span><span>⏱️ {r['time']}</span><span>📍 {r['to']}</span></div>
    <p>{r['desc']}</p>
    <p class="note"><strong>Along the way:</strong> {" · ".join(r['stops'])}</p>
    <div class="card__foot"><span class="price" style="font-size:1.05rem">From the shop<small>{r['from']}</small></span>
    <a class="btn btn--sm btn--ocean" href="rentals.html">Get a bike</a></div>
  </div>
</article>''' for i, r in enumerate(ROUTES))
    route_ld = ld({"@context": "https://schema.org", "@type": "ItemList",
                   "name": "Cycling routes in Miami Beach and South Beach",
                   "itemListElement": [{
                       "@type": "ListItem", "position": i + 1,
                       "item": {"@type": "TouristTrip", "name": r["name"], "description": r["desc"],
                                "provider": {"@id": SITE + "/#business"},
                                "itinerary": {"@type": "ItemList", "itemListElement": [
                                    {"@type": "ListItem", "position": j + 1,
                                     "item": {"@type": "TouristAttraction", "name": s}}
                                    for j, s in enumerate(r["stops"])]}}}
                       for i, r in enumerate(ROUTES)]})
    extra = "".join([speakable(), route_ld, breadcrumbs([("Home", ""), ("Routes", "routes.html")]),
                     faq_ld([f for f in FAQ if f[0] in ("Is Miami Beach safe for cycling?",)])])
    h = head("routes.html",
             T("t.routes"),
             T("d.routes"),
             "bike routes miami beach, south beach bike path, beachwalk miami beach, venetian causeway cycling, "
             "star island bike ride, best places to bike in miami",
             extra, og_img="routes-map")
    return h + nav("routes.html") + f'''
<section class="phead">
  <div class="wrap phead__in" data-reveal>
    <p class="crumbs"><a href="index.html">Home</a> · Routes</p>
    <h1 style="font-size:clamp(2.3rem,5.5vw,4.2rem)">{T("p.routes_h")}</h1>
    <p class="lead">{T("p.routes_lead")}</p>
  </div>
</section>

{answer_box(T("ab.routes_q"), T("ab.routes_a"))}

<section class="sec">
  <div class="wrap">
    <div class="center" data-reveal><span class="eyebrow">Six routes</span><h2>From a 40-minute spin to a half-day expedition</h2>
    <p class="lead">Every route starts and ends at our shop on 14th Street, so you always know how to get home.</p></div>
    <div class="grid grid--3" style="margin-top:3rem">{cards}</div>
  </div>
</section>

<section class="sec band-ocean">
  <div class="wrap split">
    <div data-reveal>
      <span class="eyebrow eyebrow--light">Local rules</span>
      <h2 style="color:#fff">Riding Miami Beach without drama</h2>
      <ul style="font-size:1.03rem;line-height:1.9;padding-left:1.1rem">
        <li>Helmets are required by Florida law for riders under 16 — we include one with every rental.</li>
        <li>Bikes are not allowed on the sand or on the wooden boardwalk section through Mid-Beach; use the paved Beachwalk.</li>
        <li>Ride with traffic, not against it. Ocean Drive and Collins both have marked lanes.</li>
        <li>Lock the frame <em>and</em> a wheel to a fixed rack. Your lock is in the basket.</li>
        <li>Afternoon storms are normal from June to September. They pass in 20 minutes — duck under an awning.</li>
        <li>Hydrate. The sun here is stronger than it feels with an ocean breeze on you.</li>
      </ul>
    </div>
    <div class="split__media" data-reveal data-delay="2">{img("tour-bike-coastal", "Cyclists on the Miami Beach Beachwalk next to the Atlantic Ocean")}</div>
  </div>
</section>

{cta_section("Pick a route. We will hand you the bike.",
 "Walk in at 233 14th Street and tell us how many hours you have — we will match the route to your legs and the day's wind.")}
''' + footer()


def page_about():
    extra = "".join([speakable(), breadcrumbs([("Home", ""), ("About", "about.html")]),
                     ld({"@context": "https://schema.org", "@type": "AboutPage",
                         "url": SITE + "/about.html", "mainEntity": {"@id": SITE + "/#business"}})])
    h = head("about.html",
             T("t.about"),
             T("d.about"),
             "miami beach bike shop, south beach bike rental company, bike repair miami beach, segway dealer miami beach",
             extra, og_img="about-shop")
    return h + nav("about.html") + f'''
<section class="phead">
  <div class="wrap phead__in" data-reveal>
    <p class="crumbs"><a href="index.html">Home</a> · About</p>
    <h1 style="font-size:clamp(2.3rem,5.5vw,4.2rem)">{T("p.about_h")}</h1>
    <p class="lead">{T("p.about_lead")}</p>
  </div>
</section>

<section class="sec">
  <div class="wrap split">
    <div data-reveal>
      <span class="eyebrow">Our story</span>
      <h2>We have been fixing and renting on 14th Street since 2009</h2>
      <p class="lead">We started with a rack of beach cruisers, a floor pump and the three-wheeled Trikke we named the place after. Today the shop runs ten kinds of wheels, six guided Segway tours, a full South Florida adventure desk and a workshop that keeps half the neighborhood&#39;s bikes, e-bikes and scooters on the road.</p>
      <p>What has not changed is the part we care about: you should be riding within ten minutes of walking in, on a bike that fits you, with someone who can tell you where to go and what to look at when you get there. Families are our favorite booking — baby seats, trailers, training wheels and kids' sizes are always in stock, and we have yet to meet a grandparent we could not get comfortable on a trike.</p>
      <div class="badge-row" style="filter:none">
        <span class="badge" style="background:var(--sand-2);border-color:var(--line);color:var(--ink)">🚻 Restroom</span>
        <span class="badge" style="background:var(--sand-2);border-color:var(--line);color:var(--ink)">📶 Free Wi-Fi</span>
        <span class="badge" style="background:var(--sand-2);border-color:var(--line);color:var(--ink)">💧 Cold water</span>
        <span class="badge" style="background:var(--sand-2);border-color:var(--line);color:var(--ink)">🛠️ Same-day repairs</span>
      </div>
    </div>
    <div class="split__media" data-reveal data-delay="2">{img("about-shop", "The Miami Beach Bikes and Tours shop on 14th Street, South Beach")}</div>
  </div>
</section>

<section class="sec band-dark">
  <div class="wrap">
    <div class="center" data-reveal><span class="eyebrow eyebrow--light">By the numbers</span><h2 style="color:#fff">Fifteen seasons on this island</h2></div>
    <div class="stats" style="margin-top:3rem">
      <div class="stat" data-reveal data-delay="1"><div class="stat__n" data-count="15" data-suffix="+">0</div><div class="stat__l">Years on 14th St</div></div>
      <div class="stat" data-reveal data-delay="2"><div class="stat__n" data-count="10">0</div><div class="stat__l">Kinds of wheels</div></div>
      <div class="stat" data-reveal data-delay="3"><div class="stat__n" data-count="131">0</div><div class="stat__l">Public reviews</div></div>
      <div class="stat" data-reveal data-delay="4"><div class="stat__n" data-count="4.8">0</div><div class="stat__l">Average rating</div></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap grid grid--3">
    <div class="tile" data-reveal data-delay="1"><div class="tile__ico">🛠️</div><h3>The workshop</h3><p>Flats, brakes, gears, wheel truing, battery diagnostics and full tune-ups — for our fleet and for yours. Walk in with a problem, ride out the same day.</p></div>
    <div class="tile" data-reveal data-delay="2"><div class="tile__ico">🛴</div><h3>Segway dealer</h3><p>Authorized Segway sales and service in Miami Beach, plus the only guided Segway tours that start this close to Ocean Drive.</p></div>
    <div class="tile" data-reveal data-delay="3"><div class="tile__ico">🏨</div><h3>Adventure desk</h3><p>Everglades airboats, Key West day trips, Miami city tours, jet skis, parasailing and helicopter rides — booked at the same counter, most with hotel pickup.</p></div>
  </div>
</section>

{reviews_section()}
{cta_section("Come say hi at 233 14th Street",
 "Open every day, 9 AM to 8 PM. No appointment needed — for anything except the Segway tours.",
 ("Get directions", "contact.html#find-us"), external=False)}
''' + footer()


def page_faq():
    extra = "".join([speakable(), faq_ld(FAQ), breadcrumbs([("Home", ""), ("FAQ", "faq.html")])])
    h = head("faq.html",
             T("t.faq"),
             T("d.faq"),
             "miami beach bike rental faq, bike rental policy, segway age requirement, "
             "bike delivery miami beach, cancellation policy bike rental",
             extra)
    return h + nav("faq.html") + f'''
<section class="phead">
  <div class="wrap phead__in" data-reveal>
    <p class="crumbs"><a href="index.html">Home</a> · FAQ</p>
    <h1 style="font-size:clamp(2.3rem,5.5vw,4.2rem)">{T("p.faq_h")}</h1>
    <p class="lead">{T("p.faq_lead")}</p>
  </div>
</section>

<section class="sec">
  <div class="wrap">{faq_block(FAQ)}</div>
</section>

<section class="sec band-sand">
  <div class="wrap">
    <div class="center" data-reveal><span class="eyebrow">Policies at a glance</span><h2>Cancellations &amp; refunds</h2></div>
    <div class="table-wrap" style="margin-top:2.4rem;max-width:760px;margin-inline:auto" data-reveal>
      <table>
        <caption class="sr-only">Cancellation refund schedule</caption>
        <thead><tr><th scope="col">You cancel</th><th scope="col">You get back</th></tr></thead>
        <tbody>
          <tr><td><strong>30+ days before</strong></td><td>100% refund</td></tr>
          <tr><td><strong>15–30 days before</strong></td><td>50% refund</td></tr>
          <tr><td><strong>8–14 days before</strong></td><td>25% refund</td></tr>
          <tr><td><strong>0–7 days before</strong></td><td>Non-refundable</td></tr>
        </tbody>
      </table>
    </div>
    <p class="note center" style="margin-top:1.2rem">All reservations are pre-paid in full, in US dollars. Named storms and shop-side cancellations are always fully refunded or rescheduled.</p>
  </div>
</section>

{cta_section("Still not sure which ride is right?",
 "Tell us who is riding, how long you have and what you want to see. We will pick it for you in one phone call.")}
''' + footer()


def page_contact():
    extra = "".join([speakable(), breadcrumbs([("Home", ""), ("Contact", "contact.html")]),
                     ld({"@context": "https://schema.org", "@type": "ContactPage",
                         "url": SITE + "/contact.html", "mainEntity": {"@id": SITE + "/#business"}})])
    h = head("contact.html",
             T("t.contact"),
             T("d.contact"),
             "book bike rental miami beach, contact miami beach bike rental, 233 14th street miami beach, "
             "bike delivery south beach hotel",
             extra, og_img="delivery")
    maps = "https://www.google.com/maps?q=%s,%s&output=embed" % (BIZ["lat"], BIZ["lng"])
    return h + nav("contact.html") + f'''
<section class="phead">
  <div class="wrap phead__in" data-reveal>
    <p class="crumbs"><a href="index.html">Home</a> · Contact</p>
    <h1 style="font-size:clamp(2.3rem,5.5vw,4.2rem)">{T("p.contact_h")}</h1>
    <p class="lead">{T("p.contact_lead")}</p>
  </div>
</section>

<section class="sec" id="book">
  <div class="wrap split">
    <div data-reveal>
      <span class="eyebrow">Reserve</span>
      <h2>Tell us what you need</h2>
      <p class="lead">Send this and we reply within the hour during shop hours. For same-day rentals, just call — or book instantly online.</p>
      <div class="btn-row" style="margin-bottom:1.6rem">
        <a class="btn btn--ocean" href="{BOOKING_URL}" target="_blank" rel="noopener">Book online now</a>
        <a class="btn btn--ghost" style="border-color:var(--line);color:var(--ink)" href="tel:{BIZ['phone']}">Call {BIZ['phone_pretty']}</a>
      </div>
      <form class="stack-sm" style="margin-top:1.6rem" action="mailto:{BIZ['email']}" method="post" enctype="text/plain">
        <div class="finder__field"><label for="c-name">Your name</label><input id="c-name" name="name" required autocomplete="name"></div>
        <div class="finder__field"><label for="c-email">Email</label><input id="c-email" name="email" type="email" required autocomplete="email"></div>
        <div class="finder__field"><label for="c-phone">Phone / WhatsApp</label><input id="c-phone" name="phone" type="tel" autocomplete="tel"></div>
        <div class="finder__field"><label for="c-what">What do you want</label>
          <select id="c-what" name="service">
            <option>Bike rental</option><option>Fat tire bike rental</option><option>Electric bike rental</option>
            <option>Electric tandem</option><option>Trikke rental</option><option>Side-by-side bike</option>
            <option>Adult tricycle</option><option>Rollerblades</option><option>Kids / family package</option>
            <option>Segway tour</option><option>Private night tour</option>
            <option>Everglades airboat adventure</option><option>Key West day trip</option>
            <option>Miami city tour</option><option>Jet ski</option><option>Parasailing</option>
            <option>Helicopter ride</option><option>Repair / tune-up</option><option>Segway sales &amp; service</option>
            <option>Hotel delivery</option><option>Group or corporate booking</option>
          </select></div>
        <div class="finder__field"><label for="c-date">Date</label><input id="c-date" name="date" type="date"></div>
        <div class="finder__field"><label for="c-riders">How many riders</label><input id="c-riders" name="riders" type="number" min="1" value="2"></div>
        <div class="finder__field"><label for="c-hotel">Hotel / address for delivery (optional)</label><input id="c-hotel" name="hotel"></div>
        <div class="finder__field"><label for="c-msg">Anything else</label><input id="c-msg" name="message"></div>
        <button class="btn btn--block" type="submit" style="margin-top:.8rem">Send booking request</button>
        <p class="note">Or skip the form: <a href="tel:{BIZ['phone']}"><strong>{BIZ['phone_pretty']}</strong></a> · <a href="mailto:{BIZ['email']}">{BIZ['email']}</a></p>
      </form>
    </div>
    <div data-reveal data-delay="2">
      <div class="grid" style="gap:1rem">
        <div class="tile"><div class="tile__ico">📍</div><h3>Walk in</h3><p>{BIZ['street']}<br>{BIZ['city']}, {BIZ['region']} {BIZ['zip']}<br>One block west of Ocean Drive, in the heart of South Beach.</p></div>
        <div class="tile"><div class="tile__ico">🕘</div><h3>Hours</h3><p>{BIZ['hours_pretty']}<br><span data-open-status style="font-weight:700"></span><br><span class="note">Happy hour 1–4 PM: +1 free hour</span></p></div>
        <div class="tile"><div class="tile__ico">📞</div><h3>Call or write</h3><p><a href="tel:{BIZ['phone']}"><strong>{BIZ['phone_pretty']}</strong></a><br><a href="mailto:{BIZ['email']}">{BIZ['email']}</a><br>English · Español · Português</p></div>
        <div class="tile"><div class="tile__ico">🏨</div><h3>Delivery zone</h3><p>Free across South Beach on 24h+ rentals. Mid-Beach, North Beach, Downtown, Brickell and Key Biscayne by flat fee.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="sec--tight" id="find-us">
  <div class="wrap" data-reveal>
    <div style="border-radius:var(--r-xl);overflow:hidden;box-shadow:var(--shadow-m)">
      <iframe title="Map to Miami Beach Bikes, 233 14th Street, Miami Beach, FL 33139"
        src="{maps}" width="100%" height="460" style="border:0;display:block" loading="lazy"
        referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
    </div>
  </div>
</section>

{cta_section("Same-day rental? Just call.",
 "We keep walk-in bikes on the rack all day, every day. Ten minutes from hello to riding.",
 ("Call " + BIZ["phone_pretty"], "tel:" + BIZ["phone"]), external=False)}
''' + footer()


def page_404():
    h = head("404.html", T("t.404"),
             T("d.404"),
             "404")
    # a 404 must not be indexed — replace the site-wide robots directive
    h = h.replace('<meta name="robots" content="index,follow,max-image-preview:large,'
                  'max-snippet:-1,max-video-preview:-1">',
                  '<meta name="robots" content="noindex,follow">')
    return h + nav("") + f'''
<section class="phead" style="min-height:52vh;display:grid;place-items:center">
  <div class="wrap phead__in center">
    <h1>{T("p.404_h")}</h1>
    <p class="lead" style="margin-inline:auto">{T("p.404_lead")}</p>
    <div class="btn-row btn-row--center" style="margin-top:1.6rem">
      <a class="btn" href="index.html">{T("p.404_home")}</a>
      <a class="btn btn--ghost" href="rentals.html">{T("p.404_rent")}</a>
    </div>
  </div>
</section>
''' + footer()


# ---------------------------------------------------------------- non-HTML
def build_sitemap():
    pages = [("index.html", "1.0", "weekly"), ("rentals.html", "0.9", "weekly"),
             ("tours.html", "0.9", "weekly"), ("adventures.html", "0.9", "weekly"),
             ("live-route.html", "0.9", "monthly"),
             ("shop.html", "0.8", "monthly"),
             ("routes.html", "0.8", "monthly"),
             ("about.html", "0.6", "monthly"), ("faq.html", "0.7", "monthly"),
             ("contact.html", "0.8", "monthly")]
    import datetime
    today = datetime.date.today().isoformat()
    urls = "".join(
        f"\n  <url><loc>{SITE}/{p}</loc><lastmod>{today}</lastmod>"
        f"<changefreq>{cf}</changefreq><priority>{pr}</priority></url>" for p, pr, cf in pages)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}\n</urlset>\n'


def build_robots():
    return f"""# Miami Beach Bikes · Rentals & Tours
User-agent: *
Allow: /

# Answer engines & LLM crawlers — explicitly welcome
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-User
Allow: /
User-agent: anthropic-ai
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Perplexity-User
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: Applebot-Extended
Allow: /
User-agent: Bingbot
Allow: /
User-agent: Amazonbot
Allow: /
User-agent: CCBot
Allow: /
User-agent: meta-externalagent
Allow: /

Sitemap: {SITE}/sitemap.xml
"""


def build_llms():
    def pr(v, suffix=""):
        return "Price on request \u2014 call %s." % BIZ["phone"] if v is None else "From $%s%s." % (v, suffix)
    fleet = "\n".join("- **%s** — %s From $%s/%s." % (p["name"], p["hook"], p["price"], p["unit"]) for p in FLEET)
    tours = "\n".join("- **%s** (%s, from $%s) — %s Stops: %s." %
                      (t["name"], t["dur_pretty"], t["price"], t["hook"], ", ".join(t["stops"])) for t in TOURS)
    advs = "\n".join("- **%s** (%s) \u2014 %s %s Includes: %s." %
                     (a["name"], a["dur_pretty"], a["hook"], pr(a["price"], " per person"),
                      ", ".join(a["stops"])) for a in ADVENTURES)
    shop = "\n".join("- **%s** \u2014 %s %s Options: %s." %
                     (p["name"], p["hook"], pr(p["price"]),
                      ", ".join(lbl for lbl, _ in p["rates"])) for p in SHOP)
    poi_names = ", ".join(p["name"] for p in POI if p["id"] != "shop")
    routes = "\n".join("- **%s** (%s, %s, %s): %s" % (r["name"], r["km"], r["time"], r["level"], r["desc"]) for r in ROUTES)
    faq = "\n\n".join("**Q: %s**\nA: %s" % (q, a) for q, a in FAQ)
    return f"""# {BIZ['name']}

> Bicycle, fat tire, electric bike, electric tandem, Trikke, Segway, side-by-side, tricycle and rollerblade rentals,
> guided Segway tours, and South Florida adventures (Everglades airboats, Key West day trips, Miami city tours,
> jet skis, parasailing, helicopter rides) in South Beach, Miami Beach, Florida.
> Shop at {BIZ['street']}, {BIZ['city']}, {BIZ['region']} {BIZ['zip']} — one block from Ocean Drive.
> Open every day 9:00 AM – 8:00 PM. Phone {BIZ['phone']}.
> Rentals from $12/hour, Segway tours from $49/person, Everglades airboat adventure $69/person.
> Also Miami's factory authorized Segway dealer: sales, genuine parts and same-day service.
> Items without a published price are quoted by phone at {BIZ['phone']}.

## Facts for citation
- Business type: bicycle rental shop, tour operator and repair workshop.
- Address: {BIZ['street']}, {BIZ['city']}, {BIZ['region']} {BIZ['zip']}, USA.
- Coordinates: {BIZ['lat']}, {BIZ['lng']}.
- Phone: {BIZ['phone']} · Email: {BIZ['email']}
- Hours: {BIZ['hours_pretty']} (open 7 days, including holidays).
- Languages: English, Spanish, Portuguese.
- Rating: 4.8 / 5 from 131 public reviews.
- Rental durations: 1 hour to 60 days. All-day rentals run 9 AM to 8 PM.
- Happy hour: rent between 1 PM and 4 PM and get one extra hour free.
- Tours: minimum 2 riders per Segway tour; training always included; no deposit taken for Segway PT tours.
- Minimum age: 14 for Segway and Trikke; under 18 must be accompanied by an adult.
- Included with every rental: helmet, lock, bottled water, printed route map, phone support while riding.
- Delivery: free across South Beach on rentals of 24 hours or more; flat fee to Mid-Beach, North Beach, Downtown Miami, Brickell and Key Biscayne.
- Areas served: {", ".join(BIZ['areas'])}.
- On-site services: flat repair, brakes, gears, battery diagnostics, full tune-ups for bikes, e-bikes and scooters.
- Miami's factory authorized Segway dealer: new Segways, electric and pedal Trikkes, electric bikes, bicycles and the full Segway i2 parts range (lower cargo frames, reflective shields, integrated lighting, patroller bag, front bumper, comfort mats, accessory bar).
- Test ride before buying; the rental fee goes toward the purchase.
- Free guided bike tours of Wynwood and Coconut Grove for anyone who rents.
- Luggage storage at the shop while you ride; restroom and free Wi-Fi on site.
- Also books: Everglades airboat adventures, Key West day trips, Miami city tours, jet ski rentals, parasailing, helicopter rides.
- Payment: cash, credit and debit cards, Apple Pay, Google Pay. Reservations pre-paid in USD.
- Cancellation: 30+ days 100% refund · 15–30 days 50% · 8–14 days 25% · 0–7 days non-refundable.

## Rentals ({SITE}/rentals.html)
{fleet}

## Guided tours ({SITE}/tours.html)
{tours}

## Adventures and day trips ({SITE}/adventures.html)
{advs}

## Sales, parts and service ({SITE}/shop.html)
{shop}

## Cycling routes from the shop ({SITE}/routes.html)
{routes}

## Frequently asked questions ({SITE}/faq.html)
{faq}

## Live Route — free self-guided tour ({SITE}/live-route.html)
A free virtual tour guide on the website (no app, no sign-up). The visitor picks how they travel
(on foot, beach cruiser, electric bike, Segway, Trikke, skates or longboard), how long they have
(30 minutes, 1 hour, 2 hours or half a day) and what they are interested in (Art Deco, beach,
photo spots, food, mansions and fame, art and museums, family, neon after dark, parks, shopping).
It then orders the nearest matching landmarks into a loop starting and ending at 233 14th Street,
gives distance and riding time for each leg, and in live mode uses the phone's location to show
the distance and compass direction to the next stop, advancing automatically on arrival.
The whole route can be opened in Google Maps in one tap.
Landmarks covered: {poi_names}.

## The assistant — extend a rental from your phone ({SITE}/#assistant)
Every page carries an assistant that opens in its own panel. Two tools:
1. Live Route, the free self-guided tour builder described above.
2. Extend my rental: the customer enters the ticket number from their receipt (format MBB-1234),
   sees what they rented and when it is due back, picks +1 hour, +2 hours, +4 hours, +1 day or
   +1 week at the published rate for that vehicle multiplied by the number of units, and pays with
   Apple Pay, Google Pay, card or PayPal. The return time moves automatically; no return trip to
   the shop is needed. A rental that is already overdue can still be extended, and the extension
   covers the time from the original return time, so there is no late fee on top.

## Pages
- [Home]({SITE}/index.html): overview, fleet, tours, adventures, routes, reviews.
- [Rentals]({SITE}/rentals.html): all ten vehicles with hourly, all-day and weekly prices.
- [Tours]({SITE}/tours.html): six guided Segway and night tours with durations, stops and prices.
- [Adventures]({SITE}/adventures.html): Everglades, Key West, Miami city tour, jet ski, parasailing, helicopter.
- [Shop]({SITE}/shop.html): Segway and Trikke sales, e-bikes, Segway i2 parts, repairs and service.
- [Live Route]({SITE}/live-route.html): free self-guided tour builder with live navigation.
- [Routes]({SITE}/routes.html): six free cycling route guides with distance and difficulty.
- [About]({SITE}/about.html): the shop, the workshop, the team.
- [FAQ]({SITE}/faq.html): prices, delivery, ages, safety, cancellations.
- [Contact]({SITE}/contact.html): booking form, map, hours, delivery zone.
"""


# ---------------------------------------------------------------- run
PAGES = [
    ("index.html", lambda: page_index()),
    ("rentals.html", lambda: page_rentals()),
    ("tours.html", lambda: page_tours()),
    ("adventures.html", lambda: page_adventures()),
    ("live-route.html", lambda: page_live_route()),
    ("shop.html", lambda: page_shop()),
    ("routes.html", lambda: page_routes()),
    ("about.html", lambda: page_about()),
    ("faq.html", lambda: page_faq()),
    ("contact.html", lambda: page_contact()),
    ("404.html", lambda: page_404()),
]


def build_sitemap_all():
    import datetime
    today = datetime.date.today().isoformat()
    pri = {"index.html": "1.0", "rentals.html": "0.9", "tours.html": "0.9",
           "adventures.html": "0.9", "live-route.html": "0.9", "shop.html": "0.8",
           "routes.html": "0.8", "faq.html": "0.7", "contact.html": "0.8",
           "about.html": "0.6"}
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
           'xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for page, _ in PAGES:
        if page == "404.html":
            continue
        for lg in LANGS:
            alts = "".join(
                '\n    <xhtml:link rel="alternate" hreflang="%s" href="%s/%s%s"/>' % (
                    a["code"], SITE, a["dir"], page) for a in LANGS)
            out.append(
                '  <url>\n    <loc>%s/%s%s</loc>\n    <lastmod>%s</lastmod>'
                '\n    <changefreq>weekly</changefreq>\n    <priority>%s</priority>%s\n  </url>'
                % (SITE, lg["dir"], page, today, pri.get(page, "0.7"), alts))
    out.append("</urlset>")
    return "\n".join(out) + "\n"


import t_copy as _copy

_COPY_HIT = set()


def localise_html(html, lang):
    """Swap the page copy that lives inside the templates.

    Longest first, so a heading never gets eaten by a shorter phrase that
    happens to sit inside it. Every key that matches is recorded, and the
    build prints the ones that never did — a reworded template shows up as a
    stale entry rather than quietly reverting to English.
    """
    if lang == "en":
        return html
    for en in sorted(_copy.COPY, key=len, reverse=True):
        for variant in (en, _entify(en), _entify(en).replace("'", "&#39;")):
            if variant in html:
                html = html.replace(variant, _entify(_copy.COPY[en][lang]))
                _COPY_HIT.add(en)
                break
    return html


# the templates write typography as named entities, so a key has to be
# matched in both spellings
_ENTS = (("\u2014", "&mdash;"), ("\u2013", "&ndash;"), ("\u00b7", "&middot;"),
         ("\u00f1", "&ntilde;"), ("\u00e9", "&eacute;"), ("\u00e1", "&aacute;"),
         ("\u00ed", "&iacute;"), ("\u00f3", "&oacute;"), ("\u00fa", "&uacute;"))


def _entify(t):
    for ch, ent in _ENTS:
        t = t.replace(ch, ent)
    return t


if __name__ == "__main__":
    import builtins
    print("Building Miami Beach Bikes in %d languages..." % len(LANGS))
    for lg in LANGS:
        use_language(lg["code"])
        outdir = os.path.join(ROOT, lg["dir"]) if lg["dir"] else ROOT
        os.makedirs(outdir, exist_ok=True)
        print(" [%s] -> %s" % (lg["short"], lg["dir"] or "/"))
        for page, fn in PAGES:
            html = localise_html(fn(), lg["code"])
            open(os.path.join(outdir, page), "w", encoding="utf-8").write(html)
        if lg["dir"]:
            write(lg["dir"] + "llms.txt", build_llms())
    write("sitemap.xml", build_sitemap_all())
    write("robots.txt", build_robots())
    write("llms.txt", build_llms())
    stale = sorted(set(_copy.COPY) - _COPY_HIT)
    if stale:
        print("  !! %d copy keys never matched the templates:" % len(stale))
        for k in stale[:12]:
            print("     %s" % k[:96])
    print("Done.")
