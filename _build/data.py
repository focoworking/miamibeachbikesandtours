# -*- coding: utf-8 -*-
"""Single source of truth: business data, fleet, tours, routes, FAQ."""

SITE = "https://www.miamibeachbikesandtours.com"

# The operator's live booking feed. Every "Book" button points here.
BOOKING_URL = "https://fareharbor.com/embeds/book/southfloridatrikketours/items/"

# Landmark covers.
#
# Empty = every Live Route stop uses the illustration drawn for it, which is
# ours, weighs about 6 KB and needs no attribution. Drop a Google Maps Static
# API key in here and every one of them becomes an official Street View
# photograph of that exact corner instead. That key is billed per request and
# belongs to the client, not to this repository — leave it empty in git.
STREETVIEW_KEY = ""

# Home page hero.
#
# Empty = the drawn South Beach scene. Point it at a photograph in
# assets/img/ and the home page leads with that instead — the illustration
# stays as the fallback and keeps serving the other pages. Give it the
# original, not a crop: the hero is landscape on a desktop and nearly
# portrait on a phone, so it is framed with object-position per breakpoint
# rather than cut once and compromised for both.
#
# Two conditions before a photograph of customers goes up: the shop has to
# own the shot, and anyone recognisable in it has to have signed a model
# release for commercial use. A photo on a rental company's home page is
# advertising, not a holiday snap.
HERO_PHOTO = "hero-oceandrive"   # basename; -900/-1400/-2000 and -tall-620/-900
HERO_FOCUS = "50% 58%"     # desktop framing
HERO_FOCUS_MOBILE = "50% 50%"   # the tall file is already framed

# WhatsApp uses the shop line, digits only.
WHATSAPP = "13058309440"
WHATSAPP_URL = ("https://wa.me/13058309440?text="
                "Hi%20Miami%20Beach%20Bikes%21%20I%27d%20like%20to%20ask%20about%20")

# --- Languages -------------------------------------------------------------
# English lives at the root; the others get their own directory. hreflang and
# the language switcher are generated from this list.
LANGS = [
    {"code": "en", "name": "English",    "short": "EN", "dir": "",    "locale": "en_US"},
    {"code": "es", "name": "Espa\u00f1ol",   "short": "ES", "dir": "es/", "locale": "es_ES"},
    {"code": "pt", "name": "Portugu\u00eas", "short": "PT", "dir": "pt/", "locale": "pt_BR"},
    {"code": "it", "name": "Italiano",   "short": "IT", "dir": "it/", "locale": "it_IT"},
]

BIZ = {
    "name": "Miami Beach Bikes",
    "legal": "Miami Beach Bikes · Rentals & Tours",
    "tagline": "Ride more. Worry less.",
    "happy_hour": "Happy hour 1–4 PM: one extra hour free on any rental",
    "phone": "+1-305-830-9440",
    "phone_pretty": "(305) 830-9440",
    "email": "hello@miamibeachbikesandtours.com",
    "street": "233 14th Street",
    "city": "Miami Beach",
    "region": "FL",
    "zip": "33139",
    "country": "US",
    "lat": "25.78730",
    "lng": "-80.13180",
    "hours": "Mo-Su 09:00-20:00",
    "hours_pretty": "Every day · 9:00 AM – 8:00 PM",
    "price_range": "$$",
    "areas": ["South Beach", "Mid-Beach", "North Beach", "Downtown Miami",
              "Brickell", "Wynwood", "Star Island", "Venetian Islands", "Key Biscayne", "Everglades", "Key West", "Coconut Grove"],
}

# --- Fleet ------------------------------------------------------------------
# cat drives the on-page chip filter. price = headline hourly rate (USD).
FLEET = [
    {
        "slug": "beach-cruiser", "cat": "bikes family", "img": "fleet-cruiser",
        "name": "Beach Cruiser", "tag": "Most booked",
        "hook": "The classic South Beach ride. Fat tires, wide saddle, one gear and zero stress along the Ocean Drive promenade.",
        "meta": ["Ages 13+", "Helmet + lock", "Basket $5"],
        "price": 12, "unit": "hour",
        "rates": [("1 hour", 12), ("2 hours", 18), ("4 hours", 22), ("All day 9am–8pm", 28), ("1 week", 75)],
    },
    {
        "slug": "fat-tire-bike", "cat": "bikes", "img": "fleet-fat-tire",
        "name": "Fat Tire Beach Bike", "tag": "Rides on sand",
        "hook": "Four-inch tires built for the hard-pack sand at the waterline. The only bike here you can actually ride on the beach.",
        "meta": ["Ages 16+", "Sand-capable", "Helmet + lock"],
        "price": 18, "unit": "hour",
        "rates": [("1 hour", 18), ("2 hours", 26), ("4 hours", 35), ("All day 9am–8pm", 45), ("1 week", 160)],
    },
    {
        "slug": "electric-bike", "cat": "bikes electric", "img": "fleet-ebike",
        "name": "Electric Bike", "tag": "Go further",
        "hook": "Pedal-assist up to 20 mph. Wynwood, Bayside, Downtown and back without breaking a sweat in the Miami sun.",
        "meta": ["Ages 16+", "40+ mi range", "Route map"],
        "price": 25, "unit": "hour",
        "rates": [("1 hour", 25), ("2 hours", 40), ("4 hours", 55), ("All day 9am–8pm", 89), ("1 week", 320)],
    },
    {
        "slug": "electric-tandem", "cat": "bikes electric family", "img": "fleet-etandem",
        "name": "Electric Tandem", "tag": "Two riders, one battery",
        "hook": "A pedal-assist tandem for two. The strongest rider sets the pace and nobody gets dropped halfway across the causeway.",
        "meta": ["2 riders", "Ages 16+", "Priced per group"],
        "price": 45, "unit": "hour",
        "rates": [("1 hour", 45), ("2 hours", 70), ("4 hours", 95), ("All day 9am–8pm", 130)],
    },
    {
        "slug": "trikke", "cat": "trikke electric", "img": "fleet-trikke",
        "name": "Trikke", "tag": "Our namesake",
        "hook": "The three-wheeled carving vehicle this shop was built around. You steer it by leaning, it is easier than a bike, and nothing turns more heads on Ocean Drive.",
        "meta": ["Ages 14+", "Training included", "Electric option"],
        "price": 35, "unit": "hour",
        "rates": [("30 minutes", 25), ("1 hour", 35), ("2 hours", 55), ("Half day", 79)],
    },
    {
        "slug": "segway", "cat": "segways electric", "img": "fleet-segway",
        "name": "Segway", "tag": "Authorized dealer",
        "hook": "Self-balancing, ridiculously fun and easier than it looks. Free training before every ride — and we sell and service them too.",
        "meta": ["Ages 14+", "Training included", "Guided tours"],
        "price": 49, "unit": "guided tour",
        "rates": [("Guided tour · from", 49), ("Sales, parts & service", 0)],
    },
    {
        "slug": "side-by-side", "cat": "family bikes", "img": "fleet-sidebyside",
        "name": "Side-by-Side & Tandem", "tag": "Ride together",
        "hook": "Four wheels, two seats, side by side — plus classic tandems. Talk the whole way instead of shouting over your shoulder.",
        "meta": ["2–4 riders", "Canopy", "Basket"],
        "price": 22, "unit": "hour",
        "rates": [("Tandem · 1 hour", 22), ("Tandem · all day", 55), ("Side-by-side · 1 hour", 39), ("Side-by-side · all day", 89)],
    },
    {
        "slug": "adult-tricycle", "cat": "bikes family", "img": "fleet-tricycle",
        "name": "Adult Tricycle", "tag": "Extra stable",
        "hook": "Three wheels, big rear basket, zero balance required. The pick for beach picnics and easy cruising.",
        "meta": ["Ages 16+", "Cargo basket", "No balance needed"],
        "price": 18, "unit": "hour",
        "rates": [("1 hour", 18), ("2 hours", 28), ("4 hours", 35), ("All day 9am–8pm", 45), ("1 week", 120)],
    },
    {
        "slug": "rollerblades", "cat": "skates family", "img": "fleet-skates",
        "name": "Rollerblades", "tag": "Lincoln Rd favorite",
        "hook": "Skate the Beachwalk like a local. Sizes for the whole family, pads and helmet included with every pair.",
        "meta": ["Kids + adults", "Pads included", "All sizes"],
        "price": 12, "unit": "hour",
        "rates": [("1 hour", 12), ("2 hours", 18), ("4 hours", 20), ("All day 9am–8pm", 25), ("1 week", 65)],
    },
    {
        "slug": "longboards", "cat": "skates family", "img": "fleet-skates",
        "name": "Longboards", "tag": "Cruise the strip",
        "hook": "Longboards for the Beachwalk and Lincoln Road. Pads and a helmet with every board, and a five-minute lesson if it is your first time.",
        "meta": ["Ages 12+", "Pads included", "Lesson included"],
        "price": 14, "unit": "hour",
        "rates": [("1 hour", 14), ("2 hours", 20), ("4 hours", 26), ("All day 9am\u20138pm", 32)],
    },
    {
        "slug": "kids-bikes", "cat": "family bikes", "img": "fleet-kids",
        "name": "Kids Bikes & Baby Seats", "tag": "Family ready",
        "hook": "Kids bikes from 12 to 24 inches, baby seats, trailers and training wheels. Everybody rolls, nobody gets left behind at the hotel.",
        "meta": ["Baby seats $5", "Trailers", "Training wheels"],
        "price": 10, "unit": "hour",
        "rates": [("Kids bike · 1 hour", 10), ("Kids bike · all day", 22), ("Baby seat", 5), ("Trailer · all day", 30), ("Basket add-on", 5)],
    },
]

