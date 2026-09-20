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
assets/img/*.svg        Generated artwork (hero scene + card scenes + favicon)

llms.txt            Machine-readable business brief for AI answer engines
robots.txt          Crawl rules, incl. explicit allow for LLM crawlers
sitemap.xml         All indexable pages

_build/             Page generator (data.py + shell.py + build.py)
```

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
