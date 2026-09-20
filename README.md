# Miami Beach Bikes & Tours

Static marketing site for a South Beach bike / e-bike / Segway rental shop and tour operator.
Zero dependencies, zero build step to serve — plain HTML, one CSS file, one JS file.

**Design reference:** the layout language of high-end charter sites (centered-logo horizontal nav,
fullscreen parallax hero with a booking "finder" bar overlapping it, filterable gallery grid,
editorial split sections, dark bands). Repainted in a South Beach palette: Atlantic turquoise,
sunset coral, Art Deco gold, palm green and sand.

**Content source:** the real business data of Miami Beach Bike Rental (233 14th Street, South Beach).

---

## Structure

```
index.html          Home: hero, finder, fleet, tours, adventures, routes, reviews, FAQ
live-route.html     Live Route — the self-guided tour builder + live navigation
shop.html           Segway / Trikke / e-bike sales, i2 parts, repairs & service
rentals.html        10 rentals + complete price table
tours.html          6 guided Segway / night tours + price table + tour FAQ
adventures.html     Everglades, Key West, Miami city tour, jet ski, parasailing, helicopter
routes.html         6 free cycling route guides (local-intent content)
about.html          Shop story, workshop, stats
faq.html            10 FAQs + cancellation policy table
contact.html        Booking form, map, hours, delivery zone
404.html            Not-found page (noindex)

assets/css/style.css    Design system: tokens, components, animations, responsive
assets/js/main.js       Parallax, scroll reveals, sticky nav, filters, counters, open/closed status
assets/js/assistant.js  The assistant panel: Live Route engine + rental extension flow
_build/i18n.py          Interface strings in EN / ES / PT / IT
es/ pt/ it/             Generated language builds (do not edit by hand)
assets/img/*.svg        Generated artwork (hero scene + card scenes + favicon)

llms.txt            Machine-readable business brief for AI answer engines
robots.txt          Crawl rules, incl. explicit allow for LLM crawlers
sitemap.xml         All indexable pages

_build/             Page generator (data.py + shell.py + build.py)
```

## The assistant

Every page carries an assistant that opens in its own full-screen panel (`assets/js/assistant.js`),
so a flow never gets mixed into the page behind it. Launch it from the desktop pill bottom-right,
the mobile action bar, any `data-assistant="<view>"` element, or a `#assistant=<view>` deep link.
It traps focus, closes on Escape or scrim click, has a back stack, and restores scroll and focus.

### Tool 1 — Live Route

A free self-guided tour builder. Three steps: how you travel (6 modes), how long you have (4
budgets), what you like (10 interests). Then:

- **Planner.** Nearest-neighbour over the POIs whose tags match, distances by Haversine. Riding time
  is `distance / mode speed` padded 35% for lights and crossings. A stop is only added if there is
  time for it *plus* the ride home. Walking and skating drop the causeway stops automatically.
- **Live mode.** `watchPosition` gives distance and compass bearing to the next stop and advances
  within 45 m. Degrades cleanly when permission is denied or GPS cannot fix.
- **Maps handoff.** One tap builds a `google.com/maps/dir/` URL with every stop in order.

`live-route.html` stays as the SEO landing: it keeps all 24 stops as static HTML, the structured
data and the answer box, and its CTA opens the assistant.

### Tool 2 — Extend my rental

Ticket number → see the rental and when it is due → pick +1h / +2h / +4h / +1 day / +1 week →
pick a payment method → hand off to checkout. Prices come from `EXTEND_RATES` per vehicle family,
multiplied by the number of units. An overdue rental is flagged and the copy states the extension
covers the time from the original return, so there is no late fee stacked on top.

**No card details are ever entered on this site.** The flow stops at method selection and hands off
to the provider's own hosted page — keep it that way, it is what keeps PCI scope off this codebase.

### Wiring it to the real system

Two hooks, both in `ASSIST_CONFIG` (emitted by `_build/shell.py`):

```js
lookupUrl : "/api/rental/{ref}"   // GET -> { ref, name, family, item, qty, dueInMins }
payUrl    : "https://…/checkout"  // receives ?ref=&block=&method=
```

`family` must match a key in `EXTEND_RATES`. Until `lookupUrl` is set the panel runs in **demo
mode**, says so on screen in a yellow notice, and only resolves the three sample tickets
(`MBB-4417`, `MBB-2098`, `MBB-7731`). Do not ship to customers with that notice showing.

FareHarbor is the operator's booking system, so the likely shape is a small endpoint that proxies
their API for the lookup, and their own checkout or a Stripe payment link for `payUrl`.

## Languages

The site builds into four languages from one source. English lives at the root; the rest get a
directory: `/es/`, `/pt/`, `/it/`. Every page carries `hreflang` for all four plus `x-default`,
the sitemap lists every URL with its alternates, and the switcher sits top-right in the bar.

- `_build/i18n.py` holds the interface strings — navigation, buttons, the whole assistant, footer,
  labels. `t(key, lang)` falls back to English on a missing key, so a partial translation degrades
  instead of rendering blank.