# --- Tours ------------------------------------------------------------------
TOURS = [
    {
        "slug": "ocean-drive-segway-tour", "cat": "segway short", "img": "tour-segway-ocean",
        "name": "Ocean Drive Segway Tour", "tag": "Best first ride",
        "hook": "The short one, and the one everybody starts with. Ocean Drive, Lummus Park and the beachfront on a Segway, training included.",
        "meta": ["1 hour", "Ages 14+", "Min. 2 riders"],
        "price": 49, "dur": "PT1H", "dur_pretty": "1 hour",
        "stops": ["Ocean Drive", "Lummus Park", "10th St Auditorium", "Beachwalk"],
        "options": [("Per person", 49)],
    },
    {
        "slug": "star-island-segway-tour", "cat": "segway short", "img": "tour-segway-star",
        "name": "Star Island Segway Tour", "tag": "Celebrity homes",
        "hook": "Over the MacArthur Causeway on the protected path to the gates of Star Island — cruise-ship terminal on one side, mansions on the other.",
        "meta": ["1 hour", "Ages 14+", "Min. 2 riders"],
        "price": 69, "dur": "PT1H", "dur_pretty": "1 hour",
        "stops": ["MacArthur Causeway", "Star Island", "Palm & Hibiscus Islands", "Terminal Island"],
        "options": [("Per person", 69)],
    },
    {
        "slug": "south-beach-segway-tour", "cat": "segway half", "img": "tour-segway-sb",
        "name": "South Beach Segway Tour", "tag": "The full island",
        "hook": "The long version: Ocean Drive, Española Way, Lincoln Road, South Pointe Park and the pier, with stops long enough to actually take pictures.",
        "meta": ["2 hours", "Ages 14+", "Min. 2 riders"],
        "price": 79, "dur": "PT2H", "dur_pretty": "2 hours",
        "stops": ["Ocean Drive", "Española Way", "Lincoln Road", "South Pointe Park"],
        "options": [("Per person", 79)],
    },
    {
        "slug": "art-deco-segway-tour", "cat": "segway half", "img": "tour-segway-deco",
        "name": "Miami Beach Art Deco Segway Tour", "tag": "Signature",
        "hook": "Glide the Art Deco Historic District while your guide unpacks 1930s Miami Beach — neon, porthole windows, eyebrows and racing stripes.",
        "meta": ["2 hours", "Ages 14+", "Min. 2 riders"],
        "price": 79, "dur": "PT2H", "dur_pretty": "2 hours",
        "stops": ["Art Deco Historic District", "Colony Hotel", "Española Way", "Washington Avenue"],
        "options": [("Per person", 79)],
    },
    {
        "slug": "millionaires-row-segway-tour", "cat": "segway half", "img": "tour-segway-row",
        "name": "Miami Millionaire's Row Segway Tour", "tag": "Longest ride",
        "hook": "North up Collins past the Faena District, the Fontainebleau and the oceanfront estates of Millionaire's Row. Our biggest Segway route.",
        "meta": ["2.5 hours", "Ages 14+", "Min. 2 riders"],
        "price": 89, "dur": "PT2H30M", "dur_pretty": "2.5 hours",
        "stops": ["Faena District", "Fontainebleau", "Millionaire's Row", "Indian Beach Park"],
        "options": [("Per person", 89)],
    },
    {
        "slug": "panoramic-night-chariot-tour", "cat": "night private", "img": "tour-night",
        "name": "Panoramic Night Private Chariot Tour", "tag": "After dark",
        "hook": "Private, after-dark and lit up: the neon of Ocean Drive, the causeway lights and the Downtown skyline reflected across Biscayne Bay.",
        "meta": ["Private group", "Evening", "All ages"],
        "price": None, "dur": "PT2H", "dur_pretty": "~2 hours",
        "stops": ["Ocean Drive neon", "MacArthur Causeway", "Biscayne Bay", "Downtown skyline"],
        "options": [("Private group", None)],
    },
    {
        "slug": "trikke-tour-south-beach", "cat": "trikke short", "img": "tour-trikke",
        "name": "South Beach Trikke Tour", "tag": "Only here",
        "hook": "The tour you cannot book anywhere else: carving South Beach on a three-wheeled Trikke, steering by leaning. Five minutes of training and you are gone.",
        "meta": ["1–2 hours", "Ages 14+", "Training included"],
        "price": None, "dur": "PT1H", "dur_pretty": "1–2 hours",
        "stops": ["Ocean Drive", "Lummus Park", "Española Way", "South Pointe Park"],
        "options": [("Per person", None)],
    },
    {
        "slug": "art-deco-bike-tour", "cat": "bike short", "img": "tour-bike-deco",
        "name": "Art Deco Bike Tour", "tag": "All ages",
        "hook": "The Art Deco district at bicycle pace, with no minimum age and no training needed. The family version of our signature route.",
        "meta": ["~2 hours", "All ages", "Helmet + water"],
        "price": None, "dur": "PT2H", "dur_pretty": "~2 hours",
        "stops": ["Art Deco Historic District", "Ocean Drive", "Lummus Park", "Española Way"],
        "options": [("Per person", None)],
    },
    {
        "slug": "south-beach-coastal-bike-ride", "cat": "bike short", "img": "tour-bike-coastal",
        "name": "South Beach Coastal Ride", "tag": "Family favorite",
        "hook": "A flat, guided run down the car-free Beachwalk to South Pointe Park and the pier, with the Atlantic on your left the whole way.",
        "meta": ["90 min", "All ages", "Helmet + water"],
        "price": None, "dur": "PT1H30M", "dur_pretty": "90 min",
        "stops": ["Beachwalk", "Lummus Park", "South Pointe Park", "South Pointe Pier"],
        "options": [("Per person", None)],
    },
    {
        "slug": "wynwood-downtown-ebike-tour", "cat": "bike electric half", "img": "tour-ebike-wynwood",
        "name": "Wynwood & Downtown E-Bike Tour", "tag": "Street art",
        "hook": "Cross the bay under power and ride the murals of Wynwood, then the Design District, Bayside and Brickell. Our longest ride on two wheels.",
        "meta": ["~4 hours", "Ages 16+", "E-bike included"],
        "price": None, "dur": "PT4H", "dur_pretty": "~4 hours",
        "stops": ["Wynwood Walls", "Design District", "Bayside Marketplace", "Brickell"],
        "options": [("Per person", None)],
    },
    {
        "slug": "sunset-venetian-islands-tour", "cat": "bike electric short", "img": "tour-ebike-sunset",
        "name": "Sunset Venetian Islands Ride", "tag": "Golden hour",
        "hook": "Out across the Venetian Causeway at golden hour to watch the Downtown skyline switch on across Biscayne Bay.",
        "meta": ["2 hours", "Ages 16+", "Bike or e-bike"],
        "price": None, "dur": "PT2H", "dur_pretty": "2 hours",
        "stops": ["Venetian Causeway", "Belle Isle", "Di Lido Island", "Sunset Harbour"],
        "options": [("Per person", None)],
    },
    {
        "slug": "free-wynwood-bike-tour", "cat": "bike free short", "img": "tour-ebike-wynwood",
        "name": "Free Wynwood Bike Tour", "tag": "Free with rental",
        "hook": "A guided run through the murals of Wynwood at no charge when you rent from us. Small groups, fixed departures, first come first served.",
        "meta": ["Free with rental", "~2 hours", "Small group"],
        "price": 0, "dur": "PT2H", "dur_pretty": "~2 hours",
        "stops": ["Wynwood Walls", "NW 2nd Avenue", "Design District", "Mural alleys"],
        "options": [("Free with any rental", 0)],
    },
    {
        "slug": "free-coconut-grove-bike-tour", "cat": "bike free short", "img": "tour-bike-coastal",
        "name": "Free Coconut Grove Bike Tour", "tag": "Free with rental",
        "hook": "Miami's oldest neighbourhood — banyan trees, the bayfront marina and Vizcaya — guided and free when you rent with us.",
        "meta": ["Free with rental", "~2 hours", "Small group"],
        "price": 0, "dur": "PT2H", "dur_pretty": "~2 hours",
        "stops": ["CocoWalk", "Bayfront marina", "Barnacle Historic Park", "Vizcaya"],
        "options": [("Free with any rental", 0)],
    },
    {
        "slug": "private-group-corporate-tour", "cat": "private segway bike", "img": "tour-private",
        "name": "Private Group & Corporate Tour", "tag": "Your route",
        "hook": "Bachelorette parties, team offsites, family reunions and film crews. Pick the machines, the route and the hour and we build the tour around you.",
        "meta": ["Custom length", "Any group size", "Segway, bike or Trikke"],
        "price": None, "dur": "PT2H", "dur_pretty": "Custom",
        "stops": ["Your route", "Your pace", "Photo stops", "Optional guide car"],
        "options": [("Per group", None)],
    },
]

