# Om forslaget

<p class="ingress">SSB har nå to forsøk på det samme. ki-praksis har guidene, forankringen og driften. ssb-ki-utvikling har rammen: innganger, områder og oversikt. Denne versjonen viser hvordan de kan bli én portal, og hva som må endres i ki-praksis for å komme dit.</p>

!!! warning "Versjon 2, skisse til diskusjon"
    Dette er et forslag fra KI-gruppen, ikke en ny portal. Målet er at alt innhold til slutt ligger i ki-praksis på `ki-praksis.intern.ssb.no`. Dette nettstedet er et verksted for å vise strukturen før noe bygges der.

## Hvorfor de to hører sammen

Begge bygger på Navs nettsted [ki-utvikling.nav.no](https://ki-utvikling.nav.no/), men på hvert sitt nivå. ki-praksis følger Navs seksjon *Praksis*: et bibliotek med guider, søk og kort. ssb-ki-utvikling fulgte toppnivået: kom i gang, regler, tilpasning og innsikt. Hver for seg mangler de det den andre har. Sammen blir de hele modellen.

| | ki-praksis | ssb-ki-utvikling |
|---|---|---|
| Styrke | 24 guider, forankret i ADR-er, driftet på intranettet | Innganger etter målgruppe, områder, oversiktsfigurer, bevisst bruk |
| Svakhet | Lite orientering: hvor begynner jeg, og hvordan henger det sammen? | Ingen forankring, feil verktøyliste i versjon 1, ligger utenfor intranettet |
| Rolle i forslaget | Portalen og innholdet | Rammen og de nye delene |

## Slik leser du merkene

Hver side og hver guide i forslaget har én av fire merker:

| Merke | Betyr |
|---|---|
| <span class="status kp">Fra ki-praksis</span> | Finnes i ki-praksis og flyttes inn som den er |
| <span class="status endres">Endres</span> | Finnes i ki-praksis, men vi foreslår et tillegg eller en endring |
| <span class="status nytt">Nytt</span> | Finnes ikke i ki-praksis. Kommer fra ssb-ki-utvikling |
| <span class="status venter">Venter</span> | Plassen er reservert, men innholdet venter på en avklaring |

Lenker til guidene i ki-praksis virker bare på SSBs interne nett.

## Det vi bygger på

Plasseringen av guidene bygger på filnavnene i `content/guides/`, verktøylisten i `content/data/verktoy.json` og README-en i ki-praksis, slik de var 25.11.2026. Reglene bygger på ADR0035 og ADR0038, som er lest. Selve guidene er ikke lest ennå. Når de er lest, kan noen av forslagene vise seg å være overflødige.

## Videre

- [Samlet struktur](struktur.md): alle sider og guider på sin plass.
- [Endringer i ki-praksis](endringer.md): de konkrete endringene, i prioritert rekkefølge.
