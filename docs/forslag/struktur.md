# Samlet struktur

<p class="ingress">Alle 24 guidene i ki-praksis, sidene om verktøy og modeller, og de nye delene fra ssb-ki-utvikling, plassert i én struktur med ni områder.</p>

<figure class="figur" id="figur-0" markdown="span">
  [![Samlet struktur for ki-praksis. Ni områder med guidene fra ki-praksis og de nye delene plassert](../figurer/0-samlet-struktur.svg){ loading=lazy }](../figurer/0-samlet-struktur.svg)
  <figcaption>Figur 0. Samlet struktur for ki-praksis · <a href="../figurer/0-samlet-struktur.svg" download>Last ned SVG</a></figcaption>
</figure>

## Fra kategorier til områder

ki-praksis har i dag seks kategorier i `src/lib/guides.ts`: `start`, `verktoy`, `regler`, `koding`, `kvalitet` og `oppsett`. Forslaget gjør dem om til områder, med tre endringer:

- `start` og `verktoy` slås sammen til **Kom i gang**.
- `koding` og `kvalitet` slås sammen til **Praksis**, slik Nav gjør.
- `oppsett` får navnet **Tilpasning**, fordi guidene handler om filer som tilpasser agentene, ikke om installasjon.

To nye kategorier kommer til: `bevisst` og `statistiker`.

## Alle sider og guider

| Område | Side eller guide | Merke | Merknad |
|---|---|---|---|
| **Start** | Forside (`/`) | <span class="status endres">Endres</span> | Innganger etter målgruppe og hovedregelen øverst |
| **Regler** | [regler-for-ki-bruk](https://ki-praksis.intern.ssb.no/praksis/regler-for-ki-bruk) | <span class="status endres">Endres</span> | Vedtatte regler fra ADR0035 i en tabell, hovedregelen og figur 1 |
| | [data-og-personvern](https://ki-praksis.intern.ssb.no/praksis/data-og-personvern) | <span class="status endres">Endres</span> | Tillegg om taushetsplikt og upubliserte tall |
| | [beskytt-repoet](https://ki-praksis.intern.ssb.no/praksis/beskytt-repoet) | <span class="status kp">Fra ki-praksis</span> | |
| | Verktøy (`/verktoy`) | <span class="status endres">Endres</span> | Datanivå og en egen gruppe for verktøy som venter |
| | Modeller (`/modeller`) | <span class="status kp">Fra ki-praksis</span> | |
| | Endringslogg | <span class="status nytt">Nytt</span> | Kan bygges fra `updated` i guidene |
| **Kom i gang** | [kom-i-gang](https://ki-praksis.intern.ssb.no/praksis/kom-i-gang) | <span class="status kp">Fra ki-praksis</span> | Blir inngangen for utviklere |
| | [oppsett-vs-code](https://ki-praksis.intern.ssb.no/praksis/oppsett-vs-code) | <span class="status kp">Fra ki-praksis</span> | |
| | [oppsett-opencode](https://ki-praksis.intern.ssb.no/praksis/oppsett-opencode) | <span class="status kp">Fra ki-praksis</span> | |
| | [andre-klienter](https://ki-praksis.intern.ssb.no/praksis/andre-klienter) | <span class="status kp">Fra ki-praksis</span> | |
| | [velg-modell](https://ki-praksis.intern.ssb.no/praksis/velg-modell) | <span class="status kp">Fra ki-praksis</span> | |
| | [spar-kostnader](https://ki-praksis.intern.ssb.no/praksis/spar-kostnader) | <span class="status kp">Fra ki-praksis</span> | |
| **Tilpasning** | [filer-agentene-leser](https://ki-praksis.intern.ssb.no/praksis/filer-agentene-leser) | <span class="status endres">Endres</span> | Figur 7 |
| | [skriv-agents-md](https://ki-praksis.intern.ssb.no/praksis/skriv-agents-md) | <span class="status kp">Fra ki-praksis</span> | |
| | [lag-instruksjonsfiler](https://ki-praksis.intern.ssb.no/praksis/lag-instruksjonsfiler) | <span class="status kp">Fra ki-praksis</span> | |
| | [lag-promptfiler](https://ki-praksis.intern.ssb.no/praksis/lag-promptfiler) | <span class="status kp">Fra ki-praksis</span> | |
| | [lag-skills](https://ki-praksis.intern.ssb.no/praksis/lag-skills) | <span class="status kp">Fra ki-praksis</span> | |
| | [lag-agenter](https://ki-praksis.intern.ssb.no/praksis/lag-agenter) | <span class="status kp">Fra ki-praksis</span> | |
| | [forbered-repoet](https://ki-praksis.intern.ssb.no/praksis/forbered-repoet) | <span class="status kp">Fra ki-praksis</span> | |
| **Praksis** | [skriv-presise-prompts](https://ki-praksis.intern.ssb.no/praksis/skriv-presise-prompts) | <span class="status kp">Fra ki-praksis</span> | |
| | [forsta-eksisterende-kode](https://ki-praksis.intern.ssb.no/praksis/forsta-eksisterende-kode) | <span class="status kp">Fra ki-praksis</span> | |
| | [store-endringer](https://ki-praksis.intern.ssb.no/praksis/store-endringer) | <span class="status kp">Fra ki-praksis</span> | Kan få en figur over flyten senere |
| | [feilsoking](https://ki-praksis.intern.ssb.no/praksis/feilsoking) | <span class="status kp">Fra ki-praksis</span> | |
| | [verifiser-og-test](https://ki-praksis.intern.ssb.no/praksis/verifiser-og-test) | <span class="status kp">Fra ki-praksis</span> | |
| | [gjennomga-ki-kode](https://ki-praksis.intern.ssb.no/praksis/gjennomga-ki-kode) | <span class="status kp">Fra ki-praksis</span> | |
| | [styrker-og-begrensninger](https://ki-praksis.intern.ssb.no/praksis/styrker-og-begrensninger) | <span class="status endres">Endres</span> | Lenke videre til Bevisst bruk |
| **Bevisst bruk** | Grønn og rød sone | <span class="status nytt">Nytt</span> | Merkes som forslag, ingen ADR som kilde |
| | KI-kompetanse | <span class="status nytt">Nytt</span> | Kilde: KI-forordningen artikkel 4 |
| **For statistikere** | Inngang for statistikere som koder | <span class="status venter">Venter</span> | Utenfor ADR0038. Lisens via S724 |
| **Nytt og innsikt** | Nyheter, måling | <span class="status nytt">Nytt</span> | Kan komme senere |
| **Om** | KI-gruppen, slik bidrar du, ordliste | <span class="status nytt">Nytt</span> | |
| | [ressurser](https://ki-praksis.intern.ssb.no/praksis/ressurser) | <span class="status kp">Fra ki-praksis</span> | Flyttes hit fra guidene |

## Oppsummert

Av 24 guider flyttes 20 inn som de er, og 4 får et tillegg. Ingen guider foreslås fjernet eller skrevet om. Det meste av endringen ligger rundt guidene: forsiden, områdene og de nye delene.