# --- Adventures: the off-the-island half of the catalogue -------------------
ADVENTURES = [
    {
        "slug": "everglades-airboat-adventure", "cat": "nature day", "img": "adv-everglades",
        "name": "Everglades Airboat Adventure", "tag": "Most booked day trip",
        "hook": "Out to the River of Grass for an airboat run through the sawgrass, a wildlife show and alligators at close range. Transport from South Beach included.",
        "meta": ["4.5 hours", "All ages", "Hotel pickup"],
        "price": 69, "dur": "PT4H30M", "dur_pretty": "4.5 hours",
        "stops": ["Hotel pickup", "Airboat ride", "Wildlife show", "Alligator encounter"],
        "options": [("Per person", 69)],
    },
    {
        "slug": "key-west-day-trip", "cat": "day", "img": "adv-keywest",
        "name": "Key West Day Trip", "tag": "Full day",
        "hook": "The whole Overseas Highway, Seven Mile Bridge included, with around six free hours on the island for Duval Street, Mallory Square and the Southernmost Point.",
        "meta": ["Full day", "All ages", "Hotel pickup"],
        "price": None, "dur": "P1D", "dur_pretty": "Full day",
        "stops": ["Seven Mile Bridge", "Duval Street", "Mallory Square", "Southernmost Point"],
        "options": [("Per person", None)],
    },
    {
        "slug": "miami-city-tour", "cat": "city day", "img": "adv-citytour",
        "name": "Miami City Tour", "tag": "Orientation",
        "hook": "Half a day across the whole city: Little Havana, Wynwood, the Design District, Brickell, Coconut Grove and back over the bay.",
        "meta": ["~4 hours", "All ages", "Hotel pickup"],
        "price": None, "dur": "PT4H", "dur_pretty": "~4 hours",
        "stops": ["Little Havana", "Wynwood Walls", "Design District", "Coconut Grove"],
        "options": [("Per person", None)],
    },
    {
        "slug": "big-bus-tour-miami", "cat": "city day", "img": "adv-bigbus",
        "name": "Big Bus Hop-On Hop-Off Tour", "tag": "Whole city pass",
        "hook": "Open-top double-decker with a day pass across Miami and Miami Beach. Hop off at Wynwood, Bayside or Little Havana and pick the next bus up when you are done.",
        "meta": ["1–2 day pass", "All ages", "Open top"],
        "price": None, "dur": "P1D", "dur_pretty": "Day pass",
        "stops": ["South Beach", "Wynwood", "Bayside", "Little Havana"],
        "options": [("Day pass", None)],
    },
    {
        "slug": "jet-ski-rental", "cat": "water", "img": "adv-jetski",
        "name": "Jet Ski Rental", "tag": "Adrenaline",
        "hook": "Open throttle on Biscayne Bay with the Downtown skyline as the backdrop. No licence needed, full safety brief before you launch.",
        "meta": ["30 or 60 min", "Ages 16+ to drive", "2 riders"],
        "price": None, "dur": "PT1H", "dur_pretty": "30–60 min",
        "stops": ["Marina check-in", "Safety brief", "Biscayne Bay run", "Skyline views"],
        "options": [("30 minutes", None), ("1 hour", None)],
    },
    {
        "slug": "parasailing-south-beach", "cat": "water", "img": "adv-parasail",
        "name": "South Beach Parasailing", "tag": "600 feet up",
        "hook": "Six hundred feet above the Atlantic with the whole Miami Beach coastline under your feet. Solo, tandem or triple flights, optional splash-down.",
        "meta": ["~1 hour", "Ages 6+", "No experience"],
        "price": None, "dur": "PT1H", "dur_pretty": "~1 hour",
        "stops": ["Marina check-in", "Boat ride", "Flight", "Optional splash-down"],
        "options": [("Single flight", None), ("Tandem flight", None), ("Triple flight", None)],
    },
    {
        "slug": "biscayne-bay-boat-cruise", "cat": "water", "img": "adv-boat",
        "name": "Biscayne Bay Millionaire's Row Cruise", "tag": "From the water",
        "hook": "The mansions of Star, Palm and Hibiscus Islands seen the way they were meant to be — from a boat, with the Downtown skyline behind them.",
        "meta": ["~90 min", "All ages", "Narrated"],
        "price": None, "dur": "PT1H30M", "dur_pretty": "~90 min",
        "stops": ["Star Island", "Palm & Hibiscus", "Port of Miami", "Downtown skyline"],
        "options": [("Per person", None)],
    },
    {
        "slug": "speedboat-sandbar-tour", "cat": "water", "img": "adv-speedboat",
        "name": "Speedboat & Sandbar Tour", "tag": "Miami classic",
        "hook": "Fast run out of the marina, then anchor at the sandbar where locals spend their Sundays in waist-deep, bath-warm water.",
        "meta": ["~2 hours", "All ages", "Swim stop"],
        "price": None, "dur": "PT2H", "dur_pretty": "~2 hours",
        "stops": ["Marina", "Government Cut", "Sandbar swim stop", "Skyline run"],
        "options": [("Per person", None)],
    },
    {
        "slug": "helicopter-ride-miami", "cat": "air", "img": "adv-helicopter",
        "name": "Miami Helicopter Ride", "tag": "Bucket list",
        "hook": "Flight over South Beach, Star Island, the Port of Miami and the Downtown skyline. The fastest way to understand how this city is laid out.",
        "meta": ["15–30 min", "All ages", "2–3 passengers"],
        "price": None, "dur": "PT30M", "dur_pretty": "15–30 min",
        "stops": ["South Beach", "Star Island", "Port of Miami", "Downtown skyline"],
        "options": [("Per person", None)],
    },
]

