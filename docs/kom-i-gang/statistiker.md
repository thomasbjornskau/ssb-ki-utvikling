# Kom i gang for statistikere som koder

<p class="ingress">Du er ekspert på statistikken din, ikke nødvendigvis på Python. Det gjør KI ekstra nyttig: den kan forklare koden du har arvet, foreslå tester og hjelpe deg med pandas-syntaksen du aldri husker. Men du sitter også tettere på dataene enn de fleste, og det krever litt ekstra omtanke.</p>

## Den viktigste regelen først

**Vis KI koden og strukturen, aldri dataene.** I en notebook ligger data og kode tett sammen. En `df.head()` i output, en feilmelding med verdier, en kopi av en celle med resultater: alt dette er data. Les [Data og taushetsplikt](../retningslinjer/data.md) før du begynner.

## Fem ting KI er god til for deg

**1. Forklare kode du har arvet.** Lim inn en funksjon og spør hva den gjør, linje for linje. Spør så hvorfor den er skrevet slik. Du lærer mer av det andre spørsmålet.

**2. Oversette fra SAS eller R.** Mange produksjonsløp flyttes fra SAS til Python på Dapla. KI er god til å oversette syntaks. Den er dårligere til å vite om resultatet blir likt. Kjør begge og sammenlign, alltid.

**3. Skrive tester.** Be om tester for funksjonene dine, basert på syntetiske data. Tester er den beste måten å oppdage at en oversettelse eller endring ikke gjør det du trodde.

**4. Rydde i en notebook.** Be KI foreslå hvordan en lang notebook kan deles i funksjoner. Det gjør koden lettere å teste og lettere å overlevere.

**5. Forklare feilmeldinger.** Lim inn feilmeldingen, ikke dataene. Fjern verdier fra stack trace først.

## Tre ting KI ikke skal gjøre for deg

- **Velge metode.** KI kan forklare forskjellen på to metoder, men valget er faglig og ditt.
- **Vurdere om tallene er rimelige.** Plausibilitetskontroll krever at du kjenner statistikken. KI gjør ikke det.
- **Bestemme prikking.** Konfidensialitetsbehandling er en menneskelig beslutning. Se [Ansvar](../retningslinjer/ansvar.md).

## Et eksempel

!!! example "Fra spørsmål til test"
    *Ikke slik:* «Hvorfor blir summen feil?» med `df.head(20)` limt inn.

    *Men slik:* «Her er funksjonen som summerer omsetning per næring. Datarammen har kolonnene `orgnr` (str), `nace` (str), `omsetning` (float). Summen per næring blir høyere enn totalen. Hva kan være årsaken? Lag en test med syntetiske data som viser feilen.»

    Det andre spørsmålet inneholder ingen data, og gir et bedre svar.

## Neste steg

- [Gode instruksjoner](instruksjoner.md)
- [Kontroll før bruk](kontroll.md)
- [Grønn og rød sone](../bevisst-bruk/soner.md)
