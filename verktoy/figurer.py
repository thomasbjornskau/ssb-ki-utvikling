"""Tegner oversiktsfigurene til nettstedet. Kjør: python3 verktoy/figurer.py"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from kf import Fig, ramme, boks, C, F_MELLOM, F_TEKST, STIPLET, FORSLAG

UT = os.path.join(os.path.dirname(__file__), "..", "docs", "figurer")
BUNN = "26.11.2026 · Versjon 2.1, skisse til diskusjon · KI-gruppen, avdeling 700"


def lagre(f, navn):
    open(os.path.join(UT, navn + ".svg"), "w", encoding="utf-8").write(f.svg())
    print("ok", navn)


# ---------------------------------------------------------------- 0
def f0():
    f = Fig()
    ramme(f, "Samlet struktur for ki-praksis",
          "Guidene fra ki-praksis i rammen fra ssb-ki-utvikling: ni områder i én portal",
          ["Oversikt", "FORSLAG"], "Slik leser du figuren",
          [("Guidene er de samme", ["20 av 24 guider flyttes inn", "som de er. Ingen fjernes", "eller skrives om."]),
           ("Fire guider får tillegg", ["Regler, data, filene agentene", "leser og styrker og", "begrensninger."]),
           ("Rammen er ny", ["Forside med innganger, områder", "med ingress og figur, og fire", "nye områder."]),
           ("Statistikere venter", ["Plassen er reservert, så det", "synes at inngangen kommer."])],
          [("kp", "Fra ki-praksis"), ("endres", "Endres"), ("forslag", "Nytt"), ("uavklart", "Venter")],
          BUNN)
    # start
    f.rect(60, 196, 1340, 84, C["hvit"], C["l3"], 1, 2)
    f.h(84, 234, "Start", 22, C["lt"])
    f.text(84, 262, "Forside: hvem er du, hovedregelen, hvor bør du begynne", 16, C["m5"])
    f.brikke(1240, 222, "Endres", "endres", 14)
    omr = [
        ("Regler", "regler", "kp", [("regler-for-ki-bruk", "endres"), ("data-og-personvern", "endres"), ("beskytt-repoet", "kp"),
                                     ("/verktoy", "endres"), ("/modeller", "kp"), ("endringslogg", "forslag")]),
        ("Kom i gang", "start + verktoy", "kp", [("kom-i-gang", "kp"), ("oppsett-vs-code", "kp"), ("oppsett-opencode", "kp"),
                                                 ("andre-klienter", "kp"), ("velg-modell", "kp"), ("spar-kostnader", "kp")]),
        ("Tilpasning", "oppsett", "kp", [("filer-agentene-leser", "endres"), ("skriv-agents-md", "kp"), ("lag-instruksjonsfiler", "kp"),
                                          ("lag-promptfiler", "kp"), ("lag-skills", "kp"), ("lag-agenter", "kp"), ("forbered-repoet", "kp")]),
        ("Praksis", "koding + kvalitet", "kp", [("skriv-presise-prompts", "kp"), ("forsta-eksisterende-kode", "kp"), ("store-endringer", "kp"),
                                                 ("feilsoking", "kp"), ("verifiser-og-test", "kp"), ("gjennomga-ki-kode", "kp"),
                                                 ("styrker-og-begrensninger", "endres")]),
        ("Bevisst bruk", "ny kategori", "forslag", [("grønn og rød sone", "forslag"), ("KI-kompetanse", "forslag")]),
        ("For statistikere", "ny kategori", "uavklart", [("inngang i Dapla", "uavklart"), ("utkast fra v1", "uavklart")]),
        ("Nytt og innsikt", "senere", "forslag", [("nyheter", "forslag"), ("måling", "forslag")]),
        ("Om", "ny side", "forslag", [("KI-gruppen", "forslag"), ("slik bidrar du", "forslag"), ("ordliste", "forslag"), ("ressurser", "kp")]),
    ]
    cw, gap = 320, 20
    for i, (navn, kat, typ, chips) in enumerate(omr):
        r, c = divmod(i, 4)
        x = 60 + c * (cw + gap)
        y = 300 if r == 0 else 690
        h = 370 if r == 0 else 276
        fi, st, da, tc = {"kp": (C["m1"], C["m5"], None, C["m5"]), "forslag": (C["l1"], C["l3"], FORSLAG, C["lt"]),
                          "uavklart": (C["hvit"], C["ustrek"], STIPLET, C["gra"])}[typ]
        f.rect(x, y, cw, h, fi, st, 1, 2, da)
        f.h(x + 20, y + 38, navn, 21, tc)
        f.text(x + 20, y + 62, kat, 14, C["gra"])
        for j, (ch, ct) in enumerate(chips):
            f.brikke(x + 20, y + 80 + j * 38, ch, ct, 14)
    lagre(f, "0-samlet-struktur")


# ---------------------------------------------------------------- 1
def f1():
    f = Fig()
    ramme(f, "Verktøy og datanivå",
          "Verktøystatusen har kilde i ADR0035 og ADR0038. Datanivåene har ingen kilde ennå",
          ["Oversikt", "FORSLAG"], "Fire ting å merke seg",
          [("Status har kilde", ["Tillatt, avklares og ikke tillatt", "kommer fra ADR0035, ADR0038", "og verktoy.json."]),
           ("Ingen ADR dekker data", ["Datanivåene er et forslag.", "KI-gruppen bør be om et", "tillegg i ADR0035."]),
           ("Taushetsbelagt: nei", ["Ingen tillatte verktøy skal få", "mikrodata eller upubliserte tall."]),
           ("Dapla Lab er det åpne", ["Statistikere er utenfor", "ADR0038. Lisens via S724,", "seksjon for dataplattform."])],
          [("data", "Tillatt"), ("vilkar", "Med vilkår"), ("nei", "Ikke tillatt"), ("uavklart", "Avklares eller venter"), ("forslag", "Forslag uten kilde")],
          BUNN)
    grupper = [("Tillatt", "ADR0038", ["VS Code", "OpenCode", "Zed", "GitHub.com"], "kp"),
               ("Avklares", "tech leads avgjør", ["JetBrains", "Copilot CLI"], "uavklart"),
               ("Venter", "lisens via S724", ["JupyterLab", "RStudio, Positron"], "uavklart"),
               ("Ikke tillatt", "ADR0035", ["private abonnement", "autonome agenter"], "nei")]
    rad = [("Åpent", ["Publisert statistikk,", "åpen kode"]), ("Internt", ["Kode uten data,", "dokumentasjon, metadata"]),
           ("Taushetsbelagt", ["Mikrodata,", "upubliserte tall"])]
    V = [[("Ja", "", "ja"), ("?", "avklares", "uavklart"), ("?", "venter", "uavklart"), ("Nei", "", "nei")],
         [("Med vilkår", "se beskytt-repoet", "vilkar"), ("?", "avklares", "uavklart"), ("?", "venter", "uavklart"), ("Nei", "", "nei")],
         [("Nei", "", "nei"), ("Nei", "", "nei"), ("?", "kode og data", "uavklart"), ("Nei", "", "nei")]]
    x0, y0, cw, ch, hh = 300, 196, 270, 196, 196
    for j, (navn, kilde, verk, typ) in enumerate(grupper):
        x = x0 + j * cw
        if typ == "kp":
            f.rect(x + 6, y0, cw - 12, hh - 14, C["m1"], C["m5"], 1, 2); tc = C["m5"]
        elif typ == "nei":
            f.rect(x + 6, y0, cw - 12, hh - 14, C["ufyll"], C["ustrek"], 1, 2); tc = C["m5"]
        else:
            f.rect(x + 6, y0, cw - 12, hh - 14, C["hvit"], C["ustrek"], 1, 2, STIPLET); tc = C["gra"]
        f.h(x + 24, y0 + 38, navn, 21, tc)
        f.text(x + 24, y0 + 64, kilde, 15, C["gra"])
        cx, cy = x + 24, y0 + 80
        for v in verk:
            w = len(v) * 14 * 0.58 + 24
            if cx + w > x + cw - 14:
                cx, cy = x + 24, cy + 36
            ct = {"kp": "kp", "uavklart": "uavklart", "nei": "flate"}[typ]
            f.brikke(cx, cy, v, ct, 14)
            cx += w + 8
    f.h(82, y0 + 38, "Data", 18, C["g4"])
    f.text(82, y0 + 64, "nedover", 15, C["gra"])
    for i, (navn, tx) in enumerate(rad):
        y = y0 + hh + i * ch
        f.rect(60, y + 6, 5, ch - 12, C["g4"], "none", 0, 0)
        f.h(82, y + 48, navn, 20, C["g4"])
        f.lines(82, y + 82, tx, 15, C["m5"], lh=21)
        for j in range(4):
            t, u, typ = V[i][j]
            x = x0 + j * cw
            cx, cy = x + cw / 2, y + ch / 2
            if typ == "ja":
                f.rect(x + 6, y + 6, cw - 12, ch - 12, C["g1"], C["g4"], 1, 2); tc = C["g4"]
            elif typ == "vilkar":
                f.rect(x + 6, y + 6, cw - 12, ch - 12, C["hvit"], C["g4"], 1, 2)
                f.rect(x + 6, y + 6, 5, ch - 12, C["g4"], "none", 0, 0); tc = C["g4"]
            elif typ == "nei":
                f.rect(x + 6, y + 6, cw - 12, ch - 12, C["ufyll"], C["ustrek"], 1, 2); tc = C["rod"]
            else:
                f.rect(x + 6, y + 6, cw - 12, ch - 12, C["hvit"], C["ustrek"], 1, 2, STIPLET); tc = C["gra"]
            f.text(cx, cy + (0 if u else 10), t, 26, tc, F_MELLOM, 700, "middle")
            if u:
                f.text(cx, cy + 32, u, 15, C["m5"] if typ != "uavklart" else C["gra"], anchor="middle")
    # datanivåene er forslag: lilla stiplet ramme rundt radetikettene
    f.rect(54, y0 + hh, 232, 3 * ch, "none", C["l3"], 1, 2, FORSLAG)
    lagre(f, "1-verktoy-og-datanivaa")


# ---------------------------------------------------------------- 7
def f7():
    f = Fig()
    ramme(f, "Hvilke filer leser hvilket verktøy",
          "Forslag til figur i guiden filer-agentene-leser. Spørsmålstegnene må fylles ut",
          ["Oversikt", "FORSLAG"], "Hva figuren skal vise",
          [("AGENTS.md først", ["Den felles filen. Skriv den", "først, så får verktøyene", "samme grunnkontekst."]),
           ("Resten varierer", ["Instruksjonsfiler, promptfiler", "og skills virker fullt ut bare", "i noen verktøy."]),
           ("Review er et eget tilfelle", ["GitHub.com leser", "copilot-instructions.md", "ved code review."]),
           ("Fyll ut spørsmålstegnene", ["Figuren bygger bare på", "verktoy.json. Resten må", "hentes fra guiden."])],
          [("data", "Leser"), ("vilkar", "Delvis"), ("uavklart", "Ukjent, fylles ut")],
          "Kilde: verktoy.json i ki-praksis, 11.11.2026 · " + BUNN.split(" · ", 1)[1])
    filer = [("AGENTS.md", "felles standard"), ("Instruksjonsfiler", "copilot-instructions.md,", "*.instructions.md"),
             ("Promptfiler", "*.prompt.md"), ("Skills", "SKILL.md")]
    verk = [("VS Code", "editor"), ("OpenCode", "terminal"), ("Zed", "editor"), ("GitHub.com", "web")]
    V = [["ja", "ja", "ja", "ja"],
         ["ja", "?", "?", "?"],
         ["?", "?", "?", "?"],
         ["?", ("delvis", "copilot-instructions.md", "ved code review"), "?", "?"]]
    x0, y0, cw, rh, hh = 300, 196, 270, 170, 116
    for j, fl in enumerate(filer):
        x = x0 + j * cw
        f.rect(x + 6, y0, cw - 12, hh - 14, C["g1"], C["g4"], 1, 2)
        f.h(x + 24, y0 + 38, fl[0], 20, C["g4"])
        f.lines(x + 24, y0 + 64, list(fl[1:]), 14, C["m5"], lh=19)
    for i, (v, t) in enumerate(verk):
        y = y0 + hh + i * rh
        f.rect(60, y + 6, 222, rh - 12, C["m1"], C["m5"], 1, 2)
        f.h(82, y + 56, v, 21)
        f.text(82, y + 84, t, 15, C["gra"])
        for j in range(4):
            c = V[i][j]
            x = x0 + j * cw
            cx, cy = x + cw / 2, y + rh / 2
            if c == "ja":
                f.rect(x + 6, y + 6, cw - 12, rh - 12, C["g1"], C["g4"], 1, 2)
                f.text(cx, cy + 9, "Leser", 24, C["g4"], F_MELLOM, 700, "middle")
            elif isinstance(c, tuple):
                f.rect(x + 6, y + 6, cw - 12, rh - 12, C["hvit"], C["g4"], 1, 2)
                f.rect(x + 6, y + 6, 5, rh - 12, C["g4"], "none", 0, 0)
                f.text(cx, cy - 10, "Delvis", 24, C["g4"], F_MELLOM, 700, "middle")
                f.text(cx, cy + 20, c[1], 14, C["m5"], anchor="middle")
                f.text(cx, cy + 40, c[2], 14, C["m5"], anchor="middle")
            else:
                f.rect(x + 6, y + 6, cw - 12, rh - 12, C["hvit"], C["ustrek"], 1, 2, STIPLET)
                f.text(cx, cy + 9, "?", 26, C["gra"], F_MELLOM, 700, "middle")
    lagre(f, "7-filer-agentene-leser")


# ---------------------------------------------------------------- 2
def f2():
    f = Fig()
    ramme(f, "To innganger, ett felles grunnlag",
          "Utviklere følger guidene i ki-praksis. Statistikersporet venter, men ender i samme vane",
          ["Oversikt", "FORSLAG"], "Hvorfor to innganger",
          [("Utviklere: finnes", ["Guidene i ki-praksis dekker", "veien fra tilgang til review.", "ADR0038 gjelder her."]),
           ("Statistikere: venter", ["I Dapla ligger kode og data", "sammen. Sporet trenger egne", "avklaringer og står på vent."]),
           ("Samme vane til slutt", ["Begge spor ender i kontroll før", "bruk: forstå, teste, sammenligne."]),
           ("Reglene ligger under", ["Ingen av stegene kan gi mer", "rom enn reglene gir."])],
          [("rolle", "Hvem"), ("flate", "Steg, med guide i ki-praksis"), ("uavklart", "Venter"), ("data", "Felles vane"), ("pil", "Rekkefølge")],
          BUNN)
    spor = [
        (80, "Utvikler", "plattform, tjenester, avd. 700",
         [("Kom i gang", "kom-i-gang"), ("Sett opp verktøyet", "oppsett-vs-code, oppsett-opencode"),
          ("Gi agenten kontekst", "skriv-agents-md, forbered-repoet"), ("Store endringer med plan", "store-endringer")]),
        (740, "Statistiker som koder", "Python eller R i Dapla · venter",
         [("Vis kode, ikke data", "struktur, ikke verdier"), ("Forklar og oversett", "arvet kode, SAS til Python"),
          ("Tester med syntetiske data", "så feil blir synlige"), ("Faglige valg selv", "metode, plausibilitet, prikking")]),
    ]
    bw = 600
    for x, navn, under, steg in spor:
        venter = x > 400
        f.rect(x, 196, bw, 92, C["l1"], C["l3"], 1, 2, FORSLAG if venter else None)
        f.rect(x, 196, 5, 92, C["l3"], "none", 0, 0)
        f.h(x + 26, 236, navn, 22, C["lt"])
        f.text(x + 26, 268, under, 16, C["m5"])
        y = 318
        for i, (a, b) in enumerate(steg):
            f.arrow([(x + bw / 2, y - 28), (x + bw / 2, y - 2)])
            if venter:
                f.rect(x + 40, y, bw - 80, 76, C["hvit"], C["ustrek"], 1, 2, STIPLET)
            else:
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
    f.text(110, yk + 80, "verifiser-og-test · gjennomga-ki-kode · forstå hver linje før du bruker den", 17, C["m5"])
    # retningslinjer
    f.rect(80, 884, 1260, 82, C["m5"], "none", 0, 2)
    f.h(110, 934, "Regler", 20, C["hvit"])
    f.text(220, 934, "regler-for-ki-bruk · data-og-personvern · beskytt-repoet · ADR0035, ADR0038", 17, C["hvit"])
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
          "Tilpasninger modnes hos den enkelte og i teamet før de havner i github-copilot",
          ["Oversikt", "FORSLAG"], "Slik kommer noe i katalogen",
          [("Bruk det selv", ["Det som har virket i noen uker,", "er klart for neste steg."]),
           ("Del i teamet", ["Andre prøver og snubler.", "Rett det de snubler i."]),
           ("Gjennom porten", ["Ingen data, ingen hemmeligheter,", "en eier, i tråd med reglene.", "Hvem som sier ja, er uavklart."]),
           ("Status synes", ["Til utprøving, anbefalt eller", "utgått. Katalogen holdes liten."])],
          [("flate", "Nivå"), ("data", "Tilpasning"), ("rolle", "Eier"), ("mork", "Kontrollpunkt"), ("pil", "Modning")],
          BUNN)
    typer = ["Instruksjon", "Skill", "Agent", "MCP-server"]
    kol = [(60, 360, "Personlig", "din egen maskin og dine repoer", "deg"),
           (470, 360, "Team", "teamets repo", "teamet"),
           (1000, 380, "github-copilot", "felles for SSB, vist i ki-praksis", "navngitt eier")]
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
    f.text(x, y, "Status (forslag)", 15, C["gra"])
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
          "KI-gruppen eier ikke reglene, kursene eller driften, men holder ki-praksis samlet",
          ["Oversikt", "FORSLAG"], "Gruppens rolle",
          [("Koordinere, ikke eie", ["Eierne av regler, opplæring og", "plattform er de samme som før."]),
           ("Ett sted å spørre", ["Gruppen svarer, eller finner", "den som kan svare."]),
           ("Samme ord overalt", ["Kurs, kartlegging og nettsted", "skal bruke de samme begrepene."]),
           ("Uavklart", ["Hvem eier strukturen og", "områdetekstene? Kanal for", "kontakt må på plass."])],
          [("rolle", "Gruppe og eiere"), ("flate", "Tiltak"), ("uavklart", "Uavklart"), ("pil", "Koordinerer"), ("pilstiplet", "Innspill")],
          BUNN)
    cx, cy = 730, 580
    f.rect(cx - 190, cy - 85, 380, 170, C["l1"], C["l3"], 2, 2)
    f.rect(cx - 190, cy - 85, 380, 5, C["l3"], "none", 0, 0)
    f.h(cx, cy - 22, "KI-gruppen", 26, C["lt"], "middle")
    f.text(cx, cy + 12, "avdeling 700", 17, C["m5"], anchor="middle")
    f.text(cx, cy + 44, "struktur i ki-praksis", 16, C["gra"], anchor="middle")
    bw, bh = 330, 150
    rundt = [
        (cx - 470, 270, "Regler", ["ADR0035, ADR0038,", "github-copilot"], "flate", "pil"),
        (cx, 250, "Opplæring", ["Copilot-kurs,", "KI for ledere"], "flate", "pil"),
        (cx + 470, 270, "AI Act-kartlegging", ["metodeledelsen,", "risikoklassifisering"], "flate", "pil"),
        (cx - 470, 890, "Drift og plattform", ["ki-plattform drifter portalen,", "Dapla for statistikersporet"], "flate", "pil"),
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
    for fn in sys.argv[1:] or ["f0", "f1", "f2", "f3", "f4", "f5", "f6", "f7"]:
        globals()[fn]()
