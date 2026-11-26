# Endringer i ki-praksis

<p class="ingress">De konkrete endringene forslaget krever, i den rekkefølgen vi mener de bør gjøres. De første gir mest orientering for minst arbeid. De siste kan vente.</p>

!!! note "Grunnlag"
    Forslagene bygger på README, filnavn og `verktoy.json` i ki-praksis, og på ADR0035 og ADR0038. Forsiden (`src/app/page.tsx`) og guidene er ikke lest. Noe kan allerede være løst.

## Utenfor ki-praksis, men viktigst

**0. Tillegg om data i ADR0035.** <span class="status nytt">Nytt</span>
Ingen ADR sier hvilke data som kan gå inn i KI-verktøyene. Uten det kan verken hovedregelen, datanivåene eller tillegget om taushetsplikt stå som regel i ki-praksis, bare som forslag. KI-gruppen bør be om et tillegg i [ADR0035](https://github.com/statisticsnorway/adr/blob/main/docs/0035-retningslinjer-for-sikker-koding.md), som gjelder agentiske kodeverktøy allerede.
*Hvem:* tech leads, Sikkerhetssenteret og seksjon for IT-arkitektur, som har myndighet over ADR0035. *Grunnlag:* [Data og taushetsplikt](../regler/data.md).

## Først: orientering

**1. Forsiden får innganger etter målgruppe.** <span class="status endres">Endres</span>
I dag har forsiden fem steg for å komme i gang og innganger til innholdet. Forslaget er å legge til hvem siden er for, en tabell over hvor du bør begynne, og hovedregelen: start med dataene, ikke verktøyet. Se [forsiden i dette forslaget](../index.md).
*Hvor:* `src/app/page.tsx`. *Arbeid:* lite.

**2. Kategoriene blir områder med egen side.** <span class="status endres">Endres</span>
Hver kategori får en egen side med en ingress, en oversiktsfigur og listen over guidene, på samme måte som områdesidene her. Guidebiblioteket med søk beholdes som det er.
*Hvor:* `src/lib/guides.ts` (kategoriene), en ny rute for områdene, menyen. *Arbeid:* middels.

**3. Ny endringslogg.** <span class="status nytt">Nytt</span>
Alle guidene har allerede `updated` i frontmatter. En side som lister guidene etter siste endring, gir en endringslogg nesten gratis.
*Hvor:* en ny rute, for eksempel `/nytt`. *Arbeid:* lite.

## Deretter: innhold

**4. Tillegg om taushetsplikt i *data-og-personvern*, og vedtatte regler i *regler-for-ki-bruk*.** <span class="status endres">Endres</span>
Statistikklovens taushetsplikt og regelen om at upubliserte tall alltid er taushetsbelagte. Gjelder også utviklere, ikke bare statistikere. Står som forslag til punkt 0 er på plass. De fem reglene fra ADR0035 kan derimot stå som regler nå, samlet i én tabell. Se [Regler](../regler/index.md).

**5. Datanivå og «ikke tillatt» på verktøysiden.** <span class="status endres">Endres</span>
Vise hvilke data som kan gå inn i de tillatte verktøyene (forslag, se punkt 0), og hva som ikke er tillatt etter ADR0035: private abonnement og autonome agenter. Forslaget krever også en tredje status, `venter`, i `verktoy.json` for Dapla Lab-verktøyene, med merknad om lisens via S724. Det er en endring i skjemaet i `src/lib/data.ts`. Se [Verktøy og datanivå](../regler/verktoy.md).

**6. Figur til *filer-agentene-leser*.** <span class="status endres">Endres</span>
En oversikt over hvilke filer hvert verktøy leser. Se [Filer agentene leser](../tilpasning/filer.md).

**7. Nytt område: Bevisst bruk.** <span class="status nytt">Nytt</span>
To guider i den nye kategorien `bevisst`. *styrker-og-begrensninger* lenker videre hit. Guidene merkes som forslag fordi de ikke har en ADR som kilde.

## Senere

**8. Om-side og slik bidrar du.** <span class="status nytt">Nytt</span>
README-en forklarer godt hvordan man bidrar, men bare for den som leser repoet. En side i portalen gjør det synlig for alle. *ressurser* flyttes hit.

**9. Plass for statistikere.** <span class="status venter">Venter</span>
Et område som er synlig, men sier at innholdet kommer. ADR0038 holder statistikere utenfor og viser til S724, seksjon for dataplattform. Området bør si det, så statistikere vet hvem de skal spørre. Fylles når statistikersporet starter.

**10. Nytt og innsikt.** <span class="status nytt">Nytt</span>
Månedlige nyheter og tall om bruk. Avhenger av hvem som skal skrive dem.

## Det vi ikke foreslår å endre

Selve guidene, kravet om kilde for hver regel, datafilene for verktøy og modeller, Designsystemet og driften på NAIS. Det fungerer, og forslaget bygger på det.

## Åpne spørsmål

- **Figurene og Designsystemet.** Konseptfigurene følger SSBs profil. Portalen bruker Designsystemet. Skal figurene tilpasses portalen, eller er SSB-profilen riktig for figurer?
- **Hvem eier områdetekstene?** Guidene har eiere gjennom kildene. Ingressene og forsiden har ikke det.
