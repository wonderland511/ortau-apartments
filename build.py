#!/usr/bin/env python3
"""Генератор index.html. Чтобы добавить квартиру — допиши словарь в APTS и запусти: python3 build.py"""
import json, math, html

ORTAU = (43.2364265, 76.9377950)  # Наурызбай батыра 127 — OpenStreetMap (Nominatim)
PHOTOS = json.load(open("photos.json"))
BK = "https://www.booking.com/hotel/kz/{slug}.ru.html?aid=304142&checkin=2026-09-23&checkout=2026-09-28&group_adults=1&no_rooms=1&group_children=0&all_sr_blocks={b}&highlighted_blocks={b}&matching_block_id={b}"

# distances: straight — по формуле гаверсинуса, foot/car — OSRM (routing.openstreetmap.de), координаты — из Booking
APTS = [
    dict(key="central", name="ЖК Central Avenue #81", sub="квартира с видом на горы", slug="central-avenue-zhiloi-kompleks", b="1487667401_427430335_4_0_0",
         addr="проспект Сейфуллина 574/1", ll=(43.2302192096248, 76.9382911907379),
         straight=691, foot=(1480, 19.7), car=(1538, 2.8),
         score="9,7", word="Великолепно", nrev=10, area=50,
         price=470, was=614, off="−23%", genius="Genius −10%",
         beds="Двуспальная кровать + диван-кровать",
         feats=["Своя кухня", "Балкон", "Кондиционер", "Телевизор", "Wi-Fi", "Бесплатная парковка", "Вид на город"],
         terms=["Бесплатная отмена до 22 сентября 2026", "Предоплата не требуется — оплата на месте"],
         cats=[("Персонал", "8,8"), ("Удобства", "9,2"), ("Чистота", "9,4"), ("Комфорт", "9,6"), ("Цена/качество", "9,6"), ("Расположение", "9,4")],
         reviews=[("Айдос, Казахстан", "Хорошая квартира с уютной атмосферой. Всё аккуратно, чисто и продумано для гостей.")]),
    dict(key="alfarabi27", name="Аль фараби 27 #23", sub="", slug="al-farabi-27-23", b="1460888301_417385936_3_0_0",
         addr="проспект Аль-Фараби 27", ll=(43.2275165444874, 76.9401675034922),
         straight=1009, foot=(1468, 19.6), car=(1845, 3.0),
         score="8,4", word="Очень хорошо", nrev=5, area=60,
         price=388, was=614, off="−37%", genius="Genius −21%",
         beds="Большая двуспальная кровать + диван-кровать",
         feats=["Своя кухня", "Балкон", "Кондиционер", "Ванна", "Телевизор", "Wi-Fi", "Бесплатная парковка", "Вид на город"],
         terms=["Бесплатная отмена до 22 сентября 2026", "Предоплата не требуется — оплата на месте"],
         cats=[("Персонал", "8,5"), ("Удобства", "8,5"), ("Чистота", "8,5"), ("Комфорт", "8,5"), ("Цена/качество", "8,5"), ("Расположение", "8,5")],
         reviews=[("Giorgi, Грузия", "Место было очень хорошее, чистое и аккуратное, отличное расположение, очень удобно. Всё работало как положено, и за время пребывания не возникло никаких проблем.")]),
    dict(key="smartlux", name="Smart Lux 320", sub="ЖК «Нурлы Тау»", slug="smart-lux-320", b="1561031301_427196015_2_0_0",
         addr="проспект Аль-Фараби 7к5а", ll=(43.23014819916744, 76.9469301094856),
         straight=1017, foot=(1889, 25.2), car=(1965, 4.0),
         score="10", word="Великолепно", nrev=2, area=100,
         price=None, was=None, off=None, genius=None,
         beds="", feats=["Своя кухня", "Вид на город", "Жильё целиком"],
         terms=[],
         cats=[("Персонал", "10"), ("Удобства", "10"), ("Чистота", "10"), ("Комфорт", "10"), ("Цена/качество", "10"), ("Расположение", "10")],
         reviews=[]),
    dict(key="metropole", name="Stay Almaty Metropole", sub="", slug="stay-almaty-metropole", b="1706125401_442246839_5_0_0",
         addr="проспект Аль-Фараби 41/7, кв. 14", ll=(43.2263132, 76.939326),
         straight=1131, foot=(1617, 21.6), car=(3369, 5.2),
         score="9,5", word="Великолепно", nrev=2, area=83,
         price=None, was=None, off=None, genius=None,
         beds="", feats=["Жильё целиком", "Парковка"],
         terms=[],
         cats=[("Удобства", "10"), ("Чистота", "10"), ("Комфорт", "10"), ("Цена/качество", "10"), ("Расположение", "10")],
         reviews=[("Жамийла, Россия", "Квартира чистая, уютная, со всеми условиями проживания. Хозяин квартиры очень приятный, доброжелательный молодой человек."),
                  ("David, Казахстан (на англ.)", "Begzat met us at the door. He has great English, very hospitable. It's the most beautiful apartment we've stayed in in Almaty. Only two months old but with quality finishes. Beautiful carpentry, tiling, flooring. Very clean and crisp....")]),
    dict(key="orion", name="Home Comfort Orion", sub="", slug="liuks-apartamenty-v-zhk-zher-ana", b="1320527001_404758007_2_0_0",
         addr="проспект Назарбаева 235Б", ll=(43.2301848685788, 76.9491433762883),
         straight=1152, foot=(1805, 24.1), car=(2537, 4.8),
         score="10", word="Великолепно", nrev=1, area=65,
         price=403, was=None, off=None, genius=None,
         beds="Двуспальная кровать + диван-кровать",
         feats=["Своя кухня", "Балкон", "Кондиционер", "Телевизор", "Стиральная машина", "Wi-Fi", "Бесплатная парковка", "Вид на горы и город", "Звукоизоляция"],
         terms=["Бесплатная отмена до 22 сентября 2026", "Предоплата не требуется, банковская карта не нужна"],
         warn="Бронирование не подтверждается мгновенно: хозяин отвечает в течение 24 часов. Booking пишет, что обычно здесь нет мест.",
         cats=[], reviews=[]),
]
APTS.sort(key=lambda a: a["straight"])