- `pack(lang)` ships the same dictionary to the browser, so the assistant speaks the page's
  language with no extra request.
- `LANGS` in `_build/data.py` drives directories, locales and the switcher. Adding a fifth language
  means adding a row there and a column in `i18n.py`.

**Translation status:** the interface is complete in all four. The editorial content — product
descriptions, tour and adventure copy, POI stories, FAQ answers, page headlines and meta
descriptions — is still English in `/es/`, `/pt/` and `/it/`. That content lives in `_build/data.py`
and needs the same treatment: a per-language dictionary keyed by slug. Until it is done, do not
submit the translated directories to Search Console — duplicate English under a Spanish URL is
worse than no Spanish URL.

## Editing content

**All copy, prices, tours, routes and FAQs live in `_build/data.py`.** Edit there, then:

```bash
python3 _build/build.py
```

That regenerates every HTML file, plus `sitemap.xml`, `robots.txt` and `llms.txt`,
and keeps the structured data (JSON-LD) in sync automatically.

Editing the HTML directly works too, but the next build overwrites it.

## Local preview

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Deployment

Any static host (Netlify, Vercel, Cloudflare Pages, GitHub Pages, S3).
Set `SITE` in `_build/data.py` to the production domain before building — it feeds every
canonical URL, Open Graph tag, sitemap entry and JSON-LD `@id`.

---

## FOCOW mode: SEO / AEO / GEO / LLM

**SEO**
- Unique title, meta description, keywords and canonical per page.
- One `<h1>` per page, clean heading hierarchy, semantic landmarks, descriptive alt text.
- Open Graph + Twitter cards on every page.
- `sitemap.xml` with per-page priority and changefreq; `robots.txt` pointing at it.
- Internal linking: every page links to rentals, tours, routes and contact.
- Performance: no framework, no images over the wire except inline-cheap SVG, deferred JS,
  preconnect to the font host, `loading="lazy"` on every non-hero image.
- Accessibility (which is ranking-relevant): skip link, focus-visible outlines, `prefers-reduced-motion`,
  ARIA on nav and filters, table captions.

**AEO (answer engines / featured snippets)**
- An `answer-box` near the top of the home, rentals, tours and routes pages: an explicit question as a
  heading and a complete, self-contained answer in one short paragraph — the shape snippets extract.
- `FAQPage` JSON-LD on home, rentals, tours, routes and FAQ; answers are written short-first.
- `speakable` JSON-LD marking the hero, the answer box and the FAQ for voice assistants.
- A cancellation-policy table and a price table: structured facts, easy to lift.

**GEO (local / "near me" intent)**
- `LocalBusiness` JSON-LD typed as `BicycleStore` + `TouristInformationCenter`, with address, geo
  coordinates, opening hours, payment methods, languages, amenities and `areaServed` for nine
  neighborhoods.
- `geo.region`, `geo.position`, `ICBM` and `business:contact_data:*` meta tags.
- NAP (name, address, phone) identical in the top bar, the footer, contact page, JSON-LD and `llms.txt`.
- An embedded map, a `hasMap` link, and neighborhood-level content (`routes.html`) naming real local
  landmarks: Beachwalk, Lummus Park, Star Island, Venetian Causeway, Wynwood Walls, South Pointe.

**LLM (AI visibility)**
- `llms.txt` at the root: a dense, citable brief with address, hours, every price, every tour, every
  route and every Q&A — the format LLM crawlers and agents read first. Linked from every page head.
- `robots.txt` explicitly allows GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended,
  Applebot-Extended, CCBot, Amazonbot and meta-externalagent.
- Entity-rich JSON-LD graph: `LocalBusiness`, `WebSite` + `SearchAction`, `ItemList`, `Product` + `Offer`
  per rental, `TouristTrip` + `TouristAttraction` itineraries per tour, `BreadcrumbList`, `FAQPage`.
- Prose written as declarative fact statements ("Beach cruisers start at $12 per hour"), which is what
  gets quoted back in an AI answer.

---

## Content audit — what came across from the client's site, and what has not

The client's own sites (miamibeachbikerental.com / southfloridatrikke.com) are blocked by this
environment's network egress policy, so nothing was read from them directly. Everything below was
reconstructed from public sources: their pages as they appear in search results, Yelp, TripAdvisor,
Greetwell, Wanderlog and the OTAs. **That means this is a faithful reconstruction, not a migration.**

### Carried across

