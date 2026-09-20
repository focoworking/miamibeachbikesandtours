# -*- coding: utf-8 -*-
"""Page copy in four languages: titles, meta descriptions, H1s, leads,
answer boxes and section headings. English is the source."""

PAGES = {
# ===================== landmarks on the home page =====================
"lm.eyebrow": {
 "en": "What you came for",
 "es": "A lo que viniste",
 "pt": "O que você veio ver",
 "it": "Quello per cui sei venuto"},
"lm.h2": {
 "en": "The South Beach you actually want to see",
 "es": "El South Beach que de verdad quieres ver",
 "pt": "A South Beach que você realmente quer ver",
 "it": "La South Beach che vuoi davvero vedere"},
"lm.lead": {
 "en": "Twenty-three landmarks sit inside an hour of our door — Art Deco neon, the Versace steps, Gehry's concert hall, the pier where the cruise ships pass. Take the wheels, take the route, take your time.",
 "es": "Veintitrés lugares emblemáticos están a menos de una hora de nuestra puerta: el neón art déco, las escaleras de Versace, el auditorio de Gehry, el muelle por donde pasan los cruceros. Coge las ruedas, coge la ruta y tómate tu tiempo.",
 "pt": "Vinte e três pontos emblemáticos ficam a menos de uma hora da nossa porta: o neon art déco, a escadaria da Versace, a sala de concertos de Gehry, o píer por onde passam os cruzeiros. Pegue as rodas, pegue a rota e vá sem pressa.",
 "it": "Ventitré luoghi simbolo sono a meno di un'ora dalla nostra porta: il neon art déco, la scalinata di Versace, l'auditorium di Gehry, il molo dove passano le navi da crociera. Prendi le ruote, prendi il percorso e prenditi il tuo tempo."},
"lm.cta": {
 "en": "See all 23 stops",
 "es": "Ver las 23 paradas",
 "pt": "Ver as 23 paradas",
 "it": "Vedi tutte le 23 tappe"},

# ===================== titles & descriptions =====================
"t.index": {
 "en": "Miami Beach Bikes | Bike, E-Bike & Segway Rentals and Tours · South Beach",
 "es": "Miami Beach Bikes | Alquiler de bicis, e-bikes y Segways y tours · South Beach",
 "pt": "Miami Beach Bikes | Aluguel de bikes, e-bikes e Segways e passeios · South Beach",
 "it": "Miami Beach Bikes | Noleggio bici, e-bike e Segway e tour · South Beach"},
"d.index": {
 "en": "Rent bikes, e-bikes, Trikkes, Segways, longboards and skates in South Beach from $12/hour. Segway tours from $49, free Wynwood and Coconut Grove bike tours, Everglades and Key West day trips, Segway sales and same-day repairs. Open daily 9 AM – 8 PM at 233 14th Street.",
 "es": "Alquila bicis, e-bikes, Trikkes, Segways, longboards y patines en South Beach desde 12 $/hora. Tours en Segway desde 49 $, tours gratis en bici por Wynwood y Coconut Grove, excursiones a los Everglades y Key West, venta de Segway y reparaciones el mismo día. Abierto todos los días de 9:00 a 20:00 en el 233 de la calle 14.",
 "pt": "Alugue bikes, e-bikes, Trikkes, Segways, longboards e patins em South Beach a partir de US$ 12/hora. Passeios de Segway a partir de US$ 49, passeios grátis de bike por Wynwood e Coconut Grove, bate-voltas aos Everglades e Key West, venda de Segway e consertos no mesmo dia. Aberto todos os dias das 9h às 20h na 233 da rua 14.",
 "it": "Noleggia bici, e-bike, Trikke, Segway, longboard e pattini a South Beach da 12 $ l'ora. Tour in Segway da 49 $, tour gratuiti in bici di Wynwood e Coconut Grove, gite alle Everglades e a Key West, vendita Segway e riparazioni in giornata. Aperto tutti i giorni dalle 9 alle 20 al 233 della 14ª strada."},
"t.rentals": {
 "en": "Rentals | Bikes, E-Bikes, Trikkes, Segways & Skates in South Beach from $12/hr",
 "es": "Alquiler | Bicis, e-bikes, Trikkes, Segways y patines en South Beach desde 12 $/h",
 "pt": "Aluguel | Bikes, e-bikes, Trikkes, Segways e patins em South Beach a partir de US$ 12/h",
 "it": "Noleggio | Bici, e-bike, Trikke, Segway e pattini a South Beach da 12 $/ora"},
"d.rentals": {
 "en": "Full price list for beach cruiser, fat tire, electric bike, electric tandem, Trikke, side-by-side, tricycle, rollerblade and kids' bike rentals in South Beach. Hourly, all-day and weekly rates, happy hour 1-4 PM, helmet and lock included, free South Beach hotel delivery.",
 "es": "Tarifas completas de alquiler en South Beach: beach cruiser, fat tire, bici eléctrica, tándem eléctrico, Trikke, lado a lado, triciclo, patines y bicis infantiles. Precios por hora, día completo y semana, happy hour de 13:00 a 16:00, casco y candado incluidos y entrega gratis en hoteles de South Beach.",
 "pt": "Tabela completa de aluguel em South Beach: beach cruiser, fat tire, bike elétrica, tandem elétrico, Trikke, lado a lado, triciclo, patins e bikes infantis. Preços por hora, dia inteiro e semana, happy hour das 13h às 16h, capacete e cadeado inclusos e entrega grátis em hotéis de South Beach.",
 "it": "Listino completo dei noleggi a South Beach: beach cruiser, fat tire, bici elettrica, tandem elettrico, Trikke, affiancata, triciclo, pattini e bici per bambini. Tariffe orarie, giornaliere e settimanali, happy hour dalle 13 alle 16, casco e lucchetto inclusi e consegna gratuita negli hotel di South Beach."},
"t.tours": {
 "en": "Tours | Segway, Bike, E-Bike & Trikke Guided Tours in Miami Beach",
 "es": "Tours | Tours guiados en Segway, bici, e-bike y Trikke en Miami Beach",
 "pt": "Passeios | Passeios guiados de Segway, bike, e-bike e Trikke em Miami Beach",
 "it": "Tour | Tour guidati in Segway, bici, e-bike e Trikke a Miami Beach"},
"d.tours": {
 "en": "Guided Segway tours of Ocean Drive ($49), Star Island ($69), South Beach and the Art Deco District ($79) and Millionaire's Row ($89), plus bike, e-bike and Trikke tours, private night tours, and free guided Wynwood and Coconut Grove bike tours with any rental.",
 "es": "Tours guiados en Segway por Ocean Drive (49 $), Star Island (69 $), South Beach y el distrito Art Déco (79 $) y Millionaire's Row (89 $), además de tours en bici, e-bike y Trikke, tours nocturnos privados y tours guiados gratis en bici por Wynwood y Coconut Grove con cualquier alquiler.",
 "pt": "Passeios guiados de Segway pela Ocean Drive (US$ 49), Star Island (US$ 69), South Beach e o distrito Art Déco (US$ 79) e Millionaire's Row (US$ 89), além de passeios de bike, e-bike e Trikke, passeios noturnos privativos e passeios guiados grátis de bike por Wynwood e Coconut Grove com qualquer aluguel.",
 "it": "Tour guidati in Segway su Ocean Drive (49 $), Star Island (69 $), South Beach e il distretto Art Déco (79 $) e Millionaire's Row (89 $), più tour in bici, e-bike e Trikke, tour notturni privati e tour guidati gratuiti in bici di Wynwood e Coconut Grove con qualsiasi noleggio."},
"t.adventures": {
 "en": "Everglades Airboats, Key West Day Trips, Jet Ski & Parasailing | Miami Beach",
 "es": "Everglades en hidrodeslizador, excursiones a Key West, motos de agua y parasailing | Miami Beach",
 "pt": "Airboat nos Everglades, bate-volta a Key West, jet ski e parasailing | Miami Beach",
 "it": "Airboat nelle Everglades, gite a Key West, moto d'acqua e parasailing | Miami Beach"},
"d.adventures": {
 "en": "Book Everglades airboat adventures from $69, Key West day trips, Miami city tours, jet ski rentals, South Beach parasailing and helicopter rides — all from our shop at 233 14th Street, South Beach. Most include hotel pickup.",
 "es": "Reserva aventuras en hidrodeslizador por los Everglades desde 69 $, excursiones de un día a Key West, city tours de Miami, alquiler de motos de agua, parasailing en South Beach y vuelos en helicóptero — todo desde nuestra tienda del 233 de la calle 14, South Beach. La mayoría incluye recogida en el hotel.",
 "pt": "Reserve aventuras de airboat nos Everglades a partir de US$ 69, bate-voltas a Key West, city tours de Miami, aluguel de jet ski, parasailing em South Beach e voos de helicóptero — tudo na nossa loja na 233 da rua 14, South Beach. A maioria inclui busca no hotel.",
 "it": "Prenota avventure in airboat nelle Everglades da 69 $, gite a Key West, city tour di Miami, noleggio moto d'acqua, parasailing a South Beach e voli in elicottero — tutto dal nostro negozio al 233 della 14ª strada, South Beach. Quasi tutto include il ritiro in hotel."},
"t.live": {
 "en": "Live Route | Free Self-Guided South Beach Tour · Virtual Tour Guide",
 "es": "Ruta Viva | Tour autoguiado gratis por South Beach · Guía turístico virtual",
 "pt": "Rota Viva | Passeio autoguiado grátis por South Beach · Guia turístico virtual",
 "it": "Rotta Live | Tour autoguidato gratuito di South Beach · Guida turistica virtuale"},
"d.live": {
 "en": "A free virtual tour guide for South Beach. Pick how you travel — on foot, bike, e-bike, Segway, Trikke or skates — how long you have and what you like, and it builds a route from 233 14th Street through the Art Deco district, Ocean Drive, Lummus Park and South Pointe, then guides you stop by stop.",
 "es": "Un guía turístico virtual gratuito para South Beach. Elige cómo te mueves — a pie, en bici, e-bike, Segway, Trikke o patines —, cuánto tiempo tienes y qué te gusta, y te monta una ruta desde el 233 de la calle 14 por el distrito Art Déco, Ocean Drive, Lummus Park y South Pointe, y luego te guía parada a parada.",
 "pt": "Um guia turístico virtual gratuito para South Beach. Escolha como você se move — a pé, de bike, e-bike, Segway, Trikke ou patins —, quanto tempo tem e do que gosta, e ele monta uma rota a partir da 233 da rua 14 pelo distrito Art Déco, Ocean Drive, Lummus Park e South Pointe, e depois te guia parada por parada.",
 "it": "Una guida turistica virtuale gratuita per South Beach. Scegli come ti muovi — a piedi, in bici, e-bike, Segway, Trikke o pattini —, quanto tempo hai e cosa ti piace, e costruisce un percorso dal 233 della 14ª strada attraverso il distretto Art Déco, Ocean Drive, Lummus Park e South Pointe, poi ti guida tappa dopo tappa."},
"t.shop": {
 "en": "Segway Dealer Miami | Buy Segways, Trikkes, E-Bikes & Parts · South Beach",
 "es": "Distribuidor Segway en Miami | Compra Segways, Trikkes, e-bikes y repuestos · South Beach",
 "pt": "Revendedor Segway em Miami | Compre Segways, Trikkes, e-bikes e peças · South Beach",
 "it": "Rivenditore Segway a Miami | Compra Segway, Trikke, e-bike e ricambi · South Beach"},
"d.shop": {
 "en": "Miami's factory authorized Segway dealer. Buy Segway personal transporters, electric Trikkes, e-bikes and genuine Segway i2 parts — cargo frames, reflective shields, lighting, patroller bags. Same-day repairs for bikes, e-bikes and Segways.",
 "es": "Distribuidor oficial de fábrica de Segway en Miami. Compra transportadores personales Segway, Trikkes eléctricos, e-bikes y repuestos originales Segway i2 — bastidores de carga, protectores reflectantes, iluminación y bolsas patrulleras. Reparaciones el mismo día de bicis, e-bikes y Segways.",
 "pt": "Revendedor autorizado de fábrica da Segway em Miami. Compre transportadores pessoais Segway, Trikkes elétricos, e-bikes e peças originais Segway i2 — suportes de carga, protetores refletivos, iluminação e bolsas patrulha. Consertos no mesmo dia de bikes, e-bikes e Segways.",
 "it": "Rivenditore autorizzato di fabbrica Segway a Miami. Compra trasportatori personali Segway, Trikke elettrici, e-bike e ricambi originali Segway i2 — telai da carico, scudi riflettenti, illuminazione e borse patroller. Riparazioni in giornata di bici, e-bike e Segway."},
"t.routes": {
 "en": "Best Bike Routes in Miami Beach & South Beach | Free Route Guide",
 "es": "Las mejores rutas en bici por Miami Beach y South Beach | Guía gratuita",
 "pt": "As melhores rotas de bike em Miami Beach e South Beach | Guia gratuito",
 "it": "I migliori percorsi in bici a Miami Beach e South Beach | Guida gratuita"},
"d.routes": {
 "en": "Six tried-and-tested cycling routes from South Beach: the Beachwalk, the Art Deco neon loop, Star Island, the Venetian Islands, Wynwood and North Beach. Distances, times, difficulty and what to see along the way.",
 "es": "Seis rutas en bici probadas desde South Beach: el Beachwalk, el circuito del neón Art Déco, Star Island, las Venetian Islands, Wynwood y North Beach. Distancias, tiempos, dificultad y qué ver por el camino.",
 "pt": "Seis rotas de bike testadas a partir de South Beach: o Beachwalk, o circuito do neon Art Déco, Star Island, as Venetian Islands, Wynwood e North Beach. Distâncias, tempos, dificuldade e o que ver pelo caminho.",
 "it": "Sei percorsi in bici collaudati da South Beach: il Beachwalk, l'anello del neon Art Déco, Star Island, le Venetian Islands, Wynwood e North Beach. Distanze, tempi, difficoltà e cosa vedere lungo la strada."},
"t.about": {
 "en": "About Miami Beach Bikes | South Beach Bike Shop, Segway Dealer & Tour Operator",
 "es": "Sobre Miami Beach Bikes | Tienda de bicis, distribuidor Segway y operador de tours en South Beach",
 "pt": "Sobre a Miami Beach Bikes | Loja de bikes, revendedor Segway e operadora de passeios em South Beach",
 "it": "Chi siamo | Negozio di bici, rivenditore Segway e tour operator a South Beach"},
"d.about": {
 "en": "A family-run bike shop, Segway dealer and tour operator at 233 14th Street, South Beach. Rentals, guided Segway tours, Everglades and Key West day trips, and a full repair workshop. Open every day, 9 AM to 8 PM.",
 "es": "Una tienda de bicis familiar, distribuidor Segway y operador de tours en el 233 de la calle 14, South Beach. Alquileres, tours guiados en Segway, excursiones a los Everglades y Key West, y un taller completo. Abierto todos los días de 9:00 a 20:00.",
 "pt": "Uma loja de bikes familiar, revendedor Segway e operadora de passeios na 233 da rua 14, South Beach. Aluguéis, passeios guiados de Segway, bate-voltas aos Everglades e Key West, e uma oficina completa. Aberto todos os dias das 9h às 20h.",
 "it": "Un negozio di bici a conduzione familiare, rivenditore Segway e tour operator al 233 della 14ª strada, South Beach. Noleggi, tour guidati in Segway, gite alle Everglades e a Key West, e un'officina completa. Aperto tutti i giorni dalle 9 alle 20."},
"t.faq": {
 "en": "FAQ | Bike Rental & Tours in Miami Beach — Prices, Delivery, Policies",
 "es": "Preguntas frecuentes | Alquiler de bicis y tours en Miami Beach — precios, entrega y políticas",
 "pt": "Perguntas frequentes | Aluguel de bikes e passeios em Miami Beach — preços, entrega e políticas",
 "it": "Domande frequenti | Noleggio bici e tour a Miami Beach — prezzi, consegna e regole"},
"d.faq": {
 "en": "Answers on bike rental prices in Miami Beach, hotel delivery, minimum ages, Segway tour rules, rental durations, what is included, cycling safety and our cancellation policy.",
 "es": "Respuestas sobre precios de alquiler de bicis en Miami Beach, entrega en hoteles, edades mínimas, normas de los tours en Segway, duraciones, qué está incluido, seguridad al pedalear y nuestra política de cancelación.",
 "pt": "Respostas sobre preços de aluguel de bikes em Miami Beach, entrega em hotéis, idades mínimas, regras dos passeios de Segway, durações, o que está incluso, segurança ao pedalar e nossa política de cancelamento.",
 "it": "Risposte su prezzi del noleggio bici a Miami Beach, consegna in hotel, età minime, regole dei tour in Segway, durate, cosa è incluso, sicurezza in bici e la nostra politica di cancellazione."},
"t.contact": {
 "en": "Contact & Booking | Miami Beach Bikes, 233 14th Street South Beach",
 "es": "Contacto y reservas | Miami Beach Bikes, 233 calle 14, South Beach",
 "pt": "Contato e reservas | Miami Beach Bikes, 233 rua 14, South Beach",
 "it": "Contatti e prenotazioni | Miami Beach Bikes, 233 14ª strada, South Beach"},
"d.contact": {
 "en": "Book a bike, e-bike, Trikke, Segway tour, Everglades airboat, Key West day trip, jet ski or parasailing in South Beach. Call (305) 830-9440 or walk in at 233 14th Street, Miami Beach, FL 33139. Open daily 9 AM – 8 PM.",
 "es": "Reserva una bici, e-bike, Trikke, tour en Segway, hidrodeslizador por los Everglades, excursión a Key West, moto de agua o parasailing en South Beach. Llama al (305) 830-9440 o pásate por el 233 de la calle 14, Miami Beach, FL 33139. Abierto todos los días de 9:00 a 20:00.",
 "pt": "Reserve uma bike, e-bike, Trikke, passeio de Segway, airboat nos Everglades, bate-volta a Key West, jet ski ou parasailing em South Beach. Ligue para (305) 830-9440 ou passe na 233 da rua 14, Miami Beach, FL 33139. Aberto todos os dias das 9h às 20h.",
 "it": "Prenota una bici, e-bike, Trikke, tour in Segway, airboat nelle Everglades, gita a Key West, moto d'acqua o parasailing a South Beach. Chiama il (305) 830-9440 o passa al 233 della 14ª strada, Miami Beach, FL 33139. Aperto tutti i giorni dalle 9 alle 20."},
"t.404": {
 "en": "Page not found | Miami Beach Bikes", "es": "Página no encontrada | Miami Beach Bikes",
 "pt": "Página não encontrada | Miami Beach Bikes", "it": "Pagina non trovata | Miami Beach Bikes"},
"d.404": {
 "en": "That page took a wrong turn on Ocean Drive. Head back to rentals, tours or routes.",
 "es": "Esa página se equivocó de giro en Ocean Drive. Vuelve a alquiler, tours o rutas.",
 "pt": "Essa página errou a curva na Ocean Drive. Volte para aluguel, passeios ou rotas.",
 "it": "Quella pagina ha sbagliato svolta su Ocean Drive. Torna a noleggio, tour o percorsi."},
}

