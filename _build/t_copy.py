# -*- coding: utf-8 -*-
"""
Page copy that lives inside build.py's templates.

Three layers already existed — i18n.py for interface strings, pages_i18n.py
for titles and H1s, content.py for the catalogue — and between them they left
the section headings, the step-by-step copy, the trust blocks and every CTA
band in English on the Spanish, Portuguese and Italian pages. A browser sweep
over 30 translated pages found 184 of them.

Rather than thread a call through a hundred f-strings, the English page is
rendered first and each of these strings is swapped on the way out. The keys
are the English source, verbatim; `build.py` reports any key it never matched,
so a reworded template shows up as a stale entry instead of silently going
back to English.

Proper nouns stay put: Ocean Drive, Española Way, Lummus, South Pointe,
Wynwood, the Beachwalk, Segway, Trikke, Live Route's landmark names.
"""

COPY = {}


def add(en, es, pt, it):
    COPY[en] = {"es": es, "pt": pt, "it": it}


# ---------------------------------------------------------------- home page
add("What do you want to ride?",
    "¿Qué quieres conducir?",
    "O que você quer pilotar?",
    "Cosa vuoi guidare?")
add("Anything with wheels", "Cualquier cosa con ruedas",
    "Qualquer coisa com rodas", "Qualsiasi cosa con le ruote")
add("When", "Cuándo", "Quando", "Quando")
add("New · free for everyone", "Nuevo · gratis para todos",
    "Novo · grátis para todos", "Nuovo · gratis per tutti")
add("Live Route: a tour guide in your pocket",
    "Ruta Viva: un guía turístico en tu bolsillo",
    "Rota Ao Vivo: um guia turístico no seu bolso",
    "Percorso Live: una guida turistica in tasca")
add("Tell it how you are moving, how long you have and what you like. It builds a route "
    "from our door on Washington and 14th through the South Beach worth seeing — Española "
    "Way, the Versace Mansion, the Lummus lifeguard towers, South Pointe — then guides you "
    "stop by stop while you ride, using your phone's location.",
    "Dile cómo te mueves, cuánto tiempo tienes y qué te gusta. Arma una ruta desde nuestra "
    "puerta en Washington con la 14 por el South Beach que vale la pena — Española Way, la "
    "Mansión Versace, las torres de socorristas de Lummus, South Pointe — y luego te guía "
    "parada por parada mientras pedaleas, usando la ubicación de tu móvil.",
    "Diga como você está se locomovendo, quanto tempo tem e do que gosta. Ele monta uma rota "
    "a partir da nossa porta na Washington com a rua 14 pela South Beach que vale a pena — "
    "Española Way, a Mansão Versace, as torres de salva-vidas de Lummus, South Pointe — e "
    "depois te guia parada por parada enquanto você pedala, usando a localização do celular.",
    "Dille come ti stai muovendo, quanto tempo hai e cosa ti piace. Costruisce un percorso "
    "dalla nostra porta tra Washington e la 14ª attraverso la South Beach che vale — Española "
    "Way, la Villa Versace, le torrette dei bagnini di Lummus, South Pointe — e poi ti guida "
    "tappa dopo tappa mentre pedali, usando la posizione del telefono.")
add("The fleet", "La flota", "A frota", "La flotta")
add("Pick your wheels", "Elige tus ruedas", "Escolha suas rodas", "Scegli le tue ruote")
add("Every rental comes with a helmet, a lock, cold water and a printed route map. "
    "Rent from one hour to sixty days.",
    "Cada alquiler incluye casco, candado, agua fría y un mapa de rutas impreso. "
    "Alquila desde una hora hasta sesenta días.",
    "Todo aluguel vem com capacete, cadeado, água gelada e um mapa de rotas impresso. "
    "Alugue de uma hora até sessenta dias.",
    "Ogni noleggio include casco, lucchetto, acqua fresca e una mappa dei percorsi stampata. "
    "Noleggia da un'ora fino a sessanta giorni.")
add("Someone who actually knows the island",
    "Alguien que de verdad conoce la isla",
    "Alguém que conhece a ilha de verdade",
    "Qualcuno che l'isola la conosce davvero")
add("Our guides grew up on this sand. One hour on Ocean Drive for $49, or 2.5 hours up "
    "Millionaire’s Row for $89 — you get the neon, the mansions and the stories behind them, "
    "at a pace that works for grandparents and fourteen-year-olds alike.",
    "Nuestros guías crecieron en esta arena. Una hora por Ocean Drive por 49 $, o 2,5 horas "
    "por Millionaire’s Row por 89 $: te llevas el neón, las mansiones y las historias que hay "
    "detrás, a un ritmo que va igual de bien a los abuelos que a los de catorce.",
    "Nossos guias cresceram nesta areia. Uma hora na Ocean Drive por US$ 49, ou 2,5 horas pela "
    "Millionaire’s Row por US$ 89: você leva o neon, as mansões e as histórias por trás delas, "
    "num ritmo que serve tanto para os avós quanto para os de catorze anos.",
    "Le nostre guide sono cresciute su questa sabbia. Un'ora su Ocean Drive a 49 $, oppure 2,5 "
    "ore lungo Millionaire’s Row a 89 $: ti porti a casa il neon, le ville e le storie che ci "
    "stanno dietro, a un ritmo che va bene ai nonni come ai quattordicenni.")
add("Segway tour from", "Tour en Segway desde", "Passeio de Segway a partir de",
    "Tour in Segway da")
add("Browse every tour", "Ver todos los tours", "Ver todos os passeios", "Vedi tutti i tour")
add("Start with one of these three", "Empieza por uno de estos tres",
    "Comece por um destes três", "Inizia da uno di questi tre")
add("Beyond the island", "Más allá de la isla", "Para além da ilha", "Oltre l'isola")
add("Airboats, the Keys, jet skis and a helicopter",
    "Hidrodeslizadores, los Cayos, motos acuáticas y un helicóptero",
    "Aerobarcos, os Keys, jet skis e um helicóptero",
    "Airboat, le Keys, moto d'acqua e un elicottero")
add("Book the whole of South Florida at the same counter where you pick up your bike. "
    "Most day trips include hotel pickup.",
    "Reserva todo el sur de Florida en el mismo mostrador donde recoges la bici. "
    "La mayoría de las excursiones incluyen recogida en el hotel.",
    "Reserve todo o sul da Flórida no mesmo balcão onde você pega a bike. "
    "A maioria dos bate-voltas inclui busca no hotel.",
    "Prenota tutta la Florida del sud allo stesso bancone dove ritiri la bici. "
    "Quasi tutte le gite includono il ritiro in hotel.")
add("Call to book", "Llama para reservar", "Ligue para reservar", "Chiama per prenotare")
add("Wheels under you in ten minutes", "Con ruedas debajo en diez minutos",
    "Com rodas embaixo em dez minutos", "In sella in dieci minuti")
