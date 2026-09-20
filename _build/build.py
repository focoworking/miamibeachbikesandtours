# -*- coding: utf-8 -*-
"""Builds every static page from data.py + shell.py. Run: python3 _build/build.py"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import BIZ, SITE, BOOKING_URL, FLEET, TOURS, ADVENTURES, ROUTES, FAQ, REVIEWS
import shell
from shell import head, nav, footer, ld, breadcrumbs, ADDRESS_LD

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
        return ('<span class="price price--ask">Price on request'
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
      {price_tag(t['price'], ('from · ' if t['price'] else '') + t['dur_pretty'])}
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
HOME_FAQ_KEYS = [
    "Where can I rent a bike in South Beach?",
    "How much does it cost to rent a bike in Miami Beach?",
    "How much are the Segway tours?",
    "What is the happy hour special?",
    "What guided tours do you run?",
    "What else do you book besides bikes and Segways?",
]
HOME_FAQ = [f for f in FAQ if f[0] in HOME_FAQ_KEYS]


def page_index():
    extra = "".join([
        speakable(),
        faq_ld(HOME_FAQ),
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
             "Miami Beach Bikes | Bike, E-Bike & Segway Rentals and Tours · South Beach",
             "Rent bikes, e-bikes, Segways, rollerblades and trikes in South Beach from $12/hour. "
             "Guided Art Deco and Ocean Drive tours, free hotel delivery, open daily 9 AM – 8 PM at 233 14th Street.",
             "miami beach bike rental, south beach bike rental, segway tour miami, electric bike rental miami beach, "
             "rollerblade rental south beach, miami beach bike tours, ocean drive bike rental",
             extra)
    fleet = "".join(fleet_card(p, i % 4 + 1) for i in range(len(FLEET)) for p in [FLEET[i]])
    tours = "".join(tour_card(t, i % 3 + 1) for i, t in enumerate(TOURS[:3]))
    adventures = "".join(tour_card(a, i % 3 + 1) for i, a in enumerate(ADVENTURES[:3]))
    routes = "".join(f'''
<article class="tile" data-reveal data-delay="{i%3+1}">
  <div class="tile__ico">🗺️</div>
  <h3>{r['name']}</h3>
  <div class="card__meta"><span>{r['km']}</span><span>{r['time']}</span><span>{r['level']}</span></div>
  <p>{r['desc']}</p>
</article>''' for i, r in enumerate(ROUTES[:3]))

    return h + nav("index.html") + f'''
<section class="hero">
  <div class="hero__media">{img("hero-southbeach", "Sunset over the palm trees and Art Deco skyline of South Beach, Miami Beach")}</div>
  <div class="hero__scrim"></div>
  <div class="wrap hero__in">
    <span class="eyebrow eyebrow--light">South Beach · 233 14th Street</span>
    <h1>Ride more.<br><em>Worry less.</em></h1>
    <p class="hero__sub">Bikes, e-bikes, Trikkes, Segways and skates one block from Ocean Drive — plus <span class="hero__sub--long">Segway tours of the Art Deco District and Star Island, Everglades airboats, Key West day trips, jet skis and parasailing. Family-friendly, sun-powered, unreasonably fun.</span><span class="hero__sub--short">guided tours, Everglades airboats and Key West day trips.</span></p>
    <div class="hero__cta">
      <a class="btn" href="rentals.html">Rent a ride · from $12</a>
      <a class="btn btn--ghost" href="tours.html">See the tours</a>
    </div>
    <div class="badge-row">
      <span class="badge">★ 4.8 · 131 reviews</span>
      <span class="badge">🚲 Helmet, lock &amp; water included</span>
      <span class="badge">🏨 Free hotel delivery 24h+</span>
      <span class="badge">⏰ Happy hour 1–4 PM · +1 free hour</span>
    </div>
  </div>
  <span class="hero__scroll">Scroll</span>
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

{marquee()}

{answer_box("Where can I rent a bike in South Beach?",
 "At Miami Beach Bikes · Rentals &amp; Tours, 233 14th Street, Miami Beach, FL 33139 — one block from Ocean Drive and the Beachwalk. "
 "We are open every day from 9 AM to 8 PM, rent by the hour, day, week or month from $12/hour, run a happy hour from 1 to 4 PM that adds a free extra hour, and deliver free to South Beach hotels on rentals of 24 hours or more. Call " + BIZ["phone_pretty"] + ".")}

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

{reviews_section()}

<section class="sec">
  <div class="wrap">
    <div class="center" data-reveal>
      <span class="eyebrow">Good to know</span>
      <h2>Questions, answered</h2>
    </div>
    <div style="margin-top:2.6rem">{faq_block(HOME_FAQ)}</div>
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
             "Rentals | Bikes, E-Bikes, Trikkes, Segways & Skates in South Beach from $12/hr",
             "Full price list for beach cruiser, fat tire, electric bike, electric tandem, Trikke, side-by-side, tricycle, "
             "rollerblade and kids' bike rentals in South Beach. Hourly, all-day and weekly rates, happy hour 1-4 PM, "
             "helmet and lock included, free South Beach hotel delivery.",
             "bike rental miami beach prices, fat tire bike rental south beach, electric bike rental south beach, "
             "trikke rental miami, electric tandem rental miami beach, side by side bike rental, "
             "rollerblade rental miami beach, kids bike rental miami beach",
             extra, og_img="fleet-cruiser")
    cards = "".join(fleet_card(p, i % 3 + 1) for i, p in enumerate(FLEET))
    return h + nav("rentals.html") + f'''
<section class="phead">
  <div class="wrap phead__in" data-reveal>
    <p class="crumbs"><a href="index.html">Home</a> · Rentals</p>
    <h1 style="font-size:clamp(2.3rem,5.5vw,4.2rem)">Rentals</h1>
    <p class="lead">Ten kinds of wheels, from one hour to sixty days. Helmet, lock, cold water and a route map come with every single one — and an extra free hour if you start between 1 and 4 PM.</p>
  </div>
</section>

{answer_box("How much does it cost to rent a bike in Miami Beach?",
 "Beach cruisers start at $12 per hour and $28 for all day (9 AM to 8 PM). Fat tire beach bikes start at $18/hour, "
 "electric bikes at $25/hour, electric tandems at $45/hour, Trikkes at $25 for 30 minutes, adult tricycles at $18/hour, "
 "tandems at $22/hour, rollerblades at $12/hour and kids&#39; bikes at $10/hour. Rent between 1 PM and 4 PM and you get "
 "an extra hour free. Helmet, lock, bottled water and a route map are included with every rental.")}

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
    <div class="tile" data-reveal data-delay="4"><div class="tile__ico">📞</div><h3>Support on the road</h3><p>Flat tire on the causeway? Call us. We answer while you ride and we come out for you.</p></div>
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
             "Tours | Segway, Bike, E-Bike & Trikke Guided Tours in Miami Beach",
             "Guided Segway tours of Ocean Drive ($49), Star Island ($69), South Beach and the Art Deco District ($79) and "
             "Millionaire's Row ($89), plus private night tours. One to 2.5 hours, training included, minimum two riders.",
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
    <h1 style="font-size:clamp(2.3rem,5.5vw,4.2rem)">Guided tours</h1>
    <p class="lead">Twelve guided rides: Segway, bike, e-bike and Trikke, one hour to a full afternoon, from $49. Training always included, and a private version of any of them.</p>
  </div>
</section>

{answer_box("What is the best guided tour in South Beach?",
 "Start with the one-hour Ocean Drive Segway Tour at $49 per person — the shortest, the cheapest, training included. "
 "The Star Island Segway Tour is $69 for an hour, the two-hour South Beach and Art Deco Segway Tours are $79 each, and the "
 "2.5-hour Miami Millionaire&#39;s Row Segway Tour is $89. Bike, e-bike, Trikke, night and private tours are quoted by phone. "
 "All tours leave from 233 14th Street, Miami Beach, and Segway tours need a minimum of two riders.")}

<section class="sec">
  <div class="wrap">
    <div class="chips" data-filter-group data-filter-target="#tour-grid" role="tablist">
      <button class="chip is-active" data-filter="all">All tours</button>
      <button class="chip" data-filter="segway">Segway</button>
      <button class="chip" data-filter="bike">Bike</button>
      <button class="chip" data-filter="electric">E-bike</button>
      <button class="chip" data-filter="trikke">Trikke</button>
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
             "Everglades Airboats, Key West Day Trips, Jet Ski & Parasailing | Miami Beach",
             "Book Everglades airboat adventures from $69, Key West day trips, Miami city tours, jet ski rentals, "
             "South Beach parasailing and helicopter rides — all from our shop at 233 14th Street, South Beach. "
             "Most include hotel pickup.",
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
    <h1 style="font-size:clamp(2.3rem,5.5vw,4.2rem)">Adventures &amp; day trips</h1>
    <p class="lead">Everything that does not fit on two wheels: airboats through the sawgrass, the Overseas Highway to Key West, jet skis on the bay, 600 feet of parasail and the city from a helicopter.</p>
  </div>
</section>

{answer_box("What day trips can you book from South Beach?",
 "From our shop at 233 14th Street you can book the Everglades Airboat Adventure (4.5 hours, $69 per person, hotel pickup included), "
 "a full-day Key West trip over the Seven Mile Bridge, a half-day Miami City Tour through Little Havana and Wynwood, "
 "jet ski rentals on Biscayne Bay from $99, South Beach parasailing from $95 and helicopter rides over the city from $149. "
 "Call " + BIZ["phone_pretty"] + " to check the next departure.")}

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


def page_routes():
    cards = "".join(f'''
<article class="card" data-reveal data-delay="{i%3+1}">
  <div class="card__media"><span class="card__tag">{r['level']}</span>{img("routes-map", r['name'] + " cycling route in Miami Beach")}</div>
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
             "Best Bike Routes in Miami Beach & South Beach | Free Route Guide",
             "Six tried-and-tested cycling routes from South Beach: the Beachwalk, the Art Deco neon loop, Star Island, "
             "the Venetian Islands, Wynwood and North Beach. Distances, times, difficulty and what to see along the way.",
             "bike routes miami beach, south beach bike path, beachwalk miami beach, venetian causeway cycling, "
             "star island bike ride, best places to bike in miami",
             extra, og_img="routes-map")
    return h + nav("routes.html") + f'''
<section class="phead">
  <div class="wrap phead__in" data-reveal>
    <p class="crumbs"><a href="index.html">Home</a> · Routes</p>
    <h1 style="font-size:clamp(2.3rem,5.5vw,4.2rem)">Where to ride</h1>
    <p class="lead">Free route guides written by people who ride this island every day. Print them, screenshot them, or grab the paper version at the shop.</p>
  </div>
</section>

{answer_box("Where is the best place to bike in Miami Beach?",
 "The Miami Beach Beachwalk — a flat, paved, car-free path running along the sand from South Pointe Park to North Beach — is the best ride on the island for all ages. "
 "For skyline views, cross the Venetian Causeway to the Venetian Islands; for mansions, take the protected path on the MacArthur Causeway to Star Island; "
 "and for street art, ride an e-bike to Wynwood. All four start within a block of 233 14th Street.")}

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
             "About Miami Beach Bikes | South Beach Bike Shop, Segway Dealer & Tour Operator",
             "A family-run bike shop, Segway dealer and tour operator at 233 14th Street, South Beach. Rentals, guided Segway "
             "tours, Everglades and Key West day trips, and a full repair workshop. Open every day, 9 AM to 8 PM.",
             "miami beach bike shop, south beach bike rental company, bike repair miami beach, segway dealer miami beach",
             extra, og_img="about-shop")
    return h + nav("about.html") + f'''
<section class="phead">
  <div class="wrap phead__in" data-reveal>
    <p class="crumbs"><a href="index.html">Home</a> · About</p>
    <h1 style="font-size:clamp(2.3rem,5.5vw,4.2rem)">A shop, not a kiosk</h1>
    <p class="lead">Real mechanics, real guides, a restroom, cold water and Wi-Fi — one block from Ocean Drive.</p>
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
             "FAQ | Bike Rental & Tours in Miami Beach — Prices, Delivery, Policies",
             "Answers on bike rental prices in Miami Beach, hotel delivery, minimum ages, Segway tour rules, "
             "rental durations, what is included, cycling safety and our cancellation policy.",
             "miami beach bike rental faq, bike rental policy, segway age requirement, "
             "bike delivery miami beach, cancellation policy bike rental",
             extra)
    return h + nav("faq.html") + f'''
<section class="phead">
  <div class="wrap phead__in" data-reveal>
    <p class="crumbs"><a href="index.html">Home</a> · FAQ</p>
    <h1 style="font-size:clamp(2.3rem,5.5vw,4.2rem)">Frequently asked</h1>
    <p class="lead">Short answers first. If yours is not here, call {BIZ['phone_pretty']} — a human picks up between 9 AM and 8 PM.</p>
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
             "Contact & Booking | Miami Beach Bikes, 233 14th Street South Beach",
             "Book a bike, e-bike, Trikke, Segway tour, Everglades airboat, Key West day trip, jet ski or parasailing in "
             "South Beach. Call (305) 830-9440 or walk in at 233 14th Street, Miami Beach, FL 33139. Open daily 9 AM – 8 PM.",
             "book bike rental miami beach, contact miami beach bike rental, 233 14th street miami beach, "
             "bike delivery south beach hotel",
             extra, og_img="delivery")
    maps = "https://www.google.com/maps?q=%s,%s&output=embed" % (BIZ["lat"], BIZ["lng"])
    return h + nav("contact.html") + f'''
<section class="phead">
  <div class="wrap phead__in" data-reveal>
    <p class="crumbs"><a href="index.html">Home</a> · Contact</p>
    <h1 style="font-size:clamp(2.3rem,5.5vw,4.2rem)">Book your ride</h1>
    <p class="lead">Fastest way is the phone. Second fastest is walking in — we are one block off Ocean Drive.</p>
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
    h = head("404.html", "Page not found | Miami Beach Bikes",
             "That page took a wrong turn on Ocean Drive. Head back to rentals, tours or routes.",
             "404")
    # a 404 must not be indexed — replace the site-wide robots directive
    h = h.replace('<meta name="robots" content="index,follow,max-image-preview:large,'
                  'max-snippet:-1,max-video-preview:-1">',
                  '<meta name="robots" content="noindex,follow">')
    return h + nav("") + f'''
<section class="phead" style="min-height:52vh;display:grid;place-items:center">
  <div class="wrap phead__in center">
    <h1>Wrong turn on Ocean Drive</h1>
    <p class="lead" style="margin-inline:auto">That page is not here, but the bikes are.</p>
    <div class="btn-row btn-row--center" style="margin-top:1.6rem">
      <a class="btn" href="index.html">Back home</a>
      <a class="btn btn--ghost" href="rentals.html">See rentals</a>
    </div>
  </div>
</section>
''' + footer()


# ---------------------------------------------------------------- non-HTML
def build_sitemap():
    pages = [("index.html", "1.0", "weekly"), ("rentals.html", "0.9", "weekly"),
             ("tours.html", "0.9", "weekly"), ("adventures.html", "0.9", "weekly"),
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
    routes = "\n".join("- **%s** (%s, %s, %s): %s" % (r["name"], r["km"], r["time"], r["level"], r["desc"]) for r in ROUTES)
    faq = "\n\n".join("**Q: %s**\nA: %s" % (q, a) for q, a in FAQ)
    return f"""# {BIZ['name']}

