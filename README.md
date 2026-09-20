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
index.html          Home: hero, finder, fleet, tours, routes, reviews, FAQ
rentals.html        Full fleet + complete price table
tours.html          6 guided tours + price table + tour FAQ
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

## Before going live — two things to confirm with the client

1. **Prices.** The rate tables in `_build/data.py` (`FLEET`, `TOURS`) are South Beach market rates, not
   confirmed from the client's own price list. Replace them with the real numbers and rebuild.
   Same for the review quotes in `REVIEWS` and the "since 2009" / fleet-size figures.
2. **The booking form** on `contact.html` currently uses a `mailto:` action, which is unreliable across
   browsers. Point it at a form backend (Formspree, Netlify Forms, or the client's booking system) or
   embed the existing reservation widget.
