# Kontroll før bruk

<p class="ingress">KI-generert kode ser riktig ut. Det er både styrken og problemet. Den er velformatert, godt navngitt og selvsikker, også når den er feil. Kontrollen må derfor gjøres med vilje, ikke på magefølelse.</p>

## Sjekkliste

Før du tar i bruk kode fra KI, bør du kunne svare ja på disse:

- [ ] **Jeg kan forklare hva koden gjør**, linje for linje, til en kollega.
- [ ] **Koden er testet**, og testene ville feilet hvis koden var feil.
- [ ] **Jeg har sjekket at funksjoner og pakker finnes.** KI finner av og til opp funksjoner og parametre som høres riktige ut.
- [ ] **Resultatet er sammenlignet** med en kjent fasit, eller med den gamle løsningen, når koden erstatter noe.
- [ ] **Ingen hemmeligheter, stier eller data** har sneket seg inn i koden.
- [ ] **Endringen har vært gjennom review** av et menneske, hvis den skal i produksjon.

## Særlig for statistikk

Kode som produserer statistikk kan være feil uten å feile. Den kjører, gir tall, og tallene er litt galt. Derfor:

- Sammenlign totaler og antall før og etter endringen.
- Se på fordelinger, ikke bare summer.
- Kjør gammel og ny løsning parallelt på samme data når du oversetter eller skriver om.
- La en som kjenner statistikken vurdere om endringen i tallene er rimelig.

## Når du ikke rekker å kontrollere

Da skal du ikke bruke koden. Det er ikke strengt, det er bare ærlig. Kode du ikke har kontrollert, er kode du ikke kan stå for. Se [Ansvar](../retningslinjer/ansvar.md).