> Bicycle, fat tire, electric bike, electric tandem, Trikke, Segway, side-by-side, tricycle and rollerblade rentals,
> guided Segway tours, and South Florida adventures (Everglades airboats, Key West day trips, Miami city tours,
> jet skis, parasailing, helicopter rides) in South Beach, Miami Beach, Florida.
> Shop at {BIZ['street']}, {BIZ['city']}, {BIZ['region']} {BIZ['zip']} — one block from Ocean Drive.
> Open every day 9:00 AM – 8:00 PM. Phone {BIZ['phone']}.
> Rentals from $12/hour, Segway tours from $49/person, Everglades airboat adventure $69/person.
> Items without a published price are booked by phone at {BIZ['phone']}.

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
- Authorized Segway dealer: sales, parts and service.
- Also books: Everglades airboat adventures, Key West day trips, Miami city tours, jet ski rentals, parasailing, helicopter rides.
- Payment: cash, credit and debit cards, Apple Pay, Google Pay. Reservations pre-paid in USD.
- Cancellation: 30+ days 100% refund · 15–30 days 50% · 8–14 days 25% · 0–7 days non-refundable.

## Rentals ({SITE}/rentals.html)
{fleet}

## Guided tours ({SITE}/tours.html)
{tours}

## Adventures and day trips ({SITE}/adventures.html)
{advs}