def km(m): return f"{m/1000:.1f}".replace(".", ",") + " км" if m >= 1000 else f"{m} м"
def esc(s): return html.escape(s, quote=True)

def gmaps(a):
    return ("https://www.google.com/maps/dir/?api=1&origin=%s,%s&destination=%s,%s&travelmode=walking" % (a["ll"][0], a["ll"][1], ORTAU[0], ORTAU[1]))

# ---------- радар-схема ----------
K = 0.40  # px на метр
X0, Y0 = 160, 90  # положение ORTAU в SVG
W, H = 640, 640
def pos(ll):
    dx = (ll[1] - ORTAU[1]) * 111320 * math.cos(math.radians(ORTAU[0]))
    dy = (ll[0] - ORTAU[0]) * 110574
    return X0 + dx * K, Y0 - dy * K
rings = "".join(f'<circle cx="{X0}" cy="{Y0}" r="{r*K:.0f}" class="ring"/><text x="{X0+r*K*0.72+4:.0f}" y="{Y0+r*K*0.72+12:.0f}" class="rl">{km(r)}</text>' for r in (500, 1000, 1500))
dots = ""
lab = {"central": (14, 5, "start"), "alfarabi27": (14, 4, "start"), "metropole": (14, 5, "start"), "smartlux": (0, -16, "middle"), "orion": (0, 26, "middle")}
for i, a in enumerate(APTS, 1):
    x, y = pos(a["ll"]); dx, dy, an = lab[a["key"]]
    dots += (f'<g><line x1="{X0}" y1="{Y0}" x2="{x:.0f}" y2="{y:.0f}" class="ln"/>'
             f'<circle cx="{x:.0f}" cy="{y:.0f}" r="12" class="dot"/><text x="{x:.0f}" y="{y+4.5:.0f}" text-anchor="middle" class="dn">{i}</text>'
             f'<text x="{x+dx:.0f}" y="{y+dy:.0f}" text-anchor="{an}" class="dl">{esc(a["name"].replace("ЖК ","").split(" #")[0])}</text></g>')
radar = (f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Схема: расположение квартир относительно ЖК ORTAU" class="radar">'
         f'{rings}{dots}<circle cx="{X0}" cy="{Y0}" r="9" class="ort"/><text x="{X0+16}" y="{Y0+5}" class="ol">ORTAU</text>'
         f'<g class="north"><path d="M{W-34} 46 l7 -20 l7 20 l-7 -6 z"/><text x="{W-27}" y="66" text-anchor="middle">С</text></g></svg>')

# ---------- таблица ----------
rows = ""
for i, a in enumerate(APTS, 1):
    price = f"${a['price']}" if a["price"] else "уточнить"
    per = f"<small>${a['price']/5:.0f}/ночь</small>" if a["price"] else ""
    rows += (f'<a class="row" href="#{a["key"]}"><span class="n">{i}</span><span class="nm"><b>{esc(a["name"])}</b><small>{esc(a["addr"])}</small></span>'
             f'<span class="c"><b>{km(a["straight"])}</b><small>по прямой</small></span>'
             f'<span class="c"><b>{a["foot"][1]:.0f} мин</b><small>пешком ~{km(a["foot"][0])}</small></span>'
             f'<span class="c"><b>{a["score"]}</b><small>{a["nrev"]} отз.</small></span>'
             f'<span class="c"><b>{price}</b>{per}</span></a>')