# --- Routes (GEO / local-intent content) -----------------------------------
ROUTES = [
    {"name": "The Beachwalk Classic", "slug": "the-beachwalk-classic", "km": "8 km · 5 mi", "time": "45 min", "level": "Easy",
     "from": "233 14th St", "to": "South Pointe Park",
     "desc": "Straight down the paved Beachwalk to South Pointe Park and back. Flat, car-free, shaded in stretches, and the single best first ride in South Beach.",
     "stops": ["Lummus Park", "Ocean Drive", "South Pointe Pier", "Joe's Stone Crab"]},
    {"name": "Art Deco Neon Loop", "slug": "art-deco-neon-loop", "km": "6 km · 3.7 mi", "time": "40 min", "level": "Easy",
     "from": "233 14th St", "to": "Española Way",
     "desc": "Ocean Drive, Collins, Washington and Española Way. Ride it after 7 PM when the neon fires up and the whole district turns pink and turquoise.",
     "stops": ["Colony Hotel", "Española Way", "Lincoln Road Mall", "Washington Ave"]},
    {"name": "Star Island & the Causeway", "slug": "star-island-&-the-causeway", "km": "16 km · 10 mi", "time": "1 h 15", "level": "Moderate",
     "from": "233 14th St", "to": "Star Island",
     "desc": "Protected bike path along the MacArthur Causeway to Palm, Hibiscus and Star Island. Cruise-ship views on one side, mansions on the other.",
     "stops": ["MacArthur Causeway", "Star Island gate", "Terminal Island", "South Pointe"]},
    {"name": "Venetian Islands Sunset", "slug": "venetian-islands-sunset", "km": "14 km · 8.7 mi", "time": "1 h", "level": "Moderate",
     "from": "233 14th St", "to": "Belle Isle",
     "desc": "Low-traffic island hopping across the Venetian Causeway. The classic golden-hour route with the Downtown skyline straight ahead.",
     "stops": ["Belle Isle", "Di Lido Island", "Rivo Alto", "Sunset Harbour"]},
    {"name": "Wynwood Mural Run", "slug": "wynwood-mural-run", "km": "26 km · 16 mi", "time": "2 h", "level": "E-bike",
     "from": "233 14th St", "to": "Wynwood Walls",
     "desc": "Our e-bike route across the bay into the street-art district, looping back through the Design District and Bayside. Take the battery.",
     "stops": ["Wynwood Walls", "NW 2nd Ave", "Design District", "Bayside Marketplace"]},
    {"name": "North Beach & Boardwalk", "slug": "north-beach-&-boardwalk", "km": "20 km · 12.4 mi", "time": "1 h 30", "level": "Moderate",
     "from": "233 14th St", "to": "North Beach Oceanside Park",
     "desc": "Head north along the boardwalk past Mid-Beach, the Faena District and the Fontainebleau all the way to the quiet end of the island.",
     "stops": ["Faena District", "Fontainebleau", "Indian Beach Park", "Oceanside Park"]},
]