add("Pick your ride", "Elige tu vehículo", "Escolha seu veículo", "Scegli il mezzo")
add("Choose online, call us, or just walk in — we are one block off Ocean Drive and we keep "
    "spare bikes for walk-ups all day.",
    "Elige por internet, llámanos o entra sin más: estamos a una cuadra de Ocean Drive y "
    "guardamos bicis libres para quien llega sin reserva, todo el día.",
    "Escolha pela internet, ligue ou simplesmente entre: estamos a um quarteirão da Ocean Drive "
    "e guardamos bikes livres para quem chega sem reserva, o dia todo.",
    "Scegli online, chiamaci o entra e basta: siamo a un isolato da Ocean Drive e teniamo bici "
    "libere per chi arriva senza prenotare, tutto il giorno.")
add("Get fitted", "Te la ajustamos", "Ajuste na medida", "Regolazione su misura")
add("Seat height, helmet, lock and a two-minute safety brief. Segway riders get a full "
    "training session on the spot.",
    "Altura del sillín, casco, candado y dos minutos de instrucciones de seguridad. Quien va "
    "en Segway recibe una sesión de entrenamiento completa allí mismo.",
    "Altura do selim, capacete, cadeado e dois minutos de orientações de segurança. Quem vai de "
    "Segway recebe um treinamento completo ali mesmo.",
    "Altezza sella, casco, lucchetto e due minuti di istruzioni di sicurezza. Chi va in Segway "
    "riceve una sessione di addestramento completa sul posto.")
add("Take the map", "Llévate el mapa", "Leve o mapa", "Prendi la mappa")
add("We mark the best route for your time, your legs and the day's wind, and we stay reachable "
    "by phone while you ride.",
    "Marcamos la mejor ruta según tu tiempo, tus piernas y el viento del día, y seguimos "
    "localizables por teléfono mientras pedaleas.",
    "Marcamos a melhor rota para o seu tempo, as suas pernas e o vento do dia, e continuamos "
    "disponíveis por telefone enquanto você pedala.",
    "Segniamo il percorso migliore per il tuo tempo, le tue gambe e il vento del giorno, e "
    "restiamo raggiungibili al telefono mentre pedali.")
add("Roll back in", "Vuelve rodando", "Volte pedalando", "Torna pedalando")
add("Return to the shop or leave it at your hotel — for 24-hour rentals in South Beach we come "
    "and get it, free.",
    "Devuélvela en la tienda o déjala en tu hotel: en alquileres de 24 horas en South Beach "
    "vamos nosotros a recogerla, gratis.",
    "Devolva na loja ou deixe no hotel: em aluguéis de 24 horas em South Beach nós buscamos, "
    "de graça.",
    "Riportala in negozio o lasciala in hotel: sui noleggi di 24 ore a South Beach veniamo noi "
    "a ritirarla, gratis.")
add("Free route guides", "Guías de rutas gratis", "Guias de rotas grátis",
    "Guide dei percorsi gratis")
add("Where to actually ride", "Dónde rodar de verdad", "Onde pedalar de verdade",
    "Dove pedalare davvero")
add("South Beach is flat, compact and laced with protected bike lanes plus a car-free Beachwalk "
    "that runs the length of the sand. These are the routes we hand our own friends.",
    "South Beach es llano, compacto y está lleno de carriles bici protegidos, más el Beachwalk "
    "sin coches que recorre toda la arena. Estas son las rutas que les damos a nuestros amigos.",
    "South Beach é plano, compacto e cheio de ciclovias protegidas, além do Beachwalk sem carros "
    "que acompanha toda a areia. Estas são as rotas que damos aos nossos amigos.",
    "South Beach è piatta, compatta e piena di piste ciclabili protette, più il Beachwalk senza "
    "auto che corre lungo tutta la sabbia. Questi sono i percorsi che diamo ai nostri amici.")
add("4.8 stars from 131 riders", "4,8 estrellas de 131 ciclistas",
    "4,8 estrelas de 131 ciclistas", "4,8 stelle da 131 ciclisti")
add("Families, couples, cruise-ship day-trippers and locals who just need a tune-up.",
    "Familias, parejas, gente de crucero por el día y vecinos que solo necesitan una puesta a punto.",
    "Famílias, casais, gente de cruzeiro passando o dia e vizinhos que só precisam de uma revisão.",
    "Famiglie, coppie, gente in escursione dalla nave e residenti che vogliono solo una messa a punto.")


# ------------------------------------------------------------------ the CTA bands
add("Ready when you are", "Cuando tú quieras", "Quando você quiser", "Quando vuoi tu")
add("Your bike is already waiting on 14th Street",
    "Tu bici ya te está esperando en la calle 14",
    "Sua bike já está esperando na rua 14",
    "La tua bici ti aspetta già in 14ª strada")
add("Walk in any day between 9 AM and 8 PM, or reserve ahead and we will have it fitted and "
    "ready when you arrive.",
    "Pásate cualquier día entre las 9:00 y las 20:00, o reserva antes y la tendremos ajustada "
    "y lista cuando llegues.",
    "Apareça qualquer dia entre 9h e 20h, ou reserve antes e a deixamos ajustada e pronta "
    "quando você chegar.",
    "Passa un giorno qualsiasi tra le 9 e le 20, oppure prenota e te la troviamo regolata e "
    "pronta al tuo arrivo.")
add("Reserve your wheels for tomorrow morning",
    "Reserva tus ruedas para mañana por la mañana",
    "Reserve suas rodas para amanhã de manhã",
    "Prenota le tue ruote per domani mattina")
add("Tell us the day, the hours and how many of you there are. We will have everything fitted "
    "and waiting at 233 14th Street.",
    "Dinos el día, las horas y cuántos sois. Lo tendremos todo ajustado y esperando en el 233 "
    "de la calle 14.",
    "Diga o dia, as horas e quantos são. Deixamos tudo ajustado e esperando no 233 da rua 14.",
    "Dicci il giorno, le ore e in quanti siete. Troverete tutto regolato e pronto al 233 della "
    "14ª strada.")
add("Pick a departure and we will hold your spot",
    "Elige una salida y te guardamos el sitio",
    "Escolha uma saída e guardamos o seu lugar",
    "Scegli una partenza e ti teniamo il posto")
add("Tours fill fastest between December and April and on weekends. Reserve by phone, email "
    "or at the shop.",
    "Los tours se llenan antes entre diciembre y abril y los fines de semana. Reserva por "
    "teléfono, por email o en la tienda.",
    "Os passeios enchem mais rápido entre dezembro e abril e nos fins de semana. Reserve por "
    "telefone, e-mail ou na loja.",
    "I tour si riempiono prima tra dicembre e aprile e nei weekend. Prenota per telefono, via "
    "email o in negozio.")