# ---------- карточки ----------
def card(i, a):
    imgs = "".join(f'<img src="{esc(u)}" alt="{esc(a["name"])} — фото {j}" referrerpolicy="no-referrer" {"loading=eager" if j==1 else "loading=lazy"} decoding="async" onerror="this.style.display=\'none\'">'
                   for j, u in enumerate(PHOTOS[a["key"]], 1))
    if a["price"]:
        was = f'<s>${a["was"]}</s> <span class="off">{a["off"]}</span>' if a["was"] else ""
        gen = f'<span class="tag">{a["genius"]}</span>' if a["genius"] else ""
        price = (f'<div class="price"><div class="pv">${a["price"]}</div><div class="pl">за 5 ночей, с налогами · ~${a["price"]/5:.0f}/ночь</div>'
                 f'<div class="pw">{was} {gen}</div></div>')
    else:
        price = '<div class="price nop"><div class="pv">цена уточняется</div><div class="pl">Booking не показал цену на даты 23–28.09 — нужна проверка по ссылке</div></div>'
    cats = "".join(f'<li><span>{c}</span><b>{v}</b></li>' for c, v in a["cats"])
    revs = "".join(f'<blockquote>«{esc(t)}»<cite>— {esc(w)}</cite></blockquote>' for w, t in a["reviews"])
    if not revs:
        revs = f'<p class="muted">Текстовых отзывов на странице нет — только оценка ({a["nrev"]} {"отзыв" if a["nrev"]==1 else "отзыва"}).</p>'
    terms = "".join(f'<li>{esc(t)}</li>' for t in a["terms"])
    feats = "".join(f'<li>{esc(f)}</li>' for f in a["feats"])
    warn = f'<p class="warn">⚠ {esc(a["warn"])}</p>' if a.get("warn") else ""
    beds = f'<li>{esc(a["beds"])}</li>' if a["beds"] else ""
    sub = f' <span class="sub">· {esc(a["sub"])}</span>' if a["sub"] else ""
    return f'''
<article class="card" id="{a["key"]}" style="animation-delay:{0.05*i:.2f}s">
  <div class="gal"><div class="track">{imgs}</div>
    <button class="nav prev" aria-label="Предыдущее фото" hidden>‹</button><button class="nav next" aria-label="Следующее фото" hidden>›</button>
    <span class="cnt" hidden></span><span class="rank">№{i} по близости</span></div>
  <div class="body">
    <h2>{esc(a["name"])}{sub}</h2>
    <p class="addr">{esc(a["addr"])}, Алматы</p>
    <div class="dist"><div class="dv"><b>{km(a["straight"])}</b><span>по прямой до ORTAU</span></div>
      <div class="dv"><b>~{a["foot"][1]:.0f} мин</b><span>пешком, ~{km(a["foot"][0])}</span></div>
      <div class="dv"><b>~{a["car"][1]:.0f} мин</b><span>на машине, ~{km(a["car"][0])}</span></div></div>
    <div class="mid"><div class="score"><b>{a["score"]}</b><span>{a["word"]} · {a["nrev"]} {"отзыв" if a["nrev"]==1 else "отзыва" if a["nrev"] in (2,3,4) else "отзывов"}</span></div>{price}</div>
    {warn}
    <ul class="chips"><li>{a["area"]} м²</li>{beds}{feats}</ul>
    {"<ul class='terms'>"+terms+"</ul>" if terms else ""}
    {"<ul class='cats'>"+cats+"</ul>" if cats else ""}
    <div class="revs">{revs}</div>
    <div class="cta"><a class="btn primary" href="{esc(BK.format(slug=a["slug"], b=a["b"]))}" target="_blank" rel="noopener">Открыть на Booking.com</a>
      <a class="btn" href="{esc(gmaps(a))}" target="_blank" rel="noopener">Маршрут пешком до ORTAU</a></div>
  </div>
</article>'''
cards = "".join(card(i, a) for i, a in enumerate(APTS, 1))

PAGE = open("template.html", encoding="utf-8").read()
PAGE = PAGE.replace("{{ROWS}}", rows).replace("{{RADAR}}", radar).replace("{{CARDS}}", cards)
open("index.html", "w", encoding="utf-8").write(PAGE)
print("ok", len(PAGE), "bytes;", len(APTS), "квартир")