# --- FAQ (AEO: short answer first, then detail) -----------------------------
FAQ = [
    ("Where can I rent a bike in South Beach?",
     "At our shop at 233 14th Street, Miami Beach, FL 33139 — one block from Ocean Drive and the Beachwalk. We are open every day from 9 AM to 8 PM. Walk-ins are welcome and we also deliver across South Beach."),
    ("How much does it cost to rent a bike in Miami Beach?",
     "Beach cruisers start at $12 for one hour and $28 for all day (9 AM to 8 PM). Fat tire beach bikes start at $18/hour, electric bikes at $25/hour, adult tricycles at $18/hour, tandems at $22/hour and rollerblades at $12/hour. Helmet, lock and bottled water are included with every rental."),
    ("What is the happy hour special?",
     "Rent between 1 PM and 4 PM and you get one extra hour free on any bike, trike or skate rental. It applies to walk-ins and reservations alike, every day of the week."),
    ("How much are the Segway tours?",
     "The Ocean Drive Segway Tour is $49 per person for one hour. The Star Island Segway Tour is $69, the South Beach and Art Deco Segway Tours are $79 each for two hours, and the Miami Millionaire's Row Segway Tour is $89 for 2.5 hours. All Segway tours include training and require a minimum of two riders."),
    ("What is a Trikke?",
     "A Trikke is a three-wheeled carving vehicle you steer by leaning your body from side to side — no pedals, no balancing act. It is the machine this shop is named after, it takes about five minutes to learn, and we rent it from $25 for 30 minutes."),
    ("Do I need to book in advance?",
     "For rentals, no — walk-ins are welcome all day, every day. Booking ahead is recommended in high season (December to April) and on weekends, and it is required for Segway tours, day trips, jet skis, parasailing and helicopter rides, which all run on fixed departure times."),
    ("Do you deliver bikes to my hotel?",
     "Yes. We deliver and pick up at hotels, Airbnbs and condos across South Beach and Mid-Beach. Delivery is free on rentals of 24 hours or more within South Beach; shorter rentals and other areas carry a flat delivery fee. Day trips and adventures include hotel pickup."),
    ("How long can I keep the bike?",
     "From one hour up to 60 days. Daily, weekly and monthly rates drop sharply the longer you ride — a week costs about the same as three single days."),
    ("What is included with a rental?",
     "Every rental includes a helmet, a lock, a bottle of water, a Miami Beach route map and roadside support by phone while you are out riding. Baskets and baby seats are $5 each."),
    ("How old do you have to be to ride a Segway or a Trikke?",
     "Riders must be at least 14 years old; riders under 18 must be accompanied by an adult. Every tour begins with a free training session, so no previous experience is needed, and Segway PT tours require no deposit at booking or in store."),
    ("What else do you book besides bikes and Segways?",
     "Everglades airboat adventures (4.5 hours, $69), Key West day trips, Miami city tours, Big Bus hop-on hop-off passes, jet ski rentals, South Beach parasailing, Biscayne Bay and sandbar boat tours, and helicopter rides over the city. All of them can be booked at the shop, online or by phone at +1-305-830-9440, and most include hotel pickup."),
    ("What guided tours do you run?",
     "Twelve of them. Five Segway tours with published prices — Ocean Drive $49, Star Island $69, South Beach $79, Art Deco $79 and Millionaire's Row $89 — plus a South Beach Trikke tour, an Art Deco bike tour, the South Beach Coastal Ride, a Wynwood and Downtown e-bike tour, a sunset ride across the Venetian Islands, a private night chariot tour and fully custom private and corporate tours."),
    ("Some tours do not show a price. Why?",
     "Those run on seasonal schedules or are priced per group, so the rate depends on the date, the group size and the operator. Call +1-305-830-9440 or book online and we will quote you on the spot — every one of them is bookable."),
    ("What is Live Route?",
     "Live Route is our free virtual tour guide for South Beach. You tell it how you are travelling \u2014 on foot, cruiser, electric bike, Segway, Trikke or skates \u2014 how long you have and what you are interested in, and it builds a route from our door at 233 14th Street through the landmarks that fit, then guides you stop by stop while you ride. It is on the website, so there is no app to install."),
    ("Do I need a bike to use Live Route?",
     "No. On foot is one of the six options and the Art Deco district works perfectly at walking pace. You will want wheels for South Pointe, the Venetian Islands or Wynwood \u2014 and we are at the start line either way."),
    ("Does Live Route cost anything?",
     "No. It is free, there is no sign-up and it works in any phone browser. Live mode asks for your location so it can tell you how far the next stop is; you can decline and follow the written route instead."),
    ("Can I extend my rental without coming back to the shop?",
     "Yes. Open the assistant on any page, tap Extend my rental, enter the ticket number from your receipt and pick how much longer you want \u2014 an hour, two, four, a day or a week. You pay on your phone with Apple Pay, Google Pay, card or PayPal and your return time moves automatically. No need to ride back."),
    ("What happens if I am already late returning?",
     "Extend it anyway. The assistant shows the rental as overdue and the extension covers you from the original return time, so there is no late fee on top. If you would rather talk to someone, call +1-305-830-9440 and we will sort it in under a minute."),
    ("Where do I find my ticket number?",
     "It is on the paper receipt we hand you at the counter and in your confirmation email, in the format MBB-1234. If you cannot find it, call +1-305-830-9440 with the name on the booking and we will look it up."),
    ("Do you sell Segways and Trikkes?",
     "Yes. We are Miami's factory authorized Segway dealer, so we sell new Segway personal transporters with full warranty, plus pedal and electric Trikkes, electric bikes, bicycles and the complete Segway i2 parts range \u2014 cargo frames, reflective shields, integrated lighting, patroller bags, bumpers, comfort mats and the accessory bar. Call +1-305-830-9440 for current models and pricing."),
    ("Can I try a Segway or Trikke before buying one?",
     "Yes, and we recommend it. Rent the exact model for an hour, take it down Ocean Drive, and if you buy it we put the rental toward the purchase."),
    ("Are the neighbourhood bike tours really free?",
     "Yes. The guided Wynwood and Coconut Grove bike tours are free when you rent from us. They run on fixed departures in small groups, first come first served, so ask at the counter or call ahead to reserve a spot."),
    ("Can I leave my luggage at the shop?",
     "Yes. We hold luggage at the shop while you ride \u2014 useful on your check-out day or between a cruise and a flight. There is also a restroom and free Wi-Fi."),
    ("Is Miami Beach safe for cycling?",
     "Yes. South Beach is flat, compact and covered by protected bike lanes plus the car-free Beachwalk that runs the length of the sand. Florida law requires helmets for riders under 16 and we provide one with every rental."),
    ("Do you repair bikes, e-bikes and scooters?",
     "Yes. Our shop handles flat tires, brakes, gears, batteries and full tune-ups for bikes, e-bikes and scooters, with most walk-in repairs finished the same day. We are also an authorized Segway dealer for sales, parts and service."),
    ("What is your cancellation policy?",
     "Cancellations 30 or more days before the reservation receive a full refund; 15 to 30 days receive 50%; 8 to 14 days receive 25%; and cancellations within 7 days of the reservation are non-refundable. All reservations are pre-paid in US dollars."),
]

REVIEWS = [
    ("The Art Deco Segway tour was the highlight of our trip. Twenty minutes of training and my mother-in-law was gliding down Ocean Drive like a pro.",
     "Danielle R. · Chicago"),
    ("Rented four bikes and a baby seat for a week. They delivered to our hotel on 16th, swapped a flat the same afternoon, no drama at all.",
     "The Okonkwo family · Atlanta"),
    ("Took the e-bikes to Wynwood and back. Best $89 we spent in Miami — we saw more of the city in one day than in the previous three.",
     "Marco V. · Milan"),
    ("Skated the Beachwalk at sunset with my kids. Pads, helmets and good advice on where to go. Super friendly crew.",
     "Yasmin K. · Toronto"),
    ("Parasailing over South Beach was unreal. Easy booking right at the shop and the boat crew made my ten-year-old feel completely safe.",
     "Greg P. · Boston"),
    ("They fixed my own bike's brakes in under an hour while I got coffee. Real mechanics, fair price, locals' spot.",
     "Andrés M. · Miami Beach"),
]