add("Airboat in the morning, cruiser in the afternoon",
    "Hidrodeslizador por la mañana, cruiser por la tarde",
    "Aerobarco de manhã, cruiser de tarde",
    "Airboat la mattina, cruiser il pomeriggio")
add("Book the adventure and the bike in the same conversation. We will line up the times so "
    "nothing overlaps.",
    "Reserva la aventura y la bici en la misma conversación. Cuadramos los horarios para que "
    "nada se solape.",
    "Reserve a aventura e a bike na mesma conversa. Ajustamos os horários para nada se "
    "sobrepor.",
    "Prenota l'avventura e la bici nella stessa conversazione. Incastriamo noi gli orari perché "
    "non si sovrappongano.")
add("Tell us what you are looking for", "Dinos qué estás buscando",
    "Diga o que você está procurando", "Dicci cosa stai cercando")
add("Models, availability and pricing change with the season. One phone call and we will tell "
    "you exactly what is on the floor today.",
    "Los modelos, la disponibilidad y los precios cambian con la temporada. Una llamada y te "
    "decimos exactamente qué hay hoy en tienda.",
    "Modelos, disponibilidade e preços mudam com a temporada. Um telefonema e dizemos "
    "exatamente o que está na loja hoje.",
    "Modelli, disponibilità e prezzi cambiano con la stagione. Una telefonata e ti diciamo "
    "esattamente cosa c'è oggi in negozio.")
add("No bike? The route still works on foot",
    "¿Sin bici? La ruta funciona igual a pie",
    "Sem bike? A rota funciona a pé do mesmo jeito",
    "Niente bici? Il percorso funziona anche a piedi")
add("Walking covers the deco strip fine. For South Pointe, the Venetian Islands or Wynwood you "
    "will want wheels — we are at the start line either way.",
    "A pie se cubre bien la franja déco. Para South Pointe, las Venetian Islands o Wynwood vas "
    "a querer ruedas: de un modo u otro, estamos en la línea de salida.",
    "A pé dá para cobrir bem a faixa déco. Para South Pointe, as Venetian Islands ou Wynwood "
    "você vai querer rodas: de um jeito ou de outro, estamos na linha de largada.",
    "A piedi la striscia déco si copre bene. Per South Pointe, le Venetian Islands o Wynwood "
    "vorrai le ruote: in ogni caso, siamo noi la linea di partenza.")
add("Pick a route. We will hand you the bike.",
    "Elige una ruta. Nosotros te damos la bici.",
    "Escolha uma rota. A bike damos nós.",
    "Scegli un percorso. La bici te la diamo noi.")
add("Walk in at 233 14th Street and tell us how many hours you have — we will match the route "
    "to your legs and the day's wind.",
    "Pásate por el 233 de la calle 14 y dinos cuántas horas tienes: ajustamos la ruta a tus "
    "piernas y al viento del día.",
    "Apareça no 233 da rua 14 e diga quantas horas você tem: ajustamos a rota às suas pernas e "
    "ao vento do dia.",
    "Passa al 233 della 14ª strada e dicci quante ore hai: adattiamo il percorso alle tue gambe "
    "e al vento del giorno.")
add("Come say hi at 233 14th Street", "Pásate a saludar al 233 de la calle 14",
    "Venha dar um oi no 233 da rua 14", "Vieni a salutarci al 233 della 14ª strada")
add("Still not sure which ride is right?", "¿Aún no sabes cuál te conviene?",
    "Ainda não sabe qual é o certo para você?", "Non sai ancora quale fa per te?")
add("Tell us who is riding, how long you have and what you want to see. We will pick it for "
    "you in one phone call.",
    "Dinos quién va a rodar, cuánto tiempo tienes y qué quieres ver. Lo elegimos por ti en una "
    "llamada.",
    "Diga quem vai pedalar, quanto tempo você tem e o que quer ver. Escolhemos por você em um "
    "telefonema.",
    "Dicci chi pedala, quanto tempo hai e cosa vuoi vedere. Lo scegliamo noi in una telefonata.")
add("Same-day rental? Just call.", "¿Alquiler para hoy mismo? Llama y ya.",
    "Aluguel para hoje? É só ligar.", "Noleggio per oggi stesso? Basta chiamare.")
add("We keep walk-in bikes on the rack all day, every day. Ten minutes from hello to riding.",
    "Guardamos bicis libres en el perchero todo el día, todos los días. Diez minutos desde el "
    "hola hasta rodar.",
    "Guardamos bikes livres no suporte o dia todo, todos os dias. Dez minutos do oi até pedalar.",
    "Teniamo bici libere in rastrelliera tutto il giorno, tutti i giorni. Dieci minuti dal "
    "saluto alla pedalata.")
add("Book online", "Reservar online", "Reservar online", "Prenota online")
add("Call ", "Llamar al ", "Ligar para ", "Chiama il ")


# --------------------------------------------------------------- rentals page
add("All prices in US dollars. The longer you ride, the less it costs — a week runs about the "
    "same as three single days.",
    "Todos los precios en dólares estadounidenses. Cuanto más ruedas, menos cuesta: una semana "
    "sale más o menos como tres días sueltos.",
    "Todos os preços em dólares americanos. Quanto mais você pedala, menos custa: uma semana "
    "sai mais ou menos como três diárias avulsas.",
    "Tutti i prezzi in dollari americani. Più pedali, meno costa: una settimana viene più o "
    "meno come tre giornate singole.")
add("Rental rates for bikes, electric bikes, Segways, skates and tricycles in Miami Beach",
    "Tarifas de alquiler de bicis, bicis eléctricas, Segways, patines y triciclos en Miami Beach",
    "Tarifas de aluguel de bikes, bikes elétricas, Segways, patins e triciclos em Miami Beach",
    "Tariffe di noleggio di bici, bici elettriche, Segway, pattini e tricicli a Miami Beach")
add("Ask at the shop", "Pregunta en la tienda", "Pergunte na loja", "Chiedi in negozio")
add("Monthly and seasonal rates available on request. Group of 6 or more? Call (305) 830-9440 "
    "for group pricing.",
    "Tarifas mensuales y de temporada bajo petición. ¿Grupo de 6 o más? Llama al (305) 830-9440 "
    "para precio de grupo.",
    "Tarifas mensais e de temporada sob consulta. Grupo de 6 ou mais? Ligue para (305) 830-9440 "
    "para preço de grupo.",
    "Tariffe mensili e stagionali su richiesta. Gruppo di 6 o più? Chiama il (305) 830-9440 per "
    "il prezzo di gruppo.")
