# Hva er lov, og hva er ikke lov

<p class="ingress">Korte lister for de vanligste spørsmålene. Er du i tvil om noe som ikke står her, gjelder hovedregelen: se på hvilke data det gjelder, og spør hvis du ikke vet.</p>

!!! warning "Forslag"
    Listene er gruppens forslag, laget med Navs retningslinjer som forbilde. Hvilke tjenester SSB faktisk har avtale med, og på hvilke vilkår, må bekreftes. <span class="status avklares">Avklares</span>

## Tillatt

- Microsoft 365 Copilot Chat med jobbkontoen, for tekst, oppsummering og spørsmål om åpne og interne dokumenter. <span class="status avklares">Avklares: hvilke lisenser</span>
- GitHub Copilot i editoren (VS Code, JupyterLab) for kode som ikke inneholder data. <span class="status avklares">Avklares: hvem har lisens</span>
- Agentmodus lokalt, i tråd med [Agenter og isolasjon](agenter.md).
- MCP-servere som står i [katalogen](../katalog/mcp.md).
- Å be KI forklare, dokumentere, teste og rydde i kode du selv har ansvaret for.
- Å bruke KI til å lage syntetiske testdata, så lenge de ikke bygger på ekte mikrodata.

## Tillatt med vilkår

- **Kodeagenter som lager endringer på egen hånd** (for eksempel Copilot coding agent). Vilkår: endringen kommer som en pull request som et menneske leser og godkjenner før fletting.
- **Intern dokumentasjon og møtenotater** i M365 Copilot. Vilkår: innholdet er ikke taushetsbelagt eller unntatt offentlighet av andre grunner.
- **Egne instruksjoner og skills i et repo.** Vilkår: de inneholder ikke hemmeligheter, tilgangsnøkler eller data.

## Ikke tillatt

- Taushetsbelagte data, mikrodata eller upubliserte tall i et KI-verktøy som ikke er særskilt godkjent for det.
- Private abonnement (ChatGPT Plus, Claude Pro og liknende) til jobbformål.
- Gratisversjoner og forbrukertjenester der leverandøren kan bruke innholdet til trening.
- MCP-servere og utvidelser fra tredjeparter som ikke står i katalogen.
- Agenter som kjører uten avgrensning på maskiner med tilgang til produksjonsdata.
- Å la KI ta beslutninger om publisering, konfidensialitet eller prikking uten menneskelig kontroll.

## Spørsmål vi får

??? question "Kan jeg lime inn en feilmelding?"
    Ja, hvis feilmeldingen ikke inneholder data. Pass på stack traces som skriver ut verdier fra en dataramme. Fjern dem eller bytt dem ut før du limer inn.

??? question "Kan jeg vise KI strukturen på et datasett?"
    Kolonnenavn, datatyper og variabelbeskrivelser fra metadata er som regel greit. Verdier er ikke det. Bruk `df.dtypes` eller et syntetisk utdrag, ikke `df.head()`.

??? question "Kan jeg bruke KI til å skrive en tekst som skal publiseres?"
    Ja, som hjelp. Tall, tolkninger og formuleringer i publisert statistikk er ditt og seksjonens ansvar, og må kontrolleres på vanlig måte. <span class="status avklares">Avklares: om KI-bruk skal merkes</span>

??? question "Hva med KI-funksjoner i Dapla eller Google Cloud?"
    <span class="status avklares">Avklares</span> Dette må vurderes for seg, fordi det gjelder plattformen der dataene ligger. Gruppen tar dette opp med Dapla-teamet.