# --- Sales: the half of the business the site was missing ------------------
# South Florida Trikke is Miami's factory authorized Segway dealer and also
# sells electric Trikkes, e-bikes and Segway parts.
SHOP = [
    {
        "slug": "segway-sales", "cat": "segway", "img": "fleet-segway",
        "name": "Segway Personal Transporters", "tag": "Factory authorized dealer",
        "hook": "We are Miami's factory authorized Segway dealer. New units, full warranty, delivery across South Florida and a test ride before you buy — at the shop, on Ocean Drive.",
        "meta": ["New units", "Full warranty", "Test ride first"],
        "price": None, "unit": "unit",
        "rates": [("Segway i2 SE", None), ("Segway x2 SE", None), ("Trade-in / used", None)],
    },
    {
        "slug": "trikke-sales", "cat": "trikke", "img": "fleet-trikke",
        "name": "Trikke & Electric Trikke", "tag": "Our specialty",
        "hook": "The three-wheeled carving vehicle we are named after, in pedal and electric versions. Try one on a tour first, then buy the one you liked.",
        "meta": ["Pedal & electric", "All sizes", "Try before you buy"],
        "price": None, "unit": "unit",
        "rates": [("Trikke carving vehicle", None), ("Electric Trikke", None)],
    },
    {
        "slug": "ebike-sales", "cat": "bikes", "img": "fleet-ebike",
        "name": "Electric Bikes & Bicycles", "tag": "New & ex-fleet",
        "hook": "New electric bikes and bicycles, plus ex-rental cruisers serviced by our own mechanics and sold at a fraction of new.",
        "meta": ["New & ex-fleet", "Serviced", "Warranty"],
        "price": None, "unit": "bike",
        "rates": [("New electric bike", None), ("New bicycle", None), ("Ex-rental cruiser", None)],
    },
    {
        "slug": "segway-accessories", "cat": "parts segway", "img": "fleet-segway",
        "name": "Segway i2 Parts & Accessories", "tag": "In stock",
        "hook": "The full Segway parts range: lower cargo frames, upper and lower reflective shields, integrated lighting, patroller bag, front bumper, comfort mats and the optional accessory bar.",
        "meta": ["Genuine parts", "Fitted in store", "Shipping available"],
        "price": None, "unit": "part",
        "rates": [("Lower cargo frame", None), ("Reflective shields", None),
                  ("Integrated lighting system", None), ("Patroller bag", None),
                  ("Front bumper", None), ("Comfort mats", None), ("Accessory bar", None)],
    },
    {
        "slug": "repairs-service", "cat": "service", "img": "about-shop",
        "name": "Repairs & Service", "tag": "Same day",
        "hook": "Flats, brakes, gears, wheel truing, battery diagnostics and full tune-ups — for bikes, e-bikes, scooters and Segways. Ours or yours. Most walk-in repairs done the same day.",
        "meta": ["Walk-in", "Same day", "Bikes, e-bikes, Segways"],
        "price": None, "unit": "job",
        "rates": [("Flat repair", None), ("Brake / gear service", None),
                  ("Full tune-up", None), ("Segway service", None), ("Battery diagnostics", None)],
    },
]