add("Hotel delivery", "Entrega en el hotel", "Entrega no hotel", "Consegna in hotel")
add("Free across South Beach on rentals of 24 hours or more. Mid-Beach, North Beach and "
    "Downtown by flat fee.",
    "Gratis por todo South Beach en alquileres de 24 horas o más. Mid-Beach, North Beach y "
    "Downtown con tarifa fija.",
    "Grátis por toda South Beach em aluguéis de 24 horas ou mais. Mid-Beach, North Beach e "
    "Downtown com taxa fixa.",
    "Gratis in tutta South Beach sui noleggi di 24 ore o più. Mid-Beach, North Beach e Downtown "
    "con tariffa fissa.")
add("Flats, brakes, gears, batteries and full tune-ups for bikes, e-bikes and scooters. Most "
    "walk-ins same day.",
    "Pinchazos, frenos, cambios, baterías y puestas a punto completas para bicis, e-bikes y "
    "patinetes. Casi todo el mismo día.",
    "Furos, freios, marchas, baterias e revisões completas para bikes, e-bikes e patinetes. "
    "Quase tudo no mesmo dia.",
    "Forature, freni, cambi, batterie e tagliandi completi per bici, e-bike e monopattini. "
    "Quasi tutto in giornata.")
add("Baby seats, trailers, training wheels and tandems, so nobody stays behind at the hotel.",
    "Sillitas, remolques, ruedines y tándems, para que nadie se quede en el hotel.",
    "Cadeirinhas, carretinhas, rodinhas e tandems, para ninguém ficar no hotel.",
    "Seggiolini, rimorchi, rotelle e tandem, così nessuno resta in hotel.")
add("Extend from your phone", "Amplía desde el móvil", "Estenda pelo celular",
    "Prolunga dal telefono")
add("Running long? Open the assistant, enter your ticket number and add an hour, a day or a "
    "week — paid on your phone, no ride back.",
    "¿Se te alarga? Abre el asistente, mete tu número de ticket y añade una hora, un día o una "
    "semana: se paga desde el móvil, sin volver pedaleando.",
    "Passou do tempo? Abra o assistente, digite o número do seu ticket e adicione uma hora, um "
    "dia ou uma semana: paga pelo celular, sem voltar pedalando.",
    "Ti stai dilungando? Apri l'assistente, inserisci il numero del biglietto e aggiungi un'ora, "
    "un giorno o una settimana: si paga dal telefono, senza tornare indietro.")

# ------------------------------------------------------------------ tours page
add("Your route · Your pace · Photo stops · Optional guide car",
    "Tu ruta · Tu ritmo · Paradas para fotos · Coche guía opcional",
    "Sua rota · Seu ritmo · Paradas para fotos · Carro-guia opcional",
    "Il tuo percorso · Il tuo ritmo · Soste per le foto · Auto guida opzionale")
add("Included on every tour", "Incluido en todos los tours",
    "Incluído em todos os passeios", "Incluso in ogni tour")
add("You bring sunscreen. We bring the rest.",
    "Tú pones el protector solar. El resto lo ponemos nosotros.",
    "Você leva o protetor solar. O resto levamos nós.",
    "Tu porti la crema solare. Il resto lo portiamo noi.")
add("Training first", "Primero, entrenamiento", "Primeiro, treinamento",
    "Prima l'addestramento")
add("Nobody rolls out until they are comfortable. Segway riders get a full supervised practice "
    "session.",
    "Nadie sale hasta estar cómodo. Quien va en Segway hace una sesión de práctica supervisada "
    "completa.",
    "Ninguém sai antes de estar confortável. Quem vai de Segway faz uma sessão de prática "
    "supervisionada completa.",
    "Nessuno parte prima di sentirsi a proprio agio. Chi va in Segway fa una sessione di pratica "
    "assistita completa.")
add("Fitted helmet, water and a radio-free small group so you can actually hear the guide.",
    "Casco a tu medida, agua y un grupo pequeño sin radios para que oigas de verdad al guía.",
    "Capacete na medida, água e um grupo pequeno sem rádios para você realmente ouvir o guia.",
    "Casco su misura, acqua e un gruppo piccolo senza radioline, così la guida la senti davvero.")
add("Built into every route — Ocean Drive, the Star Island gate and South Pointe Pier at "
    "minimum.",
    "Van en todas las rutas: como mínimo Ocean Drive, la entrada de Star Island y el South "
    "Pointe Pier.",
    "Estão em todas as rotas: no mínimo Ocean Drive, o portão de Star Island e o South Pointe "
    "Pier.",
    "Ci sono in ogni percorso: come minimo Ocean Drive, il cancello di Star Island e il South "
    "Pointe Pier.")
add("Guides switch between English, Spanish and Portuguese. Private groups on request.",
    "Los guías alternan entre inglés, español y portugués. Grupos privados bajo petición.",
    "Os guias alternam entre inglês, espanhol e português. Grupos privativos sob consulta.",
    "Le guide passano da inglese a spagnolo e portoghese. Gruppi privati su richiesta.")
add("Every departure &amp; price", "Todas las salidas y precios",
    "Todas as saídas e preços", "Tutte le partenze e i prezzi")
add("Guided tour options and prices in Miami Beach",
    "Opciones y precios de tours guiados en Miami Beach",
    "Opções e preços de passeios guiados em Miami Beach",
    "Opzioni e prezzi dei tour guidati a Miami Beach")
add("Call for price", "Consultar precio", "Consultar preço", "Chiedi il prezzo")
add("Segway tours run on fixed departure times, require a minimum of two riders and must be "
    "booked ahead. No deposit is taken at booking or in store. Private and corporate groups "
    "welcome — call (305) 830-9440.",
    "Los tours en Segway tienen horarios de salida fijos, requieren un mínimo de dos personas y "
    "hay que reservarlos con antelación. No se cobra depósito ni al reservar ni en tienda. "
    "Grupos privados y de empresa bienvenidos: llama al (305) 830-9440.",
    "Os passeios de Segway têm horários fixos de saída, exigem no mínimo duas pessoas e precisam "
    "ser reservados com antecedência. Não cobramos caução na reserva nem na loja. Grupos "
    "privativos e corporativos são bem-vindos: ligue para (305) 830-9440.",
    "I tour in Segway hanno orari di partenza fissi, richiedono minimo due persone e vanno "
    "prenotati in anticipo. Nessuna cauzione né alla prenotazione né in negozio. Gruppi privati "
    "e aziendali benvenuti: chiama il (305) 830-9440.")
add("Before you book", "Antes de reservar", "Antes de reservar", "Prima di prenotare")


# ------------------------------------------------------------- adventures page
add("On the water", "En el agua", "Na água", "Sull'acqua")
add("In the air", "En el aire", "No ar", "In cielo")
add("One counter, the whole of South Florida",
    "Un mostrador, todo el sur de Florida",
    "Um balcão, todo o sul da Flórida",
    "Un bancone, tutta la Florida del sud")