PAGES.update({
# ===================== hero =====================
"h.hero1": {"en": "Ride more.", "es": "Rueda más.", "pt": "Pedale mais.", "it": "Pedala di più."},
"h.hero2": {"en": "Worry less.", "es": "Preocúpate menos.", "pt": "Preocupe-se menos.", "it": "Pensaci meno."},
"h.hero_sub_a": {
 "en": "Bikes, e-bikes, Trikkes, Segways and skates one block from Ocean Drive — plus ",
 "es": "Bicis, e-bikes, Trikkes, Segways y patines a una manzana de Ocean Drive — y además ",
 "pt": "Bikes, e-bikes, Trikkes, Segways e patins a um quarteirão da Ocean Drive — e ainda ",
 "it": "Bici, e-bike, Trikke, Segway e pattini a un isolato da Ocean Drive — e in più "},
"h.hero_sub_long": {
 "en": "Segway tours of the Art Deco District and Star Island, Everglades airboats, Key West day trips, jet skis and parasailing. Family-friendly, sun-powered, unreasonably fun.",
 "es": "tours en Segway por el distrito Art Déco y Star Island, hidrodeslizadores en los Everglades, excursiones a Key West, motos de agua y parasailing. Para toda la familia, a pleno sol y sin medida.",
 "pt": "passeios de Segway pelo distrito Art Déco e Star Island, airboats nos Everglades, bate-voltas a Key West, jet skis e parasailing. Para a família toda, a pleno sol e sem moderação.",
 "it": "tour in Segway del distretto Art Déco e di Star Island, airboat nelle Everglades, gite a Key West, moto d'acqua e parasailing. Per tutta la famiglia, sotto il sole e senza misura."},
"h.hero_sub_short": {
 "en": "guided tours, Everglades airboats and Key West day trips.",
 "es": "tours guiados, hidrodeslizadores en los Everglades y excursiones a Key West.",
 "pt": "passeios guiados, airboats nos Everglades e bate-voltas a Key West.",
 "it": "tour guidati, airboat nelle Everglades e gite a Key West."},
"h.cta_rent": {"en": "Rent a ride · from $12", "es": "Alquila · desde 12 $",
               "pt": "Alugue · a partir de US$ 12", "it": "Noleggia · da 12 $"},
"h.cta_tours": {"en": "See the tours", "es": "Ver los tours", "pt": "Ver os passeios", "it": "Vedi i tour"},

# ===================== finder =====================
"f.what": {"en": "What do you want to ride?", "es": "¿Qué quieres montar?",
           "pt": "O que você quer pilotar?", "it": "Cosa vuoi guidare?"},
"f.anything": {"en": "Anything with wheels", "es": "Cualquier cosa con ruedas",
               "pt": "Qualquer coisa com rodas", "it": "Qualsiasi cosa con le ruote"},
"f.bikes": {"en": "Bikes & cruisers", "es": "Bicis y cruisers", "pt": "Bikes e cruisers", "it": "Bici e cruiser"},
"f.electric": {"en": "Electric bikes", "es": "Bicis eléctricas", "pt": "Bikes elétricas", "it": "Bici elettriche"},
"f.segways": {"en": "Segways", "es": "Segways", "pt": "Segways", "it": "Segway"},
"f.skates": {"en": "Rollerblades", "es": "Patines en línea", "pt": "Patins in-line", "it": "Pattini in linea"},
"f.family": {"en": "Family & kids", "es": "Familia y niños", "pt": "Família e crianças", "it": "Famiglia e bambini"},
"f.tour": {"en": "Guided tour", "es": "Tour guiado", "pt": "Passeio guiado", "it": "Tour guidato"},
"f.when": {"en": "When", "es": "Cuándo", "pt": "Quando", "it": "Quando"},
"f.howlong": {"en": "How long", "es": "Cuánto tiempo", "pt": "Por quanto tempo", "it": "Per quanto"},
"f.riders": {"en": "Riders", "es": "Personas", "pt": "Pessoas", "it": "Persone"},
"f.rider1": {"en": "1 rider", "es": "1 persona", "pt": "1 pessoa", "it": "1 persona"},
"f.rider2": {"en": "2 riders", "es": "2 personas", "pt": "2 pessoas", "it": "2 persone"},
"f.rider34": {"en": "3–4 riders", "es": "3–4 personas", "pt": "3–4 pessoas", "it": "3–4 persone"},
"f.rider58": {"en": "5–8 riders", "es": "5–8 personas", "pt": "5–8 pessoas", "it": "5–8 persone"},
"f.rider9": {"en": "Group 9+", "es": "Grupo de 9+", "pt": "Grupo de 9+", "it": "Gruppo 9+"},
"f.month": {"en": "1 month", "es": "1 mes", "pt": "1 mês", "it": "1 mese"},
"f.find": {"en": "Find it", "es": "Búscalo", "pt": "Buscar", "it": "Trova"},
"f.legend": {"en": "Find your ride", "es": "Encuentra tu vehículo",
             "pt": "Encontre seu veículo", "it": "Trova il tuo mezzo"},

# ===================== trust strip =====================
"tr.reviews": {"en": "4.8 · 131 reviews", "es": "4,8 · 131 reseñas",
               "pt": "4,8 · 131 avaliações", "it": "4,8 · 131 recensioni"},
"tr.included": {"en": "Helmet, lock &amp; water included", "es": "Casco, candado y agua incluidos",
                "pt": "Capacete, cadeado e água inclusos", "it": "Casco, lucchetto e acqua inclusi"},
"tr.delivery": {"en": "Free hotel delivery 24h+", "es": "Entrega gratis en hotel desde 24 h",
                "pt": "Entrega grátis no hotel a partir de 24 h", "it": "Consegna gratuita in hotel da 24 h"},
"tr.happy": {"en": "Happy hour 1–4 PM · +1 free hour", "es": "Happy hour 13:00–16:00 · +1 hora gratis",
             "pt": "Happy hour 13h–16h · +1 hora grátis", "it": "Happy hour 13–16 · +1 ora gratis"},
"tr.freetours": {"en": "Free Wynwood &amp; Coconut Grove tours", "es": "Tours gratis por Wynwood y Coconut Grove",
                 "pt": "Passeios grátis por Wynwood e Coconut Grove", "it": "Tour gratuiti di Wynwood e Coconut Grove"},

# ===================== page headers =====================
"p.rentals_h": {"en": "Rentals", "es": "Alquiler", "pt": "Aluguel", "it": "Noleggio"},
"p.rentals_lead": {
 "en": "Ten kinds of wheels, from one hour to sixty days. Helmet, lock, cold water and a route map come with every single one — and an extra free hour if you start between 1 and 4 PM.",
 "es": "Diez tipos de ruedas, de una hora a sesenta días. Casco, candado, agua fría y mapa de rutas con todos y cada uno — y una hora extra gratis si empiezas entre las 13:00 y las 16:00.",
 "pt": "Dez tipos de rodas, de uma hora a sessenta dias. Capacete, cadeado, água gelada e mapa de rotas com todos eles — e uma hora extra grátis se você começar entre 13h e 16h.",
 "it": "Dieci tipi di ruote, da un'ora a sessanta giorni. Casco, lucchetto, acqua fresca e mappa dei percorsi con ognuno di essi — e un'ora extra gratis se parti tra le 13 e le 16."},
"p.tours_h": {"en": "Guided tours", "es": "Tours guiados", "pt": "Passeios guiados", "it": "Tour guidati"},
"p.tours_lead": {
 "en": "Twelve guided rides: Segway, bike, e-bike and Trikke, one hour to a full afternoon, from $49. Training always included, and a private version of any of them.",
 "es": "Doce salidas guiadas: Segway, bici, e-bike y Trikke, de una hora a una tarde entera, desde 49 $. Entrenamiento siempre incluido, y versión privada de cualquiera de ellas.",
 "pt": "Doze saídas guiadas: Segway, bike, e-bike e Trikke, de uma hora a uma tarde inteira, a partir de US$ 49. Treinamento sempre incluído, e versão privativa de qualquer uma delas.",
 "it": "Dodici uscite guidate: Segway, bici, e-bike e Trikke, da un'ora a un pomeriggio intero, da 49 $. Addestramento sempre incluso, e la versione privata di ognuna."},
"p.adv_h": {"en": "Adventures &amp; day trips", "es": "Aventuras y excursiones",
            "pt": "Aventuras e bate-voltas", "it": "Avventure e gite"},
"p.adv_lead": {
 "en": "Everything that does not fit on two wheels: airboats through the sawgrass, the Overseas Highway to Key West, jet skis on the bay, 600 feet of parasail and the city from a helicopter.",
 "es": "Todo lo que no cabe sobre dos ruedas: hidrodeslizadores entre los juncos, la Overseas Highway hasta Key West, motos de agua en la bahía, 180 metros de parasail y la ciudad desde un helicóptero.",
 "pt": "Tudo o que não cabe sobre duas rodas: airboats entre os juncos, a Overseas Highway até Key West, jet skis na baía, 180 metros de parasail e a cidade de helicóptero.",
 "it": "Tutto ciò che non sta su due ruote: airboat tra i giunchi, la Overseas Highway fino a Key West, moto d'acqua sulla baia, 180 metri di parasail e la città dall'elicottero."},
"p.live_h": {"en": "Live Route", "es": "Ruta Viva", "pt": "Rota Viva", "it": "Rotta Live"},
"p.live_lead": {
 "en": "A virtual tour guide that starts at our door on Washington and 14th and takes you to the South Beach worth seeing. Tell it how you are moving, how long you have and what you like — it builds the route and then talks you through it, stop by stop, while you ride.",
 "es": "Un guía turístico virtual que arranca en nuestra puerta de Washington con la calle 14 y te lleva al South Beach que merece la pena. Dile cómo te mueves, cuánto tiempo tienes y qué te gusta — monta la ruta y luego te la va contando, parada a parada, mientras ruedas.",
 "pt": "Um guia turístico virtual que começa na nossa porta na Washington com a rua 14 e te leva à South Beach que vale a pena. Diga como você está se movendo, quanto tempo tem e do que gosta — ele monta a rota e depois vai te contando, parada por parada, enquanto você pedala.",
 "it": "Una guida turistica virtuale che parte dalla nostra porta su Washington angolo 14ª e ti porta nella South Beach che vale la pena vedere. Dille come ti muovi, quanto tempo hai e cosa ti piace — costruisce il percorso e poi te lo racconta, tappa dopo tappa, mentre pedali."},
"p.live_badge": {"en": "Free · no app · works on your phone", "es": "Gratis · sin app · funciona en tu móvil",
                 "pt": "Grátis · sem app · funciona no seu celular", "it": "Gratis · senza app · funziona sul telefono"},
"p.shop_h": {"en": "Buy, service, ride", "es": "Compra, repara, rueda",
             "pt": "Compre, conserte, pedale", "it": "Compra, ripara, pedala"},
"p.shop_lead": {
 "en": "Miami's factory authorized Segway dealer. We also sell the Trikkes we are named after, electric bikes, genuine parts — and we fix all of it, including yours.",
 "es": "Distribuidor oficial de fábrica de Segway en Miami. También vendemos los Trikkes que nos dan nombre, bicis eléctricas y repuestos originales — y lo reparamos todo, incluido lo tuyo.",
 "pt": "Revendedor autorizado de fábrica da Segway em Miami. Também vendemos os Trikkes que nos dão o nome, bikes elétricas e peças originais — e consertamos tudo, inclusive o seu.",
 "it": "Rivenditore autorizzato di fabbrica Segway a Miami. Vendiamo anche i Trikke da cui prendiamo il nome, bici elettriche e ricambi originali — e ripariamo tutto, compreso il tuo."},
"p.routes_h": {"en": "Where to ride", "es": "Dónde rodar", "pt": "Onde pedalar", "it": "Dove pedalare"},
"p.routes_lead": {
 "en": "Free route guides written by people who ride this island every day. Print them, screenshot them, or grab the paper version at the shop.",
 "es": "Guías de rutas gratuitas escritas por gente que rueda esta isla todos los días. Imprímelas, hazles captura o llévate la versión en papel de la tienda.",
 "pt": "Guias de rotas gratuitos escritos por quem pedala esta ilha todo dia. Imprima, tire print ou pegue a versão em papel na loja.",
 "it": "Guide dei percorsi gratuite, scritte da chi pedala quest'isola ogni giorno. Stampale, fanne uno screenshot o prendi la versione cartacea in negozio."},
"p.about_h": {"en": "A shop, not a kiosk", "es": "Una tienda, no un quiosco",
              "pt": "Uma loja, não um quiosque", "it": "Un negozio, non un chiosco"},
"p.about_lead": {
 "en": "Real mechanics, real guides, a restroom, cold water and Wi-Fi — one block from Ocean Drive.",
 "es": "Mecánicos de verdad, guías de verdad, baño, agua fría y wifi — a una manzana de Ocean Drive.",
 "pt": "Mecânicos de verdade, guias de verdade, banheiro, água gelada e wi-fi — a um quarteirão da Ocean Drive.",
 "it": "Meccanici veri, guide vere, bagno, acqua fresca e wi-fi — a un isolato da Ocean Drive."},
"p.faq_h": {"en": "Frequently asked", "es": "Preguntas frecuentes",
            "pt": "Perguntas frequentes", "it": "Domande frequenti"},
"p.faq_lead": {
 "en": "Short answers first. If yours is not here, call us — a human picks up between 9 AM and 8 PM.",
 "es": "Respuestas cortas primero. Si la tuya no está, llámanos — contesta una persona de 9:00 a 20:00.",
 "pt": "Respostas curtas primeiro. Se a sua não estiver aqui, ligue — uma pessoa atende das 9h às 20h.",
 "it": "Prima le risposte brevi. Se la tua non c'è, chiamaci — risponde una persona dalle 9 alle 20."},
"p.contact_h": {"en": "Book your ride", "es": "Reserva tu vehículo",
                "pt": "Reserve seu veículo", "it": "Prenota il tuo mezzo"},
"p.contact_lead": {
 "en": "Fastest way is the phone. Second fastest is walking in — we are one block off Ocean Drive.",
 "es": "Lo más rápido es el teléfono. Lo segundo más rápido es venir — estamos a una manzana de Ocean Drive.",
 "pt": "O mais rápido é o telefone. O segundo mais rápido é passar aqui — estamos a um quarteirão da Ocean Drive.",
 "it": "Il modo più veloce è il telefono. Il secondo è passare di persona — siamo a un isolato da Ocean Drive."},
"p.404_h": {"en": "Wrong turn on Ocean Drive", "es": "Giro equivocado en Ocean Drive",
            "pt": "Curva errada na Ocean Drive", "it": "Svolta sbagliata su Ocean Drive"},
"p.404_lead": {"en": "That page is not here, but the bikes are.", "es": "Esa página no está aquí, pero las bicis sí.",
               "pt": "Essa página não está aqui, mas as bikes estão.", "it": "Quella pagina non c'è, ma le bici sì."},
"p.404_home": {"en": "Back home", "es": "Volver al inicio", "pt": "Voltar ao início", "it": "Torna alla home"},
"p.404_rent": {"en": "See rentals", "es": "Ver alquileres", "pt": "Ver aluguéis", "it": "Vedi i noleggi"},
})

