# KI-utvikling i SSB

**Versjon 2.1.** Forslag til samlet struktur for [ki-praksis](https://github.com/statisticsnorway/ki-praksis): guidene derfra plassert i rammen fra dette nettstedet (innganger, områder, oversiktsfigurer, bevisst bruk). Laget som diskusjonsgrunnlag for KI-gruppen i avdeling 700. Ingenting her er vedtatt, og målet er at det som vedtas flyttes inn i ki-praksis.

Versjon 1 ligger under taggen `v1`.

Bygget med [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) og publisert på GitHub Pages med GitHub Actions.

## Struktur

```
docs/
  index.md               forside
  forslag/               om forslaget, samlet struktur, endringer i ki-praksis
  regler/                verktøy og datanivå, data og taushetsplikt, endringslogg
  kom-i-gang/            områdeside med guidene fra ki-praksis
  tilpasning/            områdeside, filer agentene leser (figur 7)
  praksis/               områdeside med guidene fra ki-praksis
  bevisst-bruk/          grønn og rød sone, KI-kompetanse (nytt)
  statistikere/          venter, med utkastet fra v1
  innsikt/               måling, nyheter
  om/                    gruppen, slik bidrar du, ordliste
  figurer/               oversiktsfigurer (SVG, 1920 x 1080)
verktoy/
  kf.py                  byggeklosser for konseptfigurer
  figurer.py             tegner figurene: python3 verktoy/figurer.py
```

## Lokalt

```
pip install -r requirements.txt
mkdocs serve
```

## Merking i teksten

- `<span class="status forslag">Forslag</span>` for gruppens forslag
- `<span class="status avklares">Avklares</span>` for det som ikke er avklart
- `<span class="status finnes">Pågår</span>` for det som finnes eller pågår
- `<span class="status kp">Fra ki-praksis</span>`, `endres`, `nytt`, `venter` for plassering av innhold fra ki-praksis

Søk etter `status avklares` for å finne alt som må avklares.

Strukturen er inspirert av [ki-utvikling.nav.no](https://ki-utvikling.nav.no/).