add("Book it where you rent your bike", "Resérvalo donde alquilas la bici",
    "Reserve onde você aluga a bike", "Prenotalo dove noleggi la bici")
add("We have been sending people to the Everglades and the Keys for as long as we have been "
    "renting cruisers. Same shop, same phone number, same people if anything goes sideways.",
    "Llevamos mandando gente a los Everglades y a los Cayos desde que alquilamos cruisers. La "
    "misma tienda, el mismo teléfono y la misma gente si algo se tuerce.",
    "Mandamos gente para os Everglades e os Keys desde que alugamos cruisers. A mesma loja, o "
    "mesmo telefone e as mesmas pessoas se algo der errado.",
    "Mandiamo gente alle Everglades e alle Keys da quando noleggiamo cruiser. Stesso negozio, "
    "stesso numero, stesse persone se qualcosa va storto.")
add("Hotel pickup", "Recogida en el hotel", "Busca no hotel", "Ritiro in hotel")
add("Day trips and adventures include pickup across South Beach and Mid-Beach. Tell us the "
    "hotel, we handle the rest.",
    "Las excursiones y aventuras incluyen recogida por South Beach y Mid-Beach. Dinos el hotel "
    "y del resto nos ocupamos nosotros.",
    "Os bate-voltas e as aventuras incluem busca por South Beach e Mid-Beach. Diga o hotel, do "
    "resto cuidamos nós.",
    "Gite e avventure includono il ritiro in tutta South Beach e Mid-Beach. Dicci l'hotel, al "
    "resto pensiamo noi.")
add("Segway PT tours require no deposit at booking or in store. Everything else is pre-paid in "
    "US dollars.",
    "Los tours en Segway PT no requieren depósito ni al reservar ni en tienda. Todo lo demás se "
    "paga por adelantado en dólares estadounidenses.",
    "Os passeios de Segway PT não exigem caução na reserva nem na loja. Todo o resto é pago "
    "antecipadamente em dólares americanos.",
    "I tour in Segway PT non richiedono cauzione né alla prenotazione né in negozio. Tutto il "
    "resto si paga in anticipo in dollari americani.")
add("English, Spanish and Portuguese at the counter and, on most departures, with the guide too.",
    "Inglés, español y portugués en el mostrador y, en casi todas las salidas, también con el guía.",
    "Inglês, espanhol e português no balcão e, na maioria das saídas, com o guia também.",
    "Inglese, spagnolo e portoghese al bancone e, quasi sempre, anche con la guida.")
add("Between 9 AM and 8 PM, every day, (305) 830-9440 reaches the shop. Not a call centre.",
    "De 9:00 a 20:00, todos los días, el (305) 830-9440 suena en la tienda. No es un call center.",
    "Das 9h às 20h, todos os dias, o (305) 830-9440 toca na loja. Não é um call center.",
    "Dalle 9 alle 20, tutti i giorni, il (305) 830-9440 squilla in negozio. Non è un call center.")
add("Every option &amp; price", "Todas las opciones y precios",
    "Todas as opções e preços", "Tutte le opzioni e i prezzi")
add("Adventure and day trip options and prices",
    "Opciones y precios de aventuras y excursiones",
    "Opções e preços de aventuras e bate-voltas",
    "Opzioni e prezzi di avventure e gite")
add("Departures are seasonal and weather-dependent. Named storms are always refunded or "
    "rescheduled. Call (305) 830-9440 for today's availability.",
    "Las salidas son de temporada y dependen del tiempo. Las tormentas con nombre siempre se "
    "reembolsan o se reprograman. Llama al (305) 830-9440 para la disponibilidad de hoy.",
    "As saídas são sazonais e dependem do tempo. Tempestades nomeadas sempre têm reembolso ou "
    "remarcação. Ligue para (305) 830-9440 para a disponibilidade de hoje.",
    "Le partenze sono stagionali e dipendono dal meteo. Le tempeste con nome vengono sempre "
    "rimborsate o riprogrammate. Chiama il (305) 830-9440 per la disponibilità di oggi.")

# ----------------------------------------------------------------- Live Route
add("Open the assistant", "Abre el asistente", "Abra o assistente", "Apri l'assistente")
add("Three questions and it builds your route. It opens in its own window so the plan stays in "
    "one place while you ride — nothing mixed in with the rest of the site.",
    "Tres preguntas y te arma la ruta. Se abre en su propia ventana para que el plan quede en "
    "un solo sitio mientras ruedas, sin mezclarse con el resto de la página.",
    "Três perguntas e ele monta a sua rota. Abre em uma janela própria para o plano ficar em um "
    "lugar só enquanto você pedala, sem se misturar com o resto do site.",
    "Tre domande e ti costruisce il percorso. Si apre in una finestra sua, così il piano resta "
    "in un posto solo mentre pedali, senza mescolarsi al resto del sito.")
add("How you move", "Cómo te mueves", "Como você se move", "Come ti muovi")
add("How long you have", "Cuánto tiempo tienes", "Quanto tempo você tem", "Quanto tempo hai")
add("What you like", "Qué te gusta", "Do que você gosta", "Cosa ti piace")
add("Free · no app · no sign-up · works in any phone browser",
    "Gratis · sin app · sin registro · funciona en cualquier navegador móvil",
    "Grátis · sem app · sem cadastro · funciona em qualquer navegador de celular",
    "Gratis · senza app · senza registrazione · funziona in qualsiasi browser")
add("A guide in your pocket, not a group to keep up with",
    "Un guía en el bolsillo, no un grupo al que seguir el paso",
    "Um guia no bolso, não um grupo para acompanhar",
    "Una guida in tasca, non un gruppo da rincorrere")
add("Pick your three", "Elige tus tres", "Escolha seus três", "Scegli i tuoi tre")
add("Vehicle, time, interests. Six ways to travel, four time budgets, ten things to be into — "
    "the combinations land in the hundreds.",
    "Vehículo, tiempo, intereses. Seis formas de moverte, cuatro franjas de tiempo y diez cosas "
    "que te pueden gustar: las combinaciones se cuentan por cientos.",
    "Veículo, tempo, interesses. Seis formas de se locomover, quatro faixas de tempo e dez "
    "coisas de que gostar: as combinações passam das centenas.",
    "Mezzo, tempo, interessi. Sei modi di muoversi, quattro fasce di tempo e dieci cose che "
    "possono piacerti: le combinazioni sono centinaia.")
add("We order the stops", "Ordenamos las paradas", "Ordenamos as paradas",
    "Mettiamo in ordine le tappe")