PAGES.update({
# ===================== answer boxes (AEO) =====================
"ab.index_q": {
 "en": "Where can I rent a bike in South Beach?",
 "es": "¿Dónde puedo alquilar una bici en South Beach?",
 "pt": "Onde posso alugar uma bike em South Beach?",
 "it": "Dove posso noleggiare una bici a South Beach?"},
"ab.index_a": {
 "en": "At Miami Beach Bikes · Rentals &amp; Tours, 233 14th Street, Miami Beach, FL 33139 — one block from Ocean Drive and the Beachwalk. We are open every day from 9 AM to 8 PM, rent by the hour, day, week or month from $12/hour, run a happy hour from 1 to 4 PM that adds a free extra hour, and deliver free to South Beach hotels on rentals of 24 hours or more. Call (305) 830-9440.",
 "es": "En Miami Beach Bikes · Rentals &amp; Tours, 233 de la calle 14, Miami Beach, FL 33139 — a una manzana de Ocean Drive y del Beachwalk. Abrimos todos los días de 9:00 a 20:00, alquilamos por hora, día, semana o mes desde 12 $/hora, tenemos happy hour de 13:00 a 16:00 que añade una hora gratis, y entregamos sin coste en hoteles de South Beach en alquileres de 24 horas o más. Llama al (305) 830-9440.",
 "pt": "Na Miami Beach Bikes · Rentals &amp; Tours, 233 da rua 14, Miami Beach, FL 33139 — a um quarteirão da Ocean Drive e do Beachwalk. Abrimos todos os dias das 9h às 20h, alugamos por hora, dia, semana ou mês a partir de US$ 12/hora, temos happy hour das 13h às 16h que dá uma hora grátis, e entregamos sem custo em hotéis de South Beach em aluguéis de 24 horas ou mais. Ligue para (305) 830-9440.",
 "it": "Da Miami Beach Bikes · Rentals &amp; Tours, 233 della 14ª strada, Miami Beach, FL 33139 — a un isolato da Ocean Drive e dal Beachwalk. Siamo aperti tutti i giorni dalle 9 alle 20, noleggiamo a ore, giorni, settimane o mesi da 12 $ l'ora, abbiamo l'happy hour dalle 13 alle 16 che regala un'ora extra, e consegniamo gratis negli hotel di South Beach per noleggi di 24 ore o più. Chiama il (305) 830-9440."},
"ab.rentals_q": {
 "en": "How much does it cost to rent a bike in Miami Beach?",
 "es": "¿Cuánto cuesta alquilar una bici en Miami Beach?",
 "pt": "Quanto custa alugar uma bike em Miami Beach?",
 "it": "Quanto costa noleggiare una bici a Miami Beach?"},
"ab.rentals_a": {
 "en": "Beach cruisers start at $12 per hour and $28 for all day (9 AM to 8 PM). Fat tire beach bikes start at $18/hour, electric bikes at $25/hour, electric tandems at $45/hour, Trikkes at $25 for 30 minutes, adult tricycles at $18/hour, tandems at $22/hour, rollerblades at $12/hour and kids&#39; bikes at $10/hour. Rent between 1 PM and 4 PM and you get an extra hour free. Helmet, lock, bottled water and a route map are included with every rental.",
 "es": "Los beach cruisers empiezan en 12 $ la hora y 28 $ el día completo (de 9:00 a 20:00). Las fat tire desde 18 $/hora, las eléctricas desde 25 $/hora, los tándems eléctricos desde 45 $/hora, los Trikkes desde 25 $ por 30 minutos, los triciclos de adulto desde 18 $/hora, los tándems desde 22 $/hora, los patines desde 12 $/hora y las bicis infantiles desde 10 $/hora. Si alquilas entre las 13:00 y las 16:00 te llevas una hora extra gratis. Casco, candado, agua y mapa de rutas incluidos en cada alquiler.",
 "pt": "Os beach cruisers começam em US$ 12 por hora e US$ 28 pelo dia inteiro (das 9h às 20h). As fat tire a partir de US$ 18/hora, as elétricas a partir de US$ 25/hora, os tandems elétricos a partir de US$ 45/hora, os Trikkes a partir de US$ 25 por 30 minutos, os tricilos adultos a partir de US$ 18/hora, os tandems a partir de US$ 22/hora, os patins a partir de US$ 12/hora e as bikes infantis a partir de US$ 10/hora. Alugando entre 13h e 16h você ganha uma hora extra. Capacete, cadeado, água e mapa de rotas inclusos em cada aluguel.",
 "it": "I beach cruiser partono da 12 $ l'ora e 28 $ per la giornata intera (dalle 9 alle 20). Le fat tire da 18 $/ora, le elettriche da 25 $/ora, i tandem elettrici da 45 $/ora, i Trikke da 25 $ per 30 minuti, i tricicli per adulti da 18 $/ora, i tandem da 22 $/ora, i pattini da 12 $/ora e le bici per bambini da 10 $/ora. Noleggiando tra le 13 e le 16 ottieni un'ora extra gratis. Casco, lucchetto, acqua e mappa dei percorsi inclusi in ogni noleggio."},
"ab.tours_q": {
 "en": "What is the best guided tour in South Beach?",
 "es": "¿Cuál es el mejor tour guiado de South Beach?",
 "pt": "Qual é o melhor passeio guiado de South Beach?",
 "it": "Qual è il miglior tour guidato di South Beach?"},
"ab.tours_a": {
 "en": "Start with the one-hour Ocean Drive Segway Tour at $49 per person — the shortest, the cheapest, training included. The Star Island Segway Tour is $69 for an hour, the two-hour South Beach and Art Deco Segway Tours are $79 each, and the 2.5-hour Miami Millionaire&#39;s Row Segway Tour is $89. Bike, e-bike, Trikke, night and private tours are quoted by phone. All tours leave from 233 14th Street, Miami Beach, and Segway tours need a minimum of two riders.",
 "es": "Empieza por el tour en Segway de Ocean Drive, una hora por 49 $ por persona — el más corto, el más barato y con entrenamiento incluido. El de Star Island cuesta 69 $ por una hora, los de South Beach y Art Déco 79 $ cada uno por dos horas, y el de Millionaire's Row 89 $ por 2,5 horas. Los tours en bici, e-bike, Trikke, nocturnos y privados se cotizan por teléfono. Todos salen del 233 de la calle 14, Miami Beach, y los de Segway requieren un mínimo de dos personas.",
 "pt": "Comece pelo passeio de Segway da Ocean Drive, uma hora por US$ 49 por pessoa — o mais curto, o mais barato e com treinamento incluído. O de Star Island custa US$ 69 por uma hora, os de South Beach e Art Déco US$ 79 cada por duas horas, e o da Millionaire's Row US$ 89 por 2,5 horas. Os passeios de bike, e-bike, Trikke, noturnos e privativos são cotados por telefone. Todos saem da 233 da rua 14, Miami Beach, e os de Segway exigem no mínimo duas pessoas.",
 "it": "Comincia dal tour in Segway di Ocean Drive, un'ora a 49 $ a persona — il più breve, il più economico e con addestramento incluso. Quello di Star Island costa 69 $ per un'ora, quelli di South Beach e Art Déco 79 $ ciascuno per due ore, e quello della Millionaire's Row 89 $ per 2,5 ore. I tour in bici, e-bike, Trikke, notturni e privati si quotano al telefono. Tutti partono dal 233 della 14ª strada, Miami Beach, e quelli in Segway richiedono almeno due persone."},
"ab.adv_q": {
 "en": "What day trips can you book from South Beach?",
 "es": "¿Qué excursiones se pueden reservar desde South Beach?",
 "pt": "Quais bate-voltas dá para reservar a partir de South Beach?",
 "it": "Quali gite si possono prenotare da South Beach?"},
"ab.adv_a": {
 "en": "From our shop at 233 14th Street you can book the Everglades Airboat Adventure (4.5 hours, $69 per person, hotel pickup included), a full-day Key West trip over the Seven Mile Bridge, a half-day Miami City Tour through Little Havana and Wynwood, jet ski rentals on Biscayne Bay from $99, South Beach parasailing from $95 and helicopter rides over the city from $149. Call (305) 830-9440 to check the next departure.",
 "es": "Desde nuestra tienda del 233 de la calle 14 puedes reservar la aventura en hidrodeslizador por los Everglades (4,5 horas, 69 $ por persona, con recogida en el hotel), una excursión de día completo a Key West cruzando el Seven Mile Bridge, un city tour de Miami de media jornada por Little Havana y Wynwood, alquiler de motos de agua en la bahía de Biscayne desde 99 $, parasailing en South Beach desde 95 $ y vuelos en helicóptero sobre la ciudad desde 149 $. Llama al (305) 830-9440 para consultar la próxima salida.",
 "pt": "Na nossa loja na 233 da rua 14 você pode reservar a aventura de airboat nos Everglades (4,5 horas, US$ 69 por pessoa, com busca no hotel), um bate-volta de dia inteiro a Key West pela Seven Mile Bridge, um city tour de Miami de meio dia por Little Havana e Wynwood, aluguel de jet ski na baía de Biscayne a partir de US$ 99, parasailing em South Beach a partir de US$ 95 e voos de helicóptero sobre a cidade a partir de US$ 149. Ligue para (305) 830-9440 para ver a próxima saída.",
 "it": "Dal nostro negozio al 233 della 14ª strada puoi prenotare l'avventura in airboat nelle Everglades (4,5 ore, 69 $ a persona, ritiro in hotel incluso), una gita di un giorno intero a Key West lungo il Seven Mile Bridge, un city tour di Miami di mezza giornata tra Little Havana e Wynwood, il noleggio di moto d'acqua sulla baia di Biscayne da 99 $, il parasailing a South Beach da 95 $ e voli in elicottero sulla città da 149 $. Chiama il (305) 830-9440 per la prossima partenza."},
"ab.live_q": {
 "en": "What is a self-guided tour of South Beach?",
 "es": "¿Qué es un tour autoguiado por South Beach?",
 "pt": "O que é um passeio autoguiado por South Beach?",
 "it": "Che cos'è un tour autoguidato di South Beach?"},
"ab.live_a": {
 "en": "Live Route is a free self-guided tour of South Beach from Miami Beach Bikes at 233 14th Street. You choose how you are travelling — on foot, beach cruiser, electric bike, Segway, Trikke or skates — how much time you have, from 30 minutes to half a day, and what you want to see. It then orders the nearest landmarks into a loop, tells you the distance and riding time between each one, and in live mode uses your phone's location to announce each stop as you reach it. No app, no sign-up, no charge.",
 "es": "Ruta Viva es un tour autoguiado gratuito por South Beach de Miami Beach Bikes, en el 233 de la calle 14. Eliges cómo te mueves — a pie, en beach cruiser, bici eléctrica, Segway, Trikke o patines —, cuánto tiempo tienes, de 30 minutos a medio día, y qué quieres ver. Después ordena los puntos más cercanos en un circuito, te dice la distancia y el tiempo entre cada uno, y en modo en vivo usa la ubicación de tu móvil para anunciarte cada parada al llegar. Sin app, sin registro y sin coste.",
 "pt": "A Rota Viva é um passeio autoguiado gratuito por South Beach da Miami Beach Bikes, na 233 da rua 14. Você escolhe como está se movendo — a pé, de beach cruiser, bike elétrica, Segway, Trikke ou patins —, quanto tempo tem, de 30 minutos a meio dia, e o que quer ver. Depois ela organiza os pontos mais próximos num circuito, informa a distância e o tempo entre cada um, e no modo ao vivo usa a localização do seu celular para anunciar cada parada quando você chega. Sem app, sem cadastro e sem custo.",
 "it": "Rotta Live è un tour autoguidato gratuito di South Beach di Miami Beach Bikes, al 233 della 14ª strada. Scegli come ti muovi — a piedi, in beach cruiser, bici elettrica, Segway, Trikke o pattini —, quanto tempo hai, da 30 minuti a mezza giornata, e cosa vuoi vedere. Poi mette in fila le tappe più vicine in un anello, ti dice distanza e tempo tra una e l'altra, e in modalità dal vivo usa la posizione del telefono per annunciarti ogni tappa quando ci arrivi. Nessuna app, nessuna registrazione, nessun costo."},
"ab.shop_q": {
 "en": "Where can I buy a Segway in Miami?",
 "es": "¿Dónde puedo comprar un Segway en Miami?",
 "pt": "Onde posso comprar um Segway em Miami?",
 "it": "Dove posso comprare un Segway a Miami?"},
"ab.shop_a": {
 "en": "At Miami Beach Bikes, 233 14th Street, Miami Beach, FL 33139 — Miami's factory authorized Segway dealer. We sell new Segway personal transporters with full warranty, electric and pedal Trikkes, electric bikes and the complete Segway i2 parts range, and you can test ride before you buy. Call (305) 830-9440 for current models and pricing.",
 "es": "En Miami Beach Bikes, 233 de la calle 14, Miami Beach, FL 33139 — distribuidor oficial de fábrica de Segway en Miami. Vendemos transportadores personales Segway nuevos con garantía completa, Trikkes eléctricos y a pedal, bicis eléctricas y la gama completa de repuestos Segway i2, y puedes probarlo antes de comprar. Llama al (305) 830-9440 para modelos y precios actuales.",
 "pt": "Na Miami Beach Bikes, 233 da rua 14, Miami Beach, FL 33139 — revendedor autorizado de fábrica da Segway em Miami. Vendemos transportadores pessoais Segway novos com garantia completa, Trikkes elétricos e a pedal, bikes elétricas e a linha completa de peças Segway i2, e você pode testar antes de comprar. Ligue para (305) 830-9440 para modelos e preços atuais.",
 "it": "Da Miami Beach Bikes, 233 della 14ª strada, Miami Beach, FL 33139 — rivenditore autorizzato di fabbrica Segway a Miami. Vendiamo trasportatori personali Segway nuovi con garanzia completa, Trikke elettrici e a pedali, bici elettriche e la gamma completa di ricambi Segway i2, e puoi provarlo prima di comprare. Chiama il (305) 830-9440 per modelli e prezzi aggiornati."},
"ab.routes_q": {
 "en": "Where is the best place to bike in Miami Beach?",
 "es": "¿Cuál es el mejor sitio para ir en bici en Miami Beach?",
 "pt": "Qual é o melhor lugar para andar de bike em Miami Beach?",
 "it": "Qual è il posto migliore per andare in bici a Miami Beach?"},
"ab.routes_a": {
 "en": "The Miami Beach Beachwalk — a flat, paved, car-free path running along the sand from South Pointe Park to North Beach — is the best ride on the island for all ages. For skyline views, cross the Venetian Causeway to the Venetian Islands; for mansions, take the protected path on the MacArthur Causeway to Star Island; and for street art, ride an e-bike to Wynwood. All four start within a block of 233 14th Street.",
 "es": "El Beachwalk de Miami Beach — un camino llano, asfaltado y sin coches que recorre la arena desde South Pointe Park hasta North Beach — es el mejor paseo de la isla para todas las edades. Para vistas del skyline, cruza el Venetian Causeway hasta las Venetian Islands; para mansiones, toma el carril protegido del MacArthur Causeway hasta Star Island; y para arte urbano, ve en e-bike a Wynwood. Los cuatro empiezan a menos de una manzana del 233 de la calle 14.",
 "pt": "O Beachwalk de Miami Beach — um caminho plano, asfaltado e sem carros que percorre a areia do South Pointe Park até North Beach — é o melhor passeio da ilha para todas as idades. Para vistas do skyline, cruze a Venetian Causeway até as Venetian Islands; para mansões, pegue a ciclovia protegida da MacArthur Causeway até Star Island; e para arte de rua, vá de e-bike até Wynwood. Os quatro começam a menos de um quarteirão da 233 da rua 14.",
 "it": "Il Beachwalk di Miami Beach — un percorso piatto, asfaltato e senza auto che corre lungo la sabbia da South Pointe Park a North Beach — è la pedalata migliore dell'isola per tutte le età. Per lo skyline, attraversa la Venetian Causeway fino alle Venetian Islands; per le ville, prendi la pista protetta della MacArthur Causeway fino a Star Island; e per la street art, vai in e-bike a Wynwood. Tutti e quattro partono a meno di un isolato dal 233 della 14ª strada."},
})
