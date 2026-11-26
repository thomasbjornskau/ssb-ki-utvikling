# Verktøy og datanivå

<p class="ingress">Verktøysiden i ki-praksis sier hvilke verktøy som er tillatt. Den sier ikke hvilke data du kan bruke dem med. Forslaget er å legge til datanivået, og å gi verktøyene statistikerne bruker en egen plass, selv om svaret ennå ikke finnes.</p>

<span class="status endres">Endres</span> Gjelder `/verktoy` og `content/data/verktoy.json` i ki-praksis.

## Verktøyene i dag

Fra `verktoy.json`, oppdatert 11.11.2026. Kilde for alle: [ADR0038](https://github.com/statisticsnorway/adr/blob/main/docs/0038-bruk-av-agentiske-kodeverktøy-i-applikasjonsutvikling.md), som velger GitHub Copilot Business og nevner VS Code, GitHub, OpenCode og Zed.

| Verktøy | Type | Status | Merknad |
|---|---|---|---|
| VS Code | Editor | <span class="status finnes">Tillatt</span> | Copilot Chat og agentmodus |
| OpenCode | Terminal | <span class="status finnes">Tillatt</span> | Agent i terminalen, med Copilot-lisensen |
| Zed | Editor | <span class="status finnes">Tillatt</span> | Innebygd agent, med Copilot-lisensen |
| GitHub.com | Web | <span class="status finnes">Tillatt</span> | Copilot Chat og code review |
| IntelliJ / JetBrains | Editor | <span class="status avklares">Avklares</span> | Ikke nevnt i ADR0038. Tech leads avgjør |
| Copilot CLI | Terminal | <span class="status avklares">Avklares</span> | Ikke nevnt i ADR0038. Tech leads avgjør |

## Ikke tillatt

| Hva | Kilde |
|---|---|
| Private abonnement og modeller utenom de sentralt administrerte lisensene | [ADR0035](https://github.com/statisticsnorway/adr/blob/main/docs/0035-retningslinjer-for-sikker-koding.md) |
| Agenter som arbeider på egen hånd uten at du godkjenner hver handling | [ADR0035](https://github.com/statisticsnorway/adr/blob/main/docs/0035-retningslinjer-for-sikker-koding.md) |

<span class="status endres">Endres</span> Forslag: verktøysiden viser også dette, så det er tydelig hva som ikke er lov, ikke bare hva som er det.

## Forslag 1: datanivå

Legg til hvilke data verktøyene kan brukes med. Samme svar gjelder alle tillatte verktøy, så det kan stå én gang over tabellen, ikke per verktøy:

| Datanivå | Eksempler | Tillatte verktøy |
|---|---|---|
| **Åpent** | Publisert statistikk, åpen kode, offentlige dokumenter | Ja |
| **Internt** | Kode i interne repoer uten data, dokumentasjon, metadata | Ja, med reglene i *beskytt-repoet* |
| **Taushetsbelagt** | Mikrodata, opplysninger om personer og foretak, upubliserte tall | Nei |

<span class="status nytt">Nytt</span> Inndelingen har ingen kilde. Verken ADR0035 eller ADR0038 sier noe om data. Den står derfor som forslag til den er tatt inn i en ADR. Se [Regler](index.md#det-som-mangler-data).

## Forslag 2: verktøy som venter

Statistikere skriver kode i Dapla Lab, ofte i JupyterLab, RStudio eller Positron. ADR0038 definerer utviklere som kodere på ekspertteam med en tech lead, som utvikler applikasjoner lokalt. Andre som mener de trenger lisens, skal kontakte leveranseansvarlig: seksjonslederen i S724, seksjon for dataplattform. Verktøyene bør stå på verktøysiden likevel, med en egen status, så det synes at spørsmålet er kjent:

| Verktøy | Type | Status | Merknad |
|---|---|---|---|
| JupyterLab i Dapla Lab | Notebook | <span class="status venter">Venter</span> | Lisens via S724 |
| RStudio / Positron i Dapla Lab | Editor | <span class="status venter">Venter</span> | Lisens via S724 |
| VS Code i Dapla Lab | Editor | <span class="status venter">Venter</span> | Er det samme vurdering som lokalt? |

Dette krever en tredje status, `venter`, i skjemaet i `src/lib/data.ts`. I dag tillater det bare `tillatt` og `avklares`.

## Hvorfor dette er det vanskelige spørsmålet

For utviklere ligger dataene et annet sted enn koden. For statistikere i Dapla ligger de i samme miljø, ofte i samme notebook. Et verktøy som er trygt på en utviklers maskin, er ikke nødvendigvis trygt der mikrodataene er. Derfor er det riktig at dette venter på en egen vurdering, og derfor er figur 1 tydelig på at det er åpent.

Én ting til: ADR0038 vurderte Google Vertex AI og valgte den bort, blant annet fordi kostnadene er vanskeligere å styre. Dapla kjører på Google Cloud. Skal KI inn i Dapla, må det trolig vurderes for seg, ikke bare som en utvidelse av ADR0038.