add("It takes the landmarks that match, orders them by what is actually nearest, and only keeps "
    "what fits your clock — including the ride back to us.",
    "Coge los lugares que encajan, los ordena por cercanía real y solo se queda con lo que cabe "
    "en tu reloj, incluida la vuelta hasta nosotros.",
    "Ele pega os pontos que combinam, ordena pelo que é de fato mais perto e só mantém o que "
    "cabe no seu relógio, incluindo a volta até nós.",
    "Prende i luoghi che corrispondono, li ordina per vicinanza reale e tiene solo quello che "
    "sta nel tuo orologio, ritorno da noi compreso.")
add("Ride it live", "Hazla en vivo", "Faça ao vivo", "Fallo in diretta")
add("Live mode uses your phone's location to show the distance and direction to the next stop, "
    "and flips over when you arrive.",
    "El modo en vivo usa la ubicación de tu móvil para mostrarte distancia y dirección hasta la "
    "siguiente parada, y pasa a la siguiente cuando llegas.",
    "O modo ao vivo usa a localização do celular para mostrar a distância e a direção até a "
    "próxima parada, e vira quando você chega.",
    "La modalità live usa la posizione del telefono per mostrarti distanza e direzione verso la "
    "tappa successiva, e gira pagina quando arrivi.")
add("Or just open Maps", "O abre Maps y ya", "Ou abra o Maps e pronto",
    "Oppure apri Maps e basta")
add("One tap sends the whole loop to Google Maps for turn-by-turn, if you would rather have a "
    "voice in your ear.",
    "Un toque manda el circuito entero a Google Maps para navegación paso a paso, si prefieres "
    "una voz al oído.",
    "Um toque manda o circuito inteiro para o Google Maps com navegação passo a passo, se você "
    "prefere uma voz no ouvido.",
    "Un tocco manda tutto il giro su Google Maps per la navigazione passo passo, se preferisci "
    "una voce nell'orecchio.")
add("Every stop on the map", "Todas las paradas del mapa", "Todas as paradas do mapa",
    "Tutte le tappe sulla mappa")
add("Written by people who ride past them every day — not scraped from a listings site.",
    "Escrito por gente que pasa por delante cada día, no copiado de un portal de listados.",
    "Escrito por gente que passa na frente todo dia, não copiado de um site de listagens.",
    "Scritto da gente che ci passa davanti ogni giorno, non copiato da un portale di annunci.")


# ---------------------------------------------------------------- shop page
add("Why buy here", "Por qué comprar aquí", "Por que comprar aqui",
    "Perché comprare qui")
add("Ride it for an hour before you spend a cent",
    "Pruébalo una hora antes de gastar un céntimo",
    "Ande uma hora antes de gastar um centavo",
    "Provalo un'ora prima di spendere un centesimo")
add("Nobody should buy a Segway or a Trikke from a photograph. Rent the exact model, take it "
    "down Ocean Drive, and if you buy it we put the rental toward the purchase. We have been "
    "servicing these machines on this street since 2009 — so the warranty work happens here "
    "too, not in a box back to the factory.",
    "Nadie debería comprar un Segway o un Trikke por una foto. Alquila el modelo exacto, bájalo "
    "por Ocean Drive y, si lo compras, te descontamos el alquiler de la compra. Llevamos "
    "reparando estas máquinas en esta calle desde 2009, así que la garantía también se resuelve "
    "aquí, no en una caja de vuelta a fábrica.",
    "Ninguém deveria comprar um Segway ou um Trikke por uma foto. Alugue o modelo exato, desça a "
    "Ocean Drive com ele e, se comprar, abatemos o aluguel da compra. Consertamos essas máquinas "
    "nesta rua desde 2009, então a garantia também é resolvida aqui, não numa caixa de volta "
    "para a fábrica.",
    "Nessuno dovrebbe comprare un Segway o un Trikke da una foto. Noleggia il modello esatto, "
    "portalo giù per Ocean Drive e, se lo compri, scaliamo il noleggio dall'acquisto. Ripariamo "
    "queste macchine in questa strada dal 2009, quindi anche la garanzia si risolve qui, non in "
    "una scatola rispedita in fabbrica.")
add("Call about a model", "Pregunta por un modelo", "Pergunte sobre um modelo",
    "Chiedi di un modello")
add("The workshop", "El taller", "A oficina", "L'officina")
add("We fix what we sell — and what we didn't",
    "Arreglamos lo que vendemos, y lo que no",
    "Consertamos o que vendemos, e o que não vendemos",
    "Ripariamo quello che vendiamo, e anche quello che non vendiamo")
add("Walk in with a flat, a dead battery or a Segway that will not calibrate. Most jobs are "
    "done the same day.",
    "Entra con un pinchazo, una batería muerta o un Segway que no calibra. Casi todo sale el "
    "mismo día.",
    "Entre com um furo, uma bateria morta ou um Segway que não calibra. Quase tudo sai no mesmo "
    "dia.",
    "Entra con una foratura, una batteria morta o un Segway che non si calibra. Quasi tutto esce "
    "in giornata.")
add("Tubes, tyres, puncture repair and wheel truing on bikes, e-bikes and trikes.",
    "Cámaras, cubiertas, reparación de pinchazos y centrado de ruedas en bicis, e-bikes y triciclos.",
    "Câmaras, pneus, conserto de furos e centragem de rodas em bikes, e-bikes e triciclos.",
    "Camere d'aria, copertoni, riparazione forature e centratura ruote su bici, e-bike e tricicli.")
add("Cable and hydraulic brakes, derailleur setup, full drivetrain tune-ups.",
    "Frenos de cable e hidráulicos, ajuste de cambios y puesta a punto completa de la transmisión.",
    "Freios de cabo e hidráulicos, regulagem de câmbio e revisão completa da transmissão.",
    "Freni a cavo e idraulici, regolazione del cambio, tagliando completo della trasmissione.")
add("E-bike and Segway battery diagnostics, replacement cells and charger testing.",
    "Diagnóstico de baterías de e-bike y Segway, sustitución de celdas y prueba de cargadores.",
    "Diagnóstico de baterias de e-bike e Segway, troca de células e teste de carregadores.",
    "Diagnostica batterie e-bike e Segway, sostituzione celle e test dei caricabatterie.")
add("Authorized warranty work, calibration, tyres, and the full i2 parts range in stock.",
    "Garantía autorizada, calibración, neumáticos y toda la gama de repuestos i2 en stock.",
    "Garantia autorizada, calibração, pneus e toda a linha de peças i2 em estoque.",
    "Garanzia autorizzata, calibrazione, gomme e tutta la gamma ricambi i2 a magazzino.")

# ---------------------------------------------------------------- routes page
add("From a 40-minute spin to a half-day expedition",
    "De una vuelta de 40 minutos a una expedición de media jornada",
    "De uma volta de 40 minutos a uma expedição de meio dia",
    "Da un giro di 40 minuti a una spedizione di mezza giornata")
