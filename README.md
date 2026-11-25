# KI-utvikling i SSB

Skisse til et nettsted med regler, veiledning og felles verktøy for bruk av KI i utvikling og statistikkproduksjon i SSB. Laget som diskusjonsgrunnlag for KI-gruppen i avdeling 700. Ingenting her er vedtatt.

Bygget med [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) og publisert på GitHub Pages med GitHub Actions.

## Struktur

```
docs/
  index.md               forside
  retningslinjer/        hva er lov, data, ansvar, agenter, endringslogg
  kom-i-gang/            utviklere, statistikere, instruksjoner, kontroll
  bevisst-bruk/          grønn og rød sone, KI-kompetanse
  katalog/               instruksjoner og skills, MCP-servere, bidra
  innsikt/               måling, nyheter
  om/                    gruppen, ordliste
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

Søk etter `status avklares` for å finne alt som må avklares.

Strukturen er inspirert av [ki-utvikling.nav.no](https://ki-utvikling.nav.no/).
