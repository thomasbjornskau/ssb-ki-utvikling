# Instruksjoner og skills

<p class="ingress">Første utgave av katalogen. Listen er et forslag til hva som kan stå her, med eksempler vi vet finnes. Eiere og status må bekreftes.</p>

## Instruksjoner

| Navn | Gjelder | Eier | Status |
|---|---|---|---|
| Python i Dapla | Repoer med statistikkproduksjon i Python | <span class="status avklares">Avklares</span> | <span class="status forslag">Forslag</span> |
| R i Dapla | Repoer med statistikkproduksjon i R | <span class="status avklares">Avklares</span> | <span class="status forslag">Forslag</span> |
| SSBs kodestandard | Alle repoer | <span class="status avklares">Avklares</span> | <span class="status forslag">Forslag</span> |
| Ikke vis data | Notebooks: minner om å tømme output og ikke lime inn verdier | KI-gruppen | <span class="status forslag">Forslag</span> |

## Skills

| Navn | Hva den gjør | Eier | Status |
|---|---|---|---|
| Diagramstandard | Lager og vurderer diagrammer etter SSBs regler | Thomas Bjørnskau | Til utprøving |
| Konseptfigurer | Tegner konseptfigurer (arkitektur, prosess, ansvar) i SSBs profil | Thomas Bjørnskau | Til utprøving |
| Dataflyt | Kartlegger og tegner dataflyt for statistikker | Thomas Bjørnskau | Til utprøving |
| SAS til Python | Oversetter SAS-kode og lager sammenligningstest | <span class="status avklares">Avklares</span> | <span class="status forslag">Forslag</span> |

!!! note "Om eksemplene"
    Skillsene fra Thomas er laget for personlig bruk og må ryddes før de deles. De står her for å vise hva en skill kan være i SSB.

## Slik ser en instruksjonsfil ut

```markdown
# Instruksjoner for dette repoet

Dette er produksjonskoden for statistikken <navn>, i Dapla.

- Python 3.12, pandas 2. Ikke foreslå nye avhengigheter uten å spørre.
- Testene ligger i tests/ og kjøres med pytest.
- Funksjoner skal ha typehint og docstring på norsk.
- Ikke les eller vis innhold fra data/. Bruk syntetiske data i tester.
- Endringer i beregninger skal ha en test som viser forskjellen.
```