add("Every route starts and ends at our shop on 14th Street, so you always know how to get home.",
    "Todas las rutas empiezan y terminan en nuestra tienda de la calle 14, así siempre sabes "
    "cómo volver.",
    "Todas as rotas começam e terminam na nossa loja da rua 14, então você sempre sabe como "
    "voltar.",
    "Ogni percorso parte e finisce dal nostro negozio in 14ª strada, così sai sempre come "
    "tornare.")
add("Along the way:", "Por el camino:", "Pelo caminho:", "Lungo il tragitto:")
add("From the shop", "Desde la tienda", "Saindo da loja", "Dal negozio")
add("Helmets are required by Florida law for riders under 16 — we include one with every rental.",
    "La ley de Florida exige casco a los menores de 16 años; lo incluimos en cada alquiler.",
    "A lei da Flórida exige capacete para menores de 16 anos; incluímos um em cada aluguel.",
    "La legge della Florida impone il casco ai minori di 16 anni; lo includiamo in ogni noleggio.")
add("Bikes are not allowed on the sand or on the wooden boardwalk section through Mid-Beach; "
    "use the paved Beachwalk.",
    "Las bicis no pueden ir por la arena ni por el tramo de madera del boardwalk de Mid-Beach; "
    "usa el Beachwalk asfaltado.",
    "As bikes não podem circular na areia nem no trecho de madeira do boardwalk de Mid-Beach; "
    "use o Beachwalk pavimentado.",
    "Le bici non possono andare sulla sabbia né sul tratto in legno del boardwalk di Mid-Beach; "
    "usa il Beachwalk asfaltato.")
add("Ride with traffic, not against it. Ocean Drive and Collins both have marked lanes.",
    "Circula en el sentido del tráfico, no en contra. Ocean Drive y Collins tienen carril "
    "señalizado.",
    "Pedale no sentido do trânsito, não contra. Ocean Drive e Collins têm faixa sinalizada.",
    "Vai nel senso del traffico, non contromano. Ocean Drive e Collins hanno la corsia segnata.")
add("Lock the frame", "Ata el cuadro", "Prenda o quadro", "Lega il telaio")
add("a wheel to a fixed rack. Your lock is in the basket.",
    "una rueda a un soporte fijo. El candado va en la cesta.",
    "uma roda a um suporte fixo. O cadeado vai na cesta.",
    "una ruota a una rastrelliera fissa. Il lucchetto è nel cestino.")
add("Afternoon storms are normal from June to September. They pass in 20 minutes — duck under "
    "an awning.",
    "Las tormentas de tarde son normales de junio a septiembre. Pasan en 20 minutos: métete "
    "bajo un toldo.",
    "As tempestades de tarde são normais de junho a setembro. Passam em 20 minutos: entre "
    "debaixo de um toldo.",
    "I temporali del pomeriggio sono normali da giugno a settembre. Passano in 20 minuti: "
    "riparati sotto una tenda.")
add("Hydrate. The sun here is stronger than it feels with an ocean breeze on you.",
    "Hidrátate. Aquí el sol pega más de lo que parece con la brisa del mar encima.",
    "Hidrate-se. Aqui o sol é mais forte do que parece com a brisa do mar em cima de você.",
    "Bevi. Qui il sole picchia più di quanto sembri con la brezza del mare addosso.")


# --------------------------------------------------------- about & contact
add("Our story", "Nuestra historia", "Nossa história", "La nostra storia")
add("We have been fixing and renting on 14th Street since 2009",
    "Llevamos arreglando y alquilando en la calle 14 desde 2009",
    "Consertamos e alugamos na rua 14 desde 2009",
    "Ripariamo e noleggiamo in 14ª strada dal 2009")
add("We started with a rack of beach cruisers, a floor pump and the three-wheeled Trikke we "
    "named the place after. Today the shop runs ten kinds of wheels, six guided Segway tours, "
    "a full South Florida adventure desk and a workshop that keeps half the neighborhood's "
    "bikes, e-bikes and scooters on the road.",
    "Empezamos con un perchero de beach cruisers, una bomba de pie y el Trikke de tres ruedas "
    "que le dio nombre al sitio. Hoy la tienda mueve diez tipos de ruedas, seis tours guiados "
    "en Segway, un mostrador completo de aventuras por el sur de Florida y un taller que "
    "mantiene rodando media las bicis, e-bikes y patinetes del barrio.",
    "Começamos com um suporte de beach cruisers, uma bomba de pé e o Trikke de três rodas que "
    "deu nome ao lugar. Hoje a loja movimenta dez tipos de rodas, seis passeios guiados de "
    "Segway, um balcão completo de aventuras pelo sul da Flórida e uma oficina que mantém na "
    "rua metade das bikes, e-bikes e patinetes do bairro.",
    "Abbiamo iniziato con una rastrelliera di beach cruiser, una pompa a pedale e il Trikke a "
    "tre ruote che ha dato il nome al posto. Oggi il negozio gestisce dieci tipi di ruote, sei "
    "tour guidati in Segway, un banco completo di avventure nella Florida del sud e un'officina "
    "che tiene su strada metà delle bici, e-bike e monopattini del quartiere.")
add("What has not changed is the part we care about: you should be riding within ten minutes of "
    "walking in, on a bike that fits you, with someone who can tell you where to go and what to "
    "look at when you get there. Families are our favorite booking — baby seats, trailers, "
    "training wheels and kids' sizes are always in stock, and we have yet to meet a grandparent "
    "we could not get comfortable on a trike.",
    "Lo que no ha cambiado es lo que nos importa: deberías estar rodando a los diez minutos de "
    "entrar, en una bici de tu talla y con alguien que sepa decirte adónde ir y qué mirar al "
    "llegar. Las familias son nuestra reserva favorita: sillitas, remolques, ruedines y tallas "
    "infantiles hay siempre, y todavía no hemos conocido a un abuelo al que no pudiéramos poner "
    "cómodo en un triciclo.",
    "O que não mudou é a parte que nos importa: você deveria estar pedalando dez minutos depois "
    "de entrar, numa bike do seu tamanho e com alguém que saiba dizer aonde ir e o que olhar ao "
    "chegar. Famílias são a nossa reserva favorita: cadeirinhas, carretinhas, rodinhas e "
    "tamanhos infantis sempre têm, e ainda não conhecemos um avô que não conseguíssemos deixar "
    "confortável num triciclo.",
    "Quello che non è cambiato è la parte che ci sta a cuore: dovresti essere in sella entro "
    "dieci minuti dall'ingresso, su una bici della tua taglia e con qualcuno che sappia dirti "
    "dove andare e cosa guardare una volta arrivato. Le famiglie sono la nostra prenotazione "
    "preferita: seggiolini, rimorchi, rotelle e misure per bambini ci sono sempre, e non abbiamo "
    "ancora incontrato un nonno che non riuscissimo a far stare comodo su un triciclo.")
