# -*- coding: utf-8 -*-
"""
Content localisation.

Two layers, because most of the 666 translatable strings per language are
short and repeat across the catalogue:

  PHRASES  — short fragments reused everywhere ("1 hour", "Ages 14+",
             "Helmet + lock"). One entry covers dozens of occurrences.
  TEXTS    — the long, unique prose: product hooks, POI stories, FAQ
             answers, route descriptions, page copy. Keyed by a dotted
             path so a missing key is obvious.

Proper nouns are deliberately absent from both. "Ocean Drive", "Española
Way", "Lummus Park", "Star Island" and the rest stay as they are in every
language — translating a street name breaks the map and the search intent.

Anything with no entry falls through to English, and `audit()` reports
exactly what is still missing per language.
"""
import copy

from t_es import PHRASES as P_ES, TEXTS as T_ES
from t_pt import PHRASES as P_PT, TEXTS as T_PT
from t_it import PHRASES as P_IT, TEXTS as T_IT

PHRASES = {"es": P_ES, "pt": P_PT, "it": P_IT}
TEXTS = {"es": T_ES, "pt": T_PT, "it": T_IT}

_MISSING = {"es": set(), "pt": set(), "it": set()}


def ph(s, lang):
    """A short reusable fragment."""
    if lang == "en" or not s:
        return s
    table = PHRASES.get(lang, {})
    if s in table:
        return table[s]
    _MISSING.setdefault(lang, set()).add("phrase:" + s)
    return s


def tx(key, default, lang):
    """A long, unique text, by dotted key."""
    if lang == "en":
        return default
    table = TEXTS.get(lang, {})
    if key in table:
        return table[key]
    _MISSING.setdefault(lang, set()).add(key)
    return default


def localise(data, lang):
    """Return language-specific copies of every catalogue structure."""
    if lang == "en":
        return dict(
            FLEET=data.FLEET, TOURS=data.TOURS, ADVENTURES=data.ADVENTURES,
            SHOP=data.SHOP, ROUTES=data.ROUTES, FAQ=data.FAQ, POI=data.POI,
            MODES=data.MODES, INTERESTS=data.INTERESTS, DURATIONS=data.DURATIONS,
            EXTEND_BLOCKS=data.EXTEND_BLOCKS, PAY_METHODS=data.PAY_METHODS,
            REVIEWS=data.REVIEWS,
        )

    def items(src, kind, name_key=True):
        out = []
        for it in copy.deepcopy(src):
            slug = it["slug"]
            base = "%s.%s" % (kind, slug)
            if name_key:
                it["name"] = tx(base + ".name", it["name"], lang)
            it["tag"] = ph(it["tag"], lang)
            it["hook"] = tx(base + ".hook", it["hook"], lang)
            it["meta"] = [ph(m, lang) for m in it.get("meta", [])]
            if "sub" in it:
                it["sub"] = tx(base + ".sub", it["sub"], lang)
            if "unit" in it:
                it["unit"] = ph(it["unit"], lang)
            if "dur_pretty" in it:
                it["dur_pretty"] = ph(it["dur_pretty"], lang)
            if "rates" in it:
                it["rates"] = [(ph(lbl, lang), v) for lbl, v in it["rates"]]
            if "options" in it:
                it["options"] = [(ph(lbl, lang), v) for lbl, v in it["options"]]
            out.append(it)
        return out

    fleet = items(data.FLEET, "fleet")
    tours = items(data.TOURS, "tour")
    advs = items(data.ADVENTURES, "adv")
    shop = items(data.SHOP, "shop")

    routes = []
    for r in copy.deepcopy(data.ROUTES):
        key = "route." + r["name"].lower().replace(" ", "-").replace("'", "")
        r["name"] = tx(key + ".name", r["name"], lang)
        r["desc"] = tx(key + ".desc", r["desc"], lang)
        r["level"] = ph(r["level"], lang)
        r["time"] = ph(r["time"], lang)
        routes.append(r)

    faq = [(tx("faq.%d.q" % i, q, lang), tx("faq.%d.a" % i, a, lang))
           for i, (q, a) in enumerate(data.FAQ)]

    poi = []
    for p in copy.deepcopy(data.POI):
        base = "poi." + p["id"]
        p["sub"] = tx(base + ".sub", p["sub"], lang)
        p["story"] = tx(base + ".story", p["story"], lang)
        poi.append(p)

    modes = []
    for m in copy.deepcopy(data.MODES):
        base = "mode." + m["id"]
        m["name"] = tx(base + ".name", m["name"], lang)
        m["short"] = ph(m["short"], lang)
        m["blurb"] = tx(base + ".blurb", m["blurb"], lang)
        modes.append(m)

    interests = [(t, ph(label, lang), ico) for t, label, ico in data.INTERESTS]
    durations = [dict(d, name=ph(d["name"], lang)) for d in copy.deepcopy(data.DURATIONS)]
    blocks = [dict(b, label=ph(b["label"], lang)) for b in copy.deepcopy(data.EXTEND_BLOCKS)]
    pays = [dict(m, note=ph(m["note"], lang)) for m in copy.deepcopy(data.PAY_METHODS)]
    reviews = [(tx("review.%d" % i, q, lang), who)
               for i, (q, who) in enumerate(data.REVIEWS)]

    return dict(FLEET=fleet, TOURS=tours, ADVENTURES=advs, SHOP=shop,
                ROUTES=routes, FAQ=faq, POI=poi, MODES=modes,
                INTERESTS=interests, DURATIONS=durations,
                EXTEND_BLOCKS=blocks, PAY_METHODS=pays, REVIEWS=reviews)


def audit():
    """What is still English, per language."""
    return {lg: sorted(keys) for lg, keys in _MISSING.items() if keys}