# --- LIVE ROUTE ------------------------------------------------------------
# Virtual tour guide. Every stop is a real South Beach landmark with its own
# address; coordinates are approximate to the block and should be verified
# against Google Maps before launch.
#
# tags drive the interest filter; mins = how long people actually linger.
POI = [
    {"id": "shop", "name": "Miami Beach Bikes", "sub": "Your start line",
     "addr": "233 14th Street", "lat": 25.78730, "lng": -80.13180,
     "tags": ["start"], "mins": 0,
     "story": "Washington and 14th. Helmet on, water in the basket, map in your pocket. Everything from here is flat."},

    {"id": "espanola", "name": "Española Way", "sub": "The Spanish village",
     "addr": "419 Española Way", "lat": 25.78760, "lng": -80.13400,
     "tags": ["deco", "food", "photo"], "mins": 15,
     "story": "Built in 1922 as Whitman's Spanish Colony — a Mediterranean village dropped into Florida. Two blocks of pink stucco, striped awnings and tables in the middle of the street. Al Capone ran a casino upstairs at number 1421."},

    {"id": "lincoln", "name": "Lincoln Road Mall", "sub": "The mile-long promenade",
     "addr": "Lincoln Rd between Alton & Washington", "lat": 25.79070, "lng": -80.13400,
     "tags": ["food", "shop", "family"], "mins": 20,
     "story": "Morris Lapidus pedestrianised it in 1960 and called it a street for people, not cars. A mile of shops, cafes and street performers. Lock up and walk this one — no wheels on the mall."},

    {"id": "newworld", "name": "New World Center", "sub": "Gehry's concert hall",
     "addr": "500 17th Street", "lat": 25.79200, "lng": -80.13980,
     "tags": ["photo", "family"], "mins": 10,
     "story": "Frank Gehry built it in 2011 with a 7,000 sq ft projection wall on the outside — on Wallcast nights the orchestra plays inside and the park watches it on the wall for free."},

    {"id": "botanical", "name": "Miami Beach Botanical Garden", "sub": "Free green escape",
     "addr": "2000 Convention Center Drive", "lat": 25.79430, "lng": -80.13480,
     "tags": ["family", "nature", "photo"], "mins": 20,
     "story": "Two and a half acres of palms, orchids and a Japanese garden, free to walk in. The quietest spot within a mile of Ocean Drive."},

    {"id": "bass", "name": "The Bass Museum", "sub": "Contemporary art in a 1930 deco shell",
     "addr": "2100 Collins Avenue", "lat": 25.79550, "lng": -80.12900,
     "tags": ["deco", "art"], "mins": 25,
     "story": "Built in 1930 as the Miami Beach Public Library out of keystone — Florida coral rock full of fossils. Look at the walls before you look at the art."},

    {"id": "boardwalk", "name": "Miami Beach Boardwalk", "sub": "The sea-grape corridor",
     "addr": "Boardwalk at 21st Street", "lat": 25.79660, "lng": -80.12560,
     "tags": ["beach", "nature", "photo"], "mins": 10,
     "story": "Raised walkway through sea grape and palm all the way north. Bikes stay on the paved Beachwalk below — the wooden stretch is for feet only."},

    {"id": "beachwalk14", "name": "Beachwalk at 14th", "sub": "Car-free, ocean on your left",
     "addr": "Beachwalk at 14th Street", "lat": 25.78740, "lng": -80.12800,
     "tags": ["beach", "family", "photo"], "mins": 5,
     "story": "The paved path that runs the length of the sand. No traffic, no lights, no thinking — just turn right for South Pointe or left for North Beach."},

    {"id": "versace", "name": "Versace Mansion", "sub": "Villa Casa Casuarina",
     "addr": "1116 Ocean Drive", "lat": 25.78185, "lng": -80.13000,
     "tags": ["deco", "photo", "celeb"], "mins": 10,
     "story": "Built 1930 by Alden Freeman, modelled on the Alcázar de Colón in Santo Domingo. Gianni Versace bought it in 1992 and was shot on these steps in 1997. Today it is a hotel — and the most photographed doorway in Florida."},

    {"id": "clevelander", "name": "The Clevelander", "sub": "Ocean Drive's loudest corner",
     "addr": "1020 Ocean Drive", "lat": 25.78090, "lng": -80.13000,
     "tags": ["night", "photo"], "mins": 5,
     "story": "1938, and the pool bar that defines the Ocean Drive soundtrack. Ride past in daylight; come back after dark when the neon is on."},

    {"id": "artdeco", "name": "Art Deco Welcome Center", "sub": "Start of the district",
     "addr": "1001 Ocean Drive", "lat": 25.78070, "lng": -80.13010,
     "tags": ["deco", "art"], "mins": 15,
     "story": "Run by the Miami Design Preservation League, the people who saved this district from the bulldozers in the 1970s. Maps, exhibits and the reason any of these buildings still stand."},

    {"id": "lummus", "name": "Lummus Park", "sub": "The candy-coloured lifeguard towers",
     "addr": "10th Street & Ocean Drive", "lat": 25.78100, "lng": -80.12970,
     "tags": ["beach", "photo", "family"], "mins": 15,
     "story": "Ten blocks of palm and sand between Ocean Drive and the Atlantic. The lifeguard towers were rebuilt after Hurricane Andrew by architect William Lane, each one a different colour. The 10th Street tower is the one on every postcard."},

    {"id": "wolfsonian", "name": "The Wolfsonian", "sub": "Design, propaganda and industry",
     "addr": "1001 Washington Avenue", "lat": 25.78050, "lng": -80.13300,
     "tags": ["deco", "art"], "mins": 30,
     "story": "A 1927 storage building turned museum of how design shaped the modern world. The lobby fountain alone is worth the stop."},

    {"id": "colony", "name": "The Colony Hotel", "sub": "The blue neon one",
     "addr": "736 Ocean Drive", "lat": 25.77930, "lng": -80.13010,
     "tags": ["deco", "photo", "night"], "mins": 5,
     "story": "1935, by Henry Hohauser. That vertical blue neon sign is the single most recognisable object in Miami Beach — and it is best at dusk, not noon."},

    {"id": "oceandrive5", "name": "Ocean Drive & 5th", "sub": "Where the district begins",
     "addr": "5th Street & Ocean Drive", "lat": 25.77400, "lng": -80.13070,
     "tags": ["deco", "photo"], "mins": 5,
     "story": "The southern gate of the Art Deco district. From here to 15th is the largest concentration of Art Deco architecture on earth — about 800 buildings."},

    {"id": "joes", "name": "Joe's Stone Crab", "sub": "Open since 1913",
     "addr": "11 Washington Avenue", "lat": 25.76830, "lng": -80.13480,
     "tags": ["food", "celeb"], "mins": 10,
     "story": "Older than the city around it. Stone crab season runs mid-October to May, they do not take reservations, and the takeaway window beside the restaurant is the locals' move."},

    {"id": "southpointe", "name": "South Pointe Park", "sub": "Where the island ends",
     "addr": "1 Washington Avenue", "lat": 25.76500, "lng": -80.13400,
     "tags": ["beach", "family", "photo", "nature"], "mins": 20,
     "story": "Seventeen acres at the southern tip, with the 1931 lighthouse and a lawn built for watching cruise ships thread Government Cut. Best light of the day is here, one hour before sunset."},

    {"id": "southpointepier", "name": "South Pointe Pier", "sub": "Cruise ships at arm's length",
     "addr": "South Pointe Pier", "lat": 25.76450, "lng": -80.13070,
     "tags": ["photo", "beach"], "mins": 15,
     "story": "Walk out over the jetty and the ships pass close enough to read the names. Sunday afternoons the whole channel is boats."},

    {"id": "flamingo", "name": "Flamingo Park", "sub": "Where locals actually go",
     "addr": "1200 Meridian Avenue", "lat": 25.78370, "lng": -80.13760,
     "tags": ["family", "nature"], "mins": 15,
     "story": "Tennis, a track, a pool and shade. Four blocks from Ocean Drive and a completely different city."},

    {"id": "sunsetharbour", "name": "Sunset Harbour", "sub": "The neighbourhood side",
     "addr": "Purdy Avenue & 18th Street", "lat": 25.79300, "lng": -80.14270,
     "tags": ["food", "shop"], "mins": 20,
     "story": "Where Miami Beach eats when it is not performing: coffee roasters, a fish counter, no neon. Ride here for lunch, not for the view."},

    {"id": "belleisle", "name": "Belle Isle", "sub": "First of the Venetian Islands",
     "addr": "Venetian Causeway at Belle Isle", "lat": 25.79080, "lng": -80.14530,
     "tags": ["photo", "nature", "celeb"], "mins": 10,
     "story": "Cross the 1926 Venetian Causeway and the whole Downtown skyline opens across Biscayne Bay. Low traffic, flat, and the best golden hour on the island."},

    {"id": "macarthur", "name": "MacArthur Causeway lookout", "sub": "Star Island and the port",
     "addr": "MacArthur Causeway bike path", "lat": 25.77160, "lng": -80.15200,
     "tags": ["celeb", "photo"], "mins": 10,
     "story": "Protected path with the cruise terminal on one side and the gates of Star, Palm and Hibiscus Islands on the other. You cannot ride onto Star Island — it is private — but the gate is the photo."},

    {"id": "faena", "name": "Faena District", "sub": "The gold mammoth",
     "addr": "3201 Collins Avenue", "lat": 25.80500, "lng": -80.12300,
     "tags": ["art", "celeb", "photo"], "mins": 15,
     "story": "Mid-Beach turned into an arts district by Alan Faena. Damien Hirst's gilded mammoth skeleton stands in a glass case you can see from the street."},

    {"id": "fontainebleau", "name": "Fontainebleau", "sub": "1954, and still showing off",
     "addr": "4441 Collins Avenue", "lat": 25.81800, "lng": -80.12200,
     "tags": ["celeb", "deco", "photo"], "mins": 10,
     "story": "Morris Lapidus's curved masterpiece, where Sinatra filmed and Bond swam. Walk into the lobby — the staircase to nowhere is still there."},
]