| Area | Status |
|---|---|
| NAP, hours, languages | ✅ 233 14th Street, +1 305-830-9440, 9 AM–8 PM daily, EN/ES/PT |
| Rentals | ✅ 11 — cruiser, fat tire, e-bike, e-tandem, Trikke, Segway, side-by-side, tricycle, rollerblades, longboards, kids & baby seats |
| Guided tours | ✅ 14, incl. the 5 Segway tours at their published prices, and the free Wynwood / Coconut Grove tours |
| Adventures | ✅ 9 — Everglades airboat, Key West, Miami city tour, Big Bus, jet ski, parasailing, boat cruise, sandbar, helicopter |
| Sales & service | ✅ Segway (factory authorized dealer), Trikkes, e-bikes, i2 parts range, repairs |
| Policies | ✅ Cancellation ladder, pre-payment, min. 2 riders, no Segway deposit, age limits |
| Amenities | ✅ Restroom, Wi-Fi, luggage storage, hotel delivery, happy hour 1–4 PM |
| Booking | ✅ Every button points at their live FareHarbor feed |

### NOT carried across — still needed from the client

- **Rental price list.** The hourly/daily figures in `FLEET` are South Beach market estimates.
  Only the tour prices and the Everglades airboat are the operator's published numbers.
- **Sales prices.** No Segway, Trikke, e-bike or parts pricing is public. Those cards show
  "Price on request" with a call button.
- **Blog.** Their site runs one; no posts were recoverable. This is the biggest SEO gap — see below.
- **Rental extension backend.** The assistant's extend flow is complete as an interface but runs in
  demo mode until `lookupUrl` and `payUrl` are wired — see *The assistant* below.
- **Photo gallery.** They have a tours gallery. Replaced here with illustrations.
- **Shopping cart / e-commerce.** Their site has a real cart for parts and merchandise. Not rebuilt.
- **Terms, waiver and rental requirements.** ID, deposit, credit card hold, damage and insurance
  terms are all unknown and are legally required before taking bookings.
- **Social profiles.** No Instagram / Facebook / TikTok URLs, so `sameAs` is absent from the
  LocalBusiness schema — that field matters for entity resolution in Google and in LLM answers.
- **Google Business Profile URL**, review counts and holiday hours.
- **Team, founding year and fleet size.** "Since 2009", "4.8 / 131 reviews" and the stat tiles are
  placeholders pulled from the Yelp listing, not verified with the client.

## Catalogue: what is confirmed and what is not

The catalogue mirrors the operator's live booking feed
(`https://fareharbor.com/embeds/book/southfloridatrikketours/items/`) — the same business as
Miami Beach Bike Rental / South Florida Trikke. **Every "Book" button on the site points at that
feed**; items with no published price show "Price on request" and a `tel:` button instead, so
nothing in the catalogue is a dead end.

**Confirmed prices** (published by the operator, live on the site):

| Item | Price |
|---|---|
| Ocean Drive Segway Tour | $49 / person, 1 h |
| Star Island Segway Tour | $69 / person, 1 h |
| South Beach Segway Tour | $79 / person, 2 h |
| Miami Beach Art Deco Segway Tour | $79 / person, 2 h |
| Miami Millionaire's Row Segway Tour | $89 / person, 2.5 h |
| Everglades Airboat Adventure | $69 / person, 4.5 h |

Also confirmed and published: happy hour 1–4 PM adds one free hour; Segway tours need a minimum of
two riders and take no deposit; the cancellation ladder (100 / 50 / 25 / 0%); baskets and baby
seats $5; hours 9 AM–8 PM daily; address 233 14th Street, Miami Beach, FL 33139.

**Listed without a price** — bookable by phone, priced per group or seasonal. Give us the numbers
and they publish like the rest:

- Tours: South Beach Trikke Tour, Art Deco Bike Tour, South Beach Coastal Ride, Wynwood & Downtown
  E-Bike Tour, Sunset Venetian Islands Ride, Panoramic Night Private Chariot Tour, Private Group &
  Corporate Tour.
- Adventures: Key West Day Trip, Miami City Tour, Big Bus Hop-On Hop-Off, Jet Ski Rental, South
  Beach Parasailing, Biscayne Bay Millionaire's Row Cruise, Speedboat & Sandbar Tour, Miami
  Helicopter Ride.

**Estimated, needs the client's real list:** the rental rate table (`FLEET` in `_build/data.py`).
The per-hour and all-day numbers are South Beach market rates, not the shop's own. The rates that
circulate on OTA listings carry reseller markup and are not usable.

Also unverified: the review quotes in `REVIEWS`, the "since 2009" line and the 4.8 / 131 rating.

## Before going live

1. **Swap the estimated rental rates** in `_build/data.py`, add any missing tour prices, then run
   `python3 _build/build.py`. Setting a `price` from `None` to a number switches that card from
   "Price on request / Call to book" to a price and a Book button automatically, and updates the
   price table, the JSON-LD offer and `llms.txt` in the same pass.
2. **Booking.** Buttons currently open the FareHarbor item list in a new tab. FareHarbor also ships
   a lightbox embed — dropping their script in and adding their class to the buttons opens booking
   in place. The `contact.html` form still uses a `mailto:` action; point it at a form backend or
   remove it in favour of the booking flow.
3. **NAP.** The address is 233 14th Street, Miami Beach, FL 33139 everywhere on the site, in the
   JSON-LD and in `llms.txt`. Make the Google Business Profile and every directory listing match it
   character for character — local ranking runs on that consistency.