add("Free Wi-Fi", "Wi-Fi gratis", "Wi-Fi grátis", "Wi-Fi gratis")
add("Restroom", "Aseo", "Banheiro", "Bagno")
add("By the numbers", "En números", "Em números", "In numeri")
add("Fifteen seasons on this island", "Quince temporadas en esta isla",
    "Quinze temporadas nesta ilha", "Quindici stagioni su quest'isola")
add("Flats, brakes, gears, wheel truing, battery diagnostics and full tune-ups — for our fleet "
    "and for yours. Walk in with a problem, ride out the same day.",
    "Pinchazos, frenos, cambios, centrado de ruedas, diagnóstico de baterías y puestas a punto "
    "completas, para nuestra flota y para la tuya. Entra con un problema y sal rodando el mismo "
    "día.",
    "Furos, freios, marchas, centragem de rodas, diagnóstico de baterias e revisões completas, "
    "para a nossa frota e para a sua. Entre com um problema e saia pedalando no mesmo dia.",
    "Forature, freni, cambi, centratura ruote, diagnostica batterie e tagliandi completi, per la "
    "nostra flotta e per la tua. Entra con un problema ed esci in sella in giornata.")
add("Authorized Segway sales and service in Miami Beach, plus the only guided Segway tours that "
    "start this close to Ocean Drive.",
    "Venta y servicio Segway autorizados en Miami Beach, además de los únicos tours guiados en "
    "Segway que salen tan cerca de Ocean Drive.",
    "Venda e assistência Segway autorizadas em Miami Beach, além dos únicos passeios guiados de "
    "Segway que saem tão perto da Ocean Drive.",
    "Vendita e assistenza Segway autorizzate a Miami Beach, più gli unici tour guidati in Segway "
    "che partono così vicino a Ocean Drive.")
add("Everglades airboats, Key West day trips, Miami city tours, jet skis, parasailing and "
    "helicopter rides — booked at the same counter, most with hotel pickup.",
    "Hidrodeslizadores por los Everglades, excursiones a Key West, tours por Miami, motos "
    "acuáticas, parasailing y vuelos en helicóptero, reservados en el mismo mostrador y casi "
    "todos con recogida en el hotel.",
    "Aerobarcos nos Everglades, bate-voltas a Key West, passeios por Miami, jet skis, "
    "parasailing e voos de helicóptero, reservados no mesmo balcão e quase todos com busca no "
    "hotel.",
    "Airboat nelle Everglades, gite a Key West, tour di Miami, moto d'acqua, parasailing e giri "
    "in elicottero, prenotati allo stesso bancone e quasi tutti con ritiro in hotel.")
add("Open every day, 9 AM to 8 PM. No appointment needed — for anything except the Segway tours.",
    "Abierto todos los días de 9:00 a 20:00. Sin cita previa, salvo para los tours en Segway.",
    "Aberto todos os dias das 9h às 20h. Sem agendamento, exceto para os passeios de Segway.",
    "Aperto tutti i giorni dalle 9 alle 20. Senza appuntamento, tranne che per i tour in Segway.")
add("You cancel", "Cuándo cancelas", "Quando você cancela", "Quando disdici")
add("You get back", "Qué recuperas", "Quanto você recebe de volta", "Quanto ti torna")
add("All reservations are pre-paid in full, in US dollars. Named storms and shop-side "
    "cancellations are always fully refunded or rescheduled.",
    "Todas las reservas se pagan por adelantado y en su totalidad, en dólares estadounidenses. "
    "Las tormentas con nombre y las cancelaciones por nuestra parte siempre se reembolsan "
    "íntegras o se reprograman.",
    "Todas as reservas são pagas integralmente e antecipadamente, em dólares americanos. "
    "Tempestades nomeadas e cancelamentos do nosso lado são sempre reembolsados por completo ou "
    "remarcados.",
    "Tutte le prenotazioni si pagano per intero e in anticipo, in dollari americani. Le tempeste "
    "con nome e le disdette da parte nostra vengono sempre rimborsate per intero o riprogrammate.")
add("Tell us what you need", "Dinos qué necesitas", "Diga o que você precisa",
    "Dicci di cosa hai bisogno")
add("Send this and we reply within the hour during shop hours. For same-day rentals, just call "
    "— or book instantly online.",
    "Envíalo y te contestamos en menos de una hora en horario de tienda. Para alquilar hoy "
    "mismo, llama sin más, o reserva al instante por internet.",
    "Envie e respondemos em menos de uma hora no horário da loja. Para alugar hoje mesmo, é só "
    "ligar, ou reserve na hora pela internet.",
    "Invia e ti rispondiamo entro un'ora negli orari del negozio. Per noleggiare oggi stesso, "
    "chiama e basta, oppure prenota subito online.")
add("Your name", "Tu nombre", "Seu nome", "Il tuo nome")
add("What do you want", "Qué quieres", "O que você quer", "Cosa vuoi")
add("Or skip the form:", "O sáltate el formulario:", "Ou pule o formulário:",
    "Oppure salta il modulo:")
add("One block west of Ocean Drive, in the heart of South Beach.",
    "A una cuadra al oeste de Ocean Drive, en pleno South Beach.",
    "A um quarteirão a oeste da Ocean Drive, no coração de South Beach.",
    "A un isolato a ovest di Ocean Drive, nel cuore di South Beach.")
add("Every day · 9:00 AM – 8:00 PM", "Todos los días · 9:00 – 20:00",
    "Todos os dias · 9h – 20h", "Tutti i giorni · 9:00 – 20:00")
add("Happy hour 1–4 PM: +1 free hour", "Happy hour de 13:00 a 16:00: +1 hora gratis",
    "Happy hour das 13h às 16h: +1 hora grátis", "Happy hour dalle 13 alle 16: +1 ora gratis")
add("Call or write", "Llama o escribe", "Ligue ou escreva", "Chiama o scrivi")
add("Free across South Beach on 24h+ rentals. Mid-Beach, North Beach, Downtown, Brickell and "
    "Key Biscayne by flat fee.",
    "Gratis por todo South Beach en alquileres de 24 h o más. Mid-Beach, North Beach, Downtown, "
    "Brickell y Key Biscayne con tarifa fija.",
    "Grátis por toda South Beach em aluguéis de 24 h ou mais. Mid-Beach, North Beach, Downtown, "
    "Brickell e Key Biscayne com taxa fixa.",
    "Gratis in tutta South Beach sui noleggi di 24 h o più. Mid-Beach, North Beach, Downtown, "
    "Brickell e Key Biscayne con tariffa fissa.")
