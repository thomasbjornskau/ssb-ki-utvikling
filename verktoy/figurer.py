"""Tegner oversiktsfigurene til nettstedet. Kjør: python3 verktoy/figurer.py"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kf import Fig, ramme, boks, C, F_MELLOM, F_TEKST, STIPLET, FORSLAG

UT = os.path.join(os.path.dirname(__file__), "..", "docs", "figurer")
BUNN = "25.11.2026 · Skisse til diskusjon · KI-gruppen, avdeling 700"


def lagre(f, navn):
    open(os.path.join(UT, navn + ".svg"), "w", encoding="utf-8").write(f.svg())
    print("ok", navn)


# ---------------------------------------------------------------- 0
def f0():
    f = Fig()
    ramme(f, "Hva nettstedet inneholder",
          "Seks områder. Retningslinjene ligger under alt, tre områder fylles i første versjon",
          ["Oversikt", "FORSLAG"], "Slik leser du figuren",
          [("Grunnmuren er reglene", ["Kom i gang og bevisst bruk bygger", "på retningslinjene. De kan ikke", "si noe reglene ikke sier."]),
           ("To spor for brukerne", ["Kom i gang er praksis: hvordan.", "Bevisst bruk er vurdering:", "når, og når ikke."]),
           ("Deling og læring kommer etter", ["Felles verktøy og innsikt får", "en ramme nå og fylles når", "reglene er på plass."]),
           ("Gruppen holder det sammen", ["KI-gruppen eier ikke alt, men", "sørger for at områdene henger", "sammen og holdes oppdatert."])],
          [("flate", "Område i første versjon"), ("uavklart", "Ramme, fylles senere"), ("rolle", "Ansvar"), ("pil", "Bygger på"), ("pilstiplet", "Påvirker")],
          BUNN)
    # gruppen som vertikalt bånd
    boks(f, 60, 200, 200, 766, "KI-gruppen", ["Koordinerer", "og holder", "oppdatert"], "rolle", accent=True)
    # topp: deling og læring (ramme)
    boks(f, 300, 200, 520, 200, "Felles verktøy", ["Instruksjoner, skills, agenter", "og godkjente MCP-servere"], "uavklart")
    boks(f, 860, 200, 520, 200, "Innsikt", ["Bruk, kostnad og erfaring.", "Nyheter hver måned."], "uavklart")
    # midt
    boks(f, 300, 450, 520, 230, "Kom i gang", ["For utviklere", "For statistikere som koder", "Gode instruksjoner · Kontroll før bruk"], "flate", accent=True)
    boks(f, 860, 450, 520, 230, "Bevisst bruk", ["Grønn og rød sone", "KI-kompetanse etter", "KI-forordningen"], "flate", accent=True)
    # grunnmur
    boks(f, 300, 736, 1080, 230, "Retningslinjer", ["Hva er lov · Data og taushetsplikt · Ansvar · Agenter og isolasjon · Endringslogg"], "flate", accent=True)
    f.rect(318, 850, 1044, 92, C["g1"], C["g4"], 1, 2)
    f.h(340, 886, "Hovedregelen", 18, C["g4"])
    f.text(340, 916, "Start med dataene: åpent, internt eller taushetsbelagt. Deretter verktøyet.", 17, C["m5"])
    # piler: bygger på
    for x in (560, 1120):
        f.arrow([(x, 734), (x, 684)])
    for x in (560, 1120):
        f.arrow([(x, 448), (x, 404)], C["gra"], dash=STIPLET)
    # innsikt påvirker reglene: retur langs høyre
    f.arrow([(1382, 300), (1410, 300), (1410, 850), (1384, 850)], C["gra"], dash=STIPLET)
    f.text(1372, 432, "innsikt justerer reglene", 15, C["gra"], anchor="end")
    # brikker for versjon 1
    for x, y in ((650, 480), (1210, 480), (1210, 766)):
        f.brikke(x, y, "Versjon 1", "data")
    lagre(f, "0-nettstedskart")


# ---------------------------------------------------------------- 1
def f1():
    f = Fig()
    ramme(f, "Hvilke data kan gå inn i hvilket verktøy",
          "Start med dataene. Jo strengere datanivå, jo færre verktøy er aktuelle",
          ["Oversikt", "FORSLAG"], "Fire ting å merke seg",
          [("Dataene bestemmer", ["Spør først hvilket nivå dataene", "har. Et godkjent verktøy gjør ikke", "taushetsbelagte data trygge."]),
           ("Taushetsbelagt: nei i dag", ["Ingen av verktøyene er godkjent", "for mikrodata. Om det skal finnes", "en egen løsning, er uavklart."]),
           ("Før publisering", ["Upubliserte tall er taushets-", "belagte, uansett hvor aggregerte", "de er."]),
           ("Private abonnement", ["Nei også for åpne data. Grunnen", "er avtalen, ikke dataene."])],
          [("data", "Tillatt"), ("vilkar", "Med vilkår"), ("nei", "Ikke tillatt"), ("uavklart", "Uavklart, avklares")],
          BUNN)
    kol = [("M365 Copilot", "Chat"), ("GitHub Copilot", "i editoren"), ("Agenter", "agentmodus, CLI"),
           ("Særskilt godkjent", "løsning"), ("Private og", "gratistjenester")]
    rad = [("Åpent", ["Publisert statistikk,", "åpen kode"]), ("Internt", ["Dokumentasjon, kode", "uten data, metadata"]),
           ("Taushetsbelagt", ["Mikrodata,", "upubliserte tall"])]
    # celler: (tekst, undertekst, type)
    V = [
        [("Ja", "", "ja"), ("Ja", "", "ja"), ("Med vilkår", "avgrenset tilgang", "vilkar"), ("–", "", "tom"), ("Nei", "ingen avtale", "nei")],
        [("Med vilkår", "jobbkonto", "vilkar"), ("Med vilkår", "kode uten data", "vilkar"), ("Med vilkår", "isolert, review", "vilkar"), ("–", "", "tom"), ("Nei", "ingen avtale", "nei")],
        [("Nei", "", "nei"), ("Nei", "", "nei"), ("Nei", "", "nei"), ("?", "finnes det?", "uavklart"), ("Nei", "", "nei")],
    ]
    x0, y0, cw, ch, rw, hh = 300, 200, 214, 210, 220, 110
    # kolonnehoder
    for j, (a, b) in enumerate(kol):
        x = x0 + j * cw
        f.rect(x + 6, y0, cw - 12, hh - 14, C["m1"], C["m5"], 1, 2)
        f.h(x + cw / 2, y0 + 38, a, 18, anchor="middle")
        f.text(x + cw / 2, y0 + 66, b, 15, C["gra"], anchor="middle")
    for i, (navn, tx) in enumerate(rad):
        y = y0 + hh + i * ch
        f.rect(60, y + 6, 5, ch - 12, C["g4"], "none", 0, 0)
        f.h(82, y + 48, navn, 20, C["g4"])
        f.lines(82, y + 82, tx, 15, C["m5"], lh=21)
        for j in range(5):
            t, u, typ = V[i][j]
            x = x0 + j * cw
            cx, cy = x + cw / 2, y + ch / 2
            if typ == "ja":
                f.rect(x + 6, y + 6, cw - 12, ch - 12, C["g1"], C["g4"], 1, 2)
                tc = C["g4"]
            elif typ == "vilkar":
                f.rect(x + 6, y + 6, cw - 12, ch - 12, C["hvit"], C["g4"], 1, 2)
                f.rect(x + 6, y + 6, 5, ch - 12, C["g4"], "none", 0, 0)
                tc = C["g4"]
            elif typ == "nei":
                f.rect(x + 6, y + 6, cw - 12, ch - 12, C["ufyll"], C["ustrek"], 1, 2)
                tc = C["rod"]
            elif typ == "uavklart":
                f.rect(x + 6, y + 6, cw - 12, ch - 12, C["hvit"], C["ustrek"], 1, 2, STIPLET)
                tc = C["gra"]
            else:
                f.rect(x + 6, y + 6, cw - 12, ch - 12, C["ufyll"], "none", 0, 2)
                tc = C["ustrek"]
            f.text(cx, cy + (0 if u else 10), t, 26, tc, F_MELLOM, 700, "middle")
            if u:
                f.text(cx, cy + 32, u, 15, C["m5"] if typ != "uavklart" else C["gra"], anchor="middle")
    # strenghet-pil
    f.arrow([(1402, y0 + hh + 10), (1402, y0 + hh + 3 * ch - 30)], C["m5"])
    f.text(1402, y0 + hh + 3 * ch, "strengere", 15, C["gra"], anchor="middle")
    f.h(82, y0 + 40, "Data", 18, C["g4"])
    f.text(82, y0 + 66, "nedover", 15, C["gra"])
    lagre(f, "1-retningslinjer")


# ---------------------------------------------------------------- 2
def f2():
    f = Fig()
    ramme(f, "To innganger, ett felles grunnlag",
          "Utviklere og statistikere starter ulikt, men kontrollerer på samme måte før koden brukes",
          ["Oversikt", "FORSLAG"], "Hvorfor to innganger",
          [("Ulike startpunkter", ["Utviklere kjenner Git og review.", "Det nye er agentene og grensene."]),
           ("Statistikere sitter tett på data", ["I en notebook ligger kode og data", "sammen. Derfor starter sporet", "med regelen om å ikke vise data."]),
           ("Samme vane til slutt", ["Begge spor ender i kontroll før", "bruk: forstå, teste, sammenligne."]),
           ("Reglene ligger under", ["Ingen av stegene kan gi mer", "rom enn retningslinjene gir."])],
          [("rolle", "Hvem"), ("flate", "Steg"), ("data", "Felles vane"), ("pil", "Rekkefølge")],
          BUNN)
    spor = [
        (80, "Utvikler", "plattform, tjenester, avd. 700",
         [("Skaff tilgang", "lisens og modeller"), ("Instruksjoner i repoet", "gi agenten kontekst"),
          ("Agentmodus med grenser", "avgrenset, godkjenn kommandoer"), ("Plan før kode", "du eier arkitekturen")]),
        (740, "Statistiker som koder", "Python eller R i Dapla",
         [("Vis kode, ikke data", "struktur, ikke verdier"), ("Forklar og oversett", "arvet kode, SAS til Python"),
          ("Tester med syntetiske data", "så feil blir synlige"), ("Faglige valg selv", "metode, plausibilitet, prikking")]),
    ]
    bw = 600
    for x, navn, under, steg in spor:
        f.rect(x, 196, bw, 92, C["l1"], C["l3"], 1, 2)
        f.rect(x, 196, 5, 92, C["l3"], "none", 0, 0)
        f.h(x + 26, 236, navn, 22, C["lt"])
        f.text(x + 26, 268, under, 16, C["m5"])
        y = 318
        for i, (a, b) in enumerate(steg):
            f.arrow([(x + bw / 2, y - 28), (x + bw / 2, y - 2)])
            f.rect(x + 40, y, bw - 80, 76, C["m1"], C["m5"], 1, 2)
            f.text(x + 70, y + 46, str(i + 1), 22, C["gra"], "Roboto, Arial, sans-serif", 700, "middle")
            f.h(x + 96, y + 34, a, 19)
            f.text(x + 96, y + 60, b, 16, C["gra"])
            y += 104
        f.arrow([(x + bw / 2, y - 28), (x + bw / 2 + (1 if x > 400 else -1) * 0, y + 8)])
    # felles kontroll
    yk = 744 + 8
    f.rect(80, yk, 1260, 112, C["g1"], C["g4"], 1, 2)
    f.rect(80, yk, 1260, 5, C["g4"], "none", 0, 0)
    f.h(110, yk + 46, "Kontroll før bruk", 22, C["g4"])
    f.text(110, yk + 80, "Forstå hver linje · test som ville feilet · sjekk at funksjonene finnes · sammenlign med fasit · review", 17, C["m5"])
    # retningslinjer
    f.rect(80, 884, 1260, 82, C["m5"], "none", 0, 2)
    f.h(110, 934, "Retningslinjer", 20, C["hvit"])
    f.text(290, 934, "Data og taushetsplikt · Ansvar · Agenter og isolasjon", 17, C["hvit"])
    lagre(f, "2-kom-i-gang")


# ---------------------------------------------------------------- 3
def f3():
    f = Fig()
    ramme(f, "Grønn og rød sone i statistikkarbeid",
          "Hvor KI sparer tid, og hvor det å gjøre jobben selv er selve verdien",
          ["Oversikt", "Diskusjon"], "Slik bruker du skillet",
          [("Grønn sone: la KI gjøre det", ["Du vet hva svaret skal bli,", "og ser raskt om det er riktig."]),
           ("Rød sone: gjør det selv først", ["Her bygges forståelsen av", "statistikken. KI kan støtte,", "men ikke tenke for deg."]),
           ("Grensen er personlig", ["Den flytter seg når du lærer.", "Nyansatte bør ha mer i rød sone."]),
           ("Tre vaner", ["Prøv selv først. Generer, så", "forstå. Merk når du slutter", "å forstå."])],
          [("data", "Grønn sone: KI gjør jobben"), ("rolle", "Rød sone: du gjør jobben"), ("flate", "Vane")],
          BUNN)
    gx, rx, w, y0 = 60, 740, 640, 196
    f.rect(gx, y0, w, 560, C["g1"], C["g4"], 1, 2)
    f.rect(gx, y0, w, 5, C["g4"], "none", 0, 0)
    f.h(gx + 28, y0 + 52, "Grønn sone", 26, C["g4"])
    f.text(gx + 28, y0 + 84, "KI sparer tid, du mister ikke noe du trenger", 17, C["m5"])
    f.rect(rx, y0, w, 560, C["l1"], C["l3"], 1, 2)
    f.rect(rx, y0, w, 5, C["l3"], "none", 0, 0)
    f.h(rx + 28, y0 + 52, "Rød sone", 26, C["lt"])
    f.text(rx + 28, y0 + 84, "Den tankemessige jobben er verdien", 17, C["m5"])
    gron = ["Boilerplate og oppsett", "Oversette syntaks fra SAS eller R", "Syntetiske testdata",
            "Dokumentasjon for kode du forstår", "Formatere og rydde kode", "Utkast til tester", "Forklare en feilmelding"]
    rod = ["Feilsøke et tall som ikke stemmer", "Avgjøre om oversettelsen gir samme tall", "Velge og begrunne metode",
           "Plausibilitetskontroll av nye tall", "Forstå en ny datakilde", "Bestemme hva som skal testes", "Kjernelogikk i produksjonsløpet"]
    for i, t in enumerate(gron):
        y = y0 + 116 + i * 62
        f.rect(gx + 28, y, w - 56, 50, C["hvit"], C["g4"], 1, 2)
        f.text(gx + 50, y + 32, t, 18, C["m5"])
    for i, t in enumerate(rod):
        y = y0 + 116 + i * 62
        f.rect(rx + 28, y, w - 56, 50, C["hvit"], C["l3"], 1, 2)
        f.text(rx + 50, y + 32, t, 18, C["m5"])
    # parpiler: samme arbeid, to sider
    for i, j in ((1, 1), (2, 3)):
        pass
    # grense
    f.line(720, y0 - 6, 720, y0 + 572, C["m5"], 2, "3 6")
    f.arrow([(720, 778), (668, 778)], C["m5"])
    f.arrow([(720, 778), (772, 778)], C["m5"])
    f.text(720, 806, "grensen flytter seg", 15, C["gra"], anchor="middle")
    # tre vaner
    vaner = [("Prøv selv først", "tre forsøk før du spør"), ("Generer, så forstå", "spør hvorfor, kan du forklare det?"),
             ("Merk når du slutter å forstå", "varselet er vanen, ikke enkelttilfellet")]
    vw = 420
    for i, (a, b) in enumerate(vaner):
        x = 60 + i * (vw + 30)
        f.rect(x, 834, vw, 132, C["m1"], C["m5"], 1, 2)
        f.text(x + 22, 876, f"Vane {i + 1}", 15, C["gra"])
        f.h(x + 22, 908, a, 20)
        f.text(x + 22, 940, b, 16, C["m5"])
    lagre(f, "3-bevisst-bruk")


# ---------------------------------------------------------------- 4
def f4():
    f = Fig()
    ramme(f, "Fra eget oppsett til felles verktøy",
          "Tilpasninger modnes hos den enkelte og i teamet før de deles i hele SSB",
          ["Oversikt", "FORSLAG"], "Slik kommer noe i katalogen",
          [("Bruk det selv", ["Det som har virket i noen uker,", "er klart for neste steg."]),
           ("Del i teamet", ["Andre prøver og snubler.", "Rett det de snubler i."]),
           ("Gjennom porten", ["KI-gruppen sjekker: ingen data,", "ingen hemmeligheter, en eier,", "i tråd med retningslinjene."]),
           ("Status synes", ["Til utprøving, anbefalt eller", "utgått. Katalogen holdes liten."])],
          [("flate", "Nivå"), ("data", "Tilpasning"), ("rolle", "Eier"), ("mork", "Kontrollpunkt"), ("pil", "Modning")],
          BUNN)
    typer = ["Instruksjon", "Skill", "Agent", "MCP-server"]
    kol = [(60, 360, "Personlig", "din egen maskin og dine repoer", "deg"),
           (470, 360, "Team", "teamets repo", "teamet"),
           (1000, 380, "Felles katalog", "hele SSB, med eier og status", "navngitt eier")]
    for x, w, navn, under, eier in kol:
        f.rect(x, 196, w, 770, C["m1"], C["m5"], 1, 2)
        f.h(x + 24, 240, navn, 24)
        f.text(x + 24, 270, under, 16, C["gra"])
        for i, t in enumerate(typer):
            y = 310 + i * 96
            f.rect(x + 24, y, w - 48, 72, C["g1"], C["g4"], 1, 2)
            f.text(x + 46, y + 44, t, 18, C["m5"], "Roboto, Arial, sans-serif", 700)
        f.text(x + 24, 720, "Eier", 15, C["gra"])
        f.brikke(x + 24, 734, eier, "rolle", 15)
    f.arrow([(424, 560), (466, 560)], C["m5"], 2)
    # port
    px = 868
    f.rect(px, 196, 92, 770, C["m5"], "none", 0, 2)
    f.text(px + 46, 250, "Port", 20, C["hvit"], "Roboto, Arial, sans-serif", 700, "middle")
    sj = ["ingen", "data", "", "ingen", "hemme-", "ligheter", "", "eier", "finnes", "", "følger", "reglene"]
    f.lines(px + 46, 310, sj, 15, C["hvit"], anchor="middle", lh=22)
    f.arrow([(834, 560), (866, 560)], C["m5"])
    f.arrow([(962, 560), (996, 560)], C["m5"])
    # status
    y = 800
    x = 1024
    f.text(x, y, "Status", 15, C["gra"])
    w1 = f.brikke(x, y + 14, "Til utprøving", "flate", 15)
    f.arrow([(x + w1 + 4, y + 28), (x + w1 + 28, y + 28)], C["m5"])
    w2 = f.brikke(x + w1 + 32, y + 14, "Anbefalt", "data", 15)
    f.brikke(x, y + 60, "Utgått", "uavklart", 15)
    f.text(x + 100, y + 78, "når den ikke vedlikeholdes", 15, C["gra"])
    lagre(f, "4-katalog")


# ---------------------------------------------------------------- 5
def f5():
    f = Fig()
    ramme(f, "Måle, lære, justere",
          "Innsikt gjør at retningslinjer og veiledning endres i takt med hvordan KI faktisk brukes",
          ["Oversikt", "FORSLAG"], "Hvorfor sløyfen",
          [("Vi vet lite i dag", ["Ikke hvor mange som bruker KI,", "til hva, til hvilken kostnad, eller", "om det hjelper."]),
           ("Enkelt først", ["Månedlige tall og en kort", "oppsummering. Ikke dashbord", "før vi vet hva som er nyttig."]),
           ("Spørsmål er data", ["Det folk lurer på, viser hva", "veiledningen mangler."]),
           ("Aldri enkeltpersoner", ["Tall per team bare når teamet", "er stort nok. Samme prinsipp", "som i statistikken."])],
          [("flate", "Steg i sløyfen"), ("data", "Kilde"), ("rolle", "Bruker"), ("pil", "Rekkefølge"), ("pilstiplet", "Gir grunnlag for")],
          BUNN)
    cx, cy = 730, 580
    noder = {
        "bruk": (cx, 250, "Bruk", ["i seksjonene og teamene"], "rolle"),
        "male": (cx + 400, cy, "Måle", ["bruk, kostnad,", "erfaring, avvik"], "flate"),
        "laere": (cx, 910, "Lære", ["nyheter hver måned,", "halvårlig gjennomgang"], "flate"),
        "justere": (cx - 400, cy, "Justere", ["retningslinjer,", "veiledning, katalog"], "flate"),
    }
    bw, bh = 300, 120
    for k, (x, y, t, l, typ) in noder.items():
        boks(f, x - bw / 2, y - bh / 2, bw, bh, t, l, typ, size=22, tsize=16)
    f.arrow([(cx + bw / 2 + 6, 250), (cx + 400, 250), (cx + 400, cy - bh / 2 - 4)])
    f.arrow([(cx + 400, cy + bh / 2 + 4), (cx + 400, 910), (cx + bw / 2 + 6, 910)])
    f.arrow([(cx - bw / 2 - 6, 910), (cx - 400, 910), (cx - 400, cy + bh / 2 + 4)])
    f.arrow([(cx - 400, cy - bh / 2 - 4), (cx - 400, 250), (cx - bw / 2 - 6, 250)])
    # kilder i midten
    f.h(cx, 440, "Kilder", 20, anchor="middle")
    kilder = ["Lisens- og bruksdata", "Repoer med tilpasninger", "Kartlegging etter KI-forordningen",
              "Spørreundersøkelse", "Spørsmål og avvik"]
    for i, k in enumerate(kilder):
        w = len(k) * 15 * 0.58 + 24
        f.brikke(cx - w / 2, 464 + i * 46, k, "data", 15)
    f.arrow([(cx + 190, 600), (cx + 244, 600)], C["gra"], dash=STIPLET)
    lagre(f, "5-innsikt")


# ---------------------------------------------------------------- 6
def f6():
    f = Fig()
    ramme(f, "Hva gruppen koordinerer",
          "KI-gruppen eier ikke reglene, kursene eller plattformen, men holder dem sammen",
          ["Oversikt", "FORSLAG"], "Gruppens rolle",
          [("Koordinere, ikke eie", ["Eierne av regler, opplæring og", "plattform er de samme som før."]),
           ("Ett sted å spørre", ["Gruppen svarer, eller finner", "den som kan svare."]),
           ("Samme ord overalt", ["Kurs, kartlegging og nettsted", "skal bruke de samme begrepene."]),
           ("Uavklart", ["Medlemmer, mandat og kanal", "for kontakt må på plass."])],
          [("rolle", "Gruppe og eiere"), ("flate", "Tiltak"), ("uavklart", "Uavklart"), ("pil", "Koordinerer"), ("pilstiplet", "Innspill")],
          BUNN)
    cx, cy = 730, 580
    f.rect(cx - 190, cy - 85, 380, 170, C["l1"], C["l3"], 2, 2)
    f.rect(cx - 190, cy - 85, 380, 5, C["l3"], "none", 0, 0)
    f.h(cx, cy - 22, "KI-gruppen", 26, C["lt"], "middle")
    f.text(cx, cy + 12, "avdeling 700", 17, C["m5"], anchor="middle")
    f.text(cx, cy + 44, "nettstedet · katalog · innsikt", 16, C["gra"], anchor="middle")
    bw, bh = 330, 150
    rundt = [
        (cx - 470, 270, "Retningslinjer", ["eies av sikkerhet,", "personvernombud, jus"], "uavklart", "pil"),
        (cx, 250, "Opplæring", ["Copilot-kurs,", "KI for ledere"], "flate", "pil"),
        (cx + 470, 270, "AI Act-kartlegging", ["metodeledelsen,", "risikoklassifisering"], "flate", "pil"),
        (cx - 470, 890, "Plattform", ["Dapla-teamet,", "KI-funksjoner i Dapla Lab"], "uavklart", "pil"),
        (cx, 910, "Seksjonene", ["utviklere og statistikere", "som bruker verktøyene"], "rolle", "inn"),
        (cx + 470, 890, "Lisenser og innkjøp", ["hvem bestemmer", "hvilke verktøy"], "uavklart", "inn"),
    ]
    for x, y, t, l, typ, pil in rundt:
        boks(f, x - bw / 2, y - bh / 2, bw, bh, t, l, typ, size=21, tsize=16)
        # linje fra sentrum til boks
        sx = cx + (0 if x == cx else (150 if x > cx else -150))
        sy = cy - 85 if y < cy else cy + 85
        ex = x
        ey = y + bh / 2 + 4 if y < cy else y - bh / 2 - 4
        if pil == "pil":
            f.arrow([(sx, sy), (ex, ey)], C["m5"])
        else:
            f.arrow([(ex, ey), (sx, sy + (-4 if y < cy else 4))], C["gra"], dash=STIPLET)
    lagre(f, "6-gruppen")


if __name__ == "__main__":
    os.makedirs(UT, exist_ok=True)
    for fn in sys.argv[1:] or ["f0", "f1", "f2", "f3", "f4", "f5", "f6"]:
        globals()[fn]()