# Travel modes for the live route planner. speed = km/h on the flat.
MODES = [
    {"id": "walk",    "name": "On foot",      "short": "Walk",   "icon": '<svg viewBox="0 0 48 48" width="34" height="34" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="26" cy="8" r="4" fill="currentColor" stroke="none"/><path d="M26 14 L22 24 L28 28 L30 38"/><path d="M22 24 L15 32"/><path d="M26 17 L33 21"/></svg>', "speed": 4.5,
     "blurb": "No rental needed. Great for the deco strip, slow for anything past 5th Street.",
     "cta": None},
    {"id": "cruiser", "name": "Beach cruiser", "short": "Bike",   "icon": '<svg viewBox="0 0 48 48" width="34" height="34" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="33" r="9"/><circle cx="36" cy="33" r="9"/><path d="M12 33 L20 18 L30 18 M20 18 L26 33 L36 33"/><path d="M17 14 L25 14"/></svg>', "speed": 12,
     "blurb": "The default. Flat, easy, covers the whole island.", "cta": "rentals.html#beach-cruiser"},
    {"id": "ebike",   "name": "Electric bike", "short": "E-bike", "icon": '<svg viewBox="0 0 48 48" width="34" height="34" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="33" r="9"/><circle cx="36" cy="33" r="9"/><path d="M12 33 L20 18 L30 18 M20 18 L26 33 L36 33"/><path d="M17 14 L25 14"/><path d="M27 20 l-7 9 h6 l-6 9" stroke-width="3.4" stroke-linejoin="miter"/></svg>', "speed": 18,
     "blurb": "Doubles your range. Wynwood and Mid-Beach come into play.", "cta": "rentals.html#electric-bike"},
    {"id": "segway",  "name": "Segway",        "short": "Segway", "icon": '<svg viewBox="0 0 48 48" width="34" height="34" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="13" cy="36" r="7"/><circle cx="35" cy="36" r="7"/><path d="M13 36 L35 36"/><path d="M24 36 L24 12"/><path d="M16 9 L32 9"/></svg>', "speed": 12,
     "blurb": "Guided only \u2014 we build the route, a guide rides it with you.", "cta": "tours.html"},
    {"id": "trikke",  "name": "Trikke",        "short": "Trikke", "icon": '<svg viewBox="0 0 48 48" width="34" height="34" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="10" cy="36" r="6"/><circle cx="24" cy="36" r="6"/><circle cx="38" cy="36" r="6"/><path d="M10 36 L24 22 L38 36"/><path d="M24 22 L24 10"/><path d="M17 8 L31 8"/></svg>', "speed": 10,
     "blurb": "Carve it by leaning. Best on the wide flat paths.", "cta": "rentals.html#trikke"},
    {"id": "skate",   "name": "Skates or longboard", "short": "Skates", "icon": '<svg viewBox="0 0 48 48" width="34" height="34" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 30 L8 16 L16 16 L22 22 L34 24 L34 30 Z"/><circle cx="13" cy="36" r="5"/><circle cx="29" cy="36" r="5"/></svg>', "speed": 10,
     "blurb": "Beachwalk and Lincoln Road only. Avoid the causeways.", "cta": "rentals.html#rollerblades"},
]

INTERESTS = [
    ("deco",   "Art Deco",        "\U0001F3E8"),
    ("beach",  "Beach & ocean",   "\U0001F3D6️"),
    ("photo",  "Photo spots",     "\U0001F4F8"),
    ("food",   "Food & coffee",   "☕"),
    ("celeb",  "Mansions & fame", "⭐"),
    ("art",    "Art & museums",   "\U0001F3A8"),
    ("family", "Family friendly", "\U0001F46A"),
    ("night",  "Neon after dark", "\U0001F303"),
    ("nature", "Parks & green",   "\U0001F334"),
    ("shop",   "Shopping",        "\U0001F6CD️"),
]

DURATIONS = [
    {"id": "30",  "name": "30 minutes", "mins": 30},
    {"id": "60",  "name": "1 hour",     "mins": 60},
    {"id": "120", "name": "2 hours",    "mins": 120},
    {"id": "240", "name": "Half a day", "mins": 240},
]

# --- Rental extension -------------------------------------------------------
# What an extension costs, per vehicle family. Derived from the same rate card
# as FLEET so the two can never drift apart.
EXTEND_BLOCKS = [
    {"id": "1h",  "label": "+1 hour",  "mins": 60},
    {"id": "2h",  "label": "+2 hours", "mins": 120},
    {"id": "4h",  "label": "+4 hours", "mins": 240},
    {"id": "1d",  "label": "+1 day",   "mins": 660},   # 9am-8pm
    {"id": "1w",  "label": "+1 week",  "mins": 4620},
]

# family -> {block id: price in USD}. None = quote at the counter.
EXTEND_RATES = {
    "cruiser":   {"1h": 12, "2h": 18, "4h": 22, "1d": 28,  "1w": 75},
    "fat-tire":  {"1h": 18, "2h": 26, "4h": 35, "1d": 45,  "1w": 160},
    "ebike":     {"1h": 25, "2h": 40, "4h": 55, "1d": 89,  "1w": 320},
    "etandem":   {"1h": 45, "2h": 70, "4h": 95, "1d": 130, "1w": None},
    "trikke":    {"1h": 35, "2h": 55, "4h": 79, "1d": None, "1w": None},
    "sidebyside":{"1h": 39, "2h": 60, "4h": 75, "1d": 89,  "1w": None},
    "tricycle":  {"1h": 18, "2h": 28, "4h": 35, "1d": 45,  "1w": 120},
    "skates":    {"1h": 12, "2h": 18, "4h": 20, "1d": 25,  "1w": 65},
    "longboard": {"1h": 14, "2h": 20, "4h": 26, "1d": 32,  "1w": None},
    "kids":      {"1h": 10, "2h": 15, "4h": 18, "1d": 22,  "1w": None},
    "tandem":    {"1h": 22, "2h": 34, "4h": 44, "1d": 55,  "1w": None},
}

EXTEND_FAMILIES = [
    ("cruiser",    "Beach cruiser"),
    ("fat-tire",   "Fat tire beach bike"),
    ("ebike",      "Electric bike"),
    ("etandem",    "Electric tandem"),
    ("trikke",     "Trikke"),
    ("sidebyside", "Side-by-side"),
    ("tandem",     "Tandem"),
    ("tricycle",   "Adult tricycle"),
    ("skates",     "Rollerblades"),
    ("longboard",  "Longboard"),
    ("kids",       "Kids bike"),
]

# Payment methods offered at checkout. Every one of these hands off to the
# provider's own hosted page — no card details are ever typed into this site.
PAY_METHODS = [
    # generic glyphs, not brand logos — the name beside them does the identifying
    {"id": "applepay", "name": "Apple Pay",  "icon": '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="2" width="12" height="20" rx="3"/><path d="M11 18h2"/></svg>', "note": "One tap on iPhone"},
    {"id": "googlepay","name": "Google Pay", "icon": '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><rect x="4" y="3" width="11" height="18" rx="3"/><path d="M18 9a5 5 0 0 1 0 6"/><path d="M20.5 6.5a8.5 8.5 0 0 1 0 11"/></svg>', "note": "One tap on Android"},
    {"id": "card",     "name": "Card",       "icon": '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="5" width="20" height="14" rx="3"/><path d="M2 10h20"/><path d="M6 15h4"/></svg>', "note": "Visa, Mastercard, Amex"},
    {"id": "paypal",   "name": "PayPal",     "icon": '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2"/><rect x="3" y="7" width="18" height="13" rx="3"/><circle cx="16.5" cy="13.5" r="1.4"/></svg>', "note": "Pay with your balance"},
]