## Cycling routes from the shop ({SITE}/routes.html)
{routes}

## Frequently asked questions ({SITE}/faq.html)
{faq}

## Pages
- [Home]({SITE}/index.html): overview, fleet, tours, adventures, routes, reviews.
- [Rentals]({SITE}/rentals.html): all ten vehicles with hourly, all-day and weekly prices.
- [Tours]({SITE}/tours.html): six guided Segway and night tours with durations, stops and prices.
- [Adventures]({SITE}/adventures.html): Everglades, Key West, Miami city tour, jet ski, parasailing, helicopter.
- [Routes]({SITE}/routes.html): six free cycling route guides with distance and difficulty.
- [About]({SITE}/about.html): the shop, the workshop, the team.
- [FAQ]({SITE}/faq.html): prices, delivery, ages, safety, cancellations.
- [Contact]({SITE}/contact.html): booking form, map, hours, delivery zone.
"""


# ---------------------------------------------------------------- run
if __name__ == "__main__":
    print("Building Miami Beach Bikes...")
    write("index.html", page_index())
    write("rentals.html", page_rentals())
    write("tours.html", page_tours())
    write("adventures.html", page_adventures())
    write("routes.html", page_routes())
    write("about.html", page_about())
    write("faq.html", page_faq())
    write("contact.html", page_contact())
    write("404.html", page_404())
    write("sitemap.xml", build_sitemap())
    write("robots.txt", build_robots())
    write("llms.txt", build_llms())
    print("Done.")
