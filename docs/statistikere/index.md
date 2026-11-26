# For statistikere

<p class="ingress">De fleste som skriver kode i SSB, er statistikere. De koder i Dapla Lab, ofte i notebooks, tett på dataene. Reglene og guidene i resten av portalen er skrevet for applikasjonsutvikling. Dette området skal bli inngangen for statistikerne.</p>

!!! info "Venter"
    <span class="status venter">Venter</span> Statistikersporet er satt på vent i KI-gruppen. Området er reservert, så det synes at det kommer. Til da: les [Regler](../regler/index.md) og [Data og taushetsplikt](../regler/data.md) før du bruker KI-verktøy på kode i Dapla.

## Hva sporet venter på

- **Hvilke verktøy som er tillatt i Dapla Lab.** ADR0038 gjelder utviklere på ekspertteam med tech lead, og nevner ikke JupyterLab, RStudio eller Positron. Se [Verktøy og datanivå](../regler/verktoy.md).
- **Hvem som avgjør.** ADR0038 sier at andre som trenger lisens, skal kontakte leveranseansvarlig: seksjonslederen i S724, seksjon for dataplattform. Det gjør S724 til den naturlige eieren av spørsmålet, og sannsynligvis av sporet.
- **Om plattformen må vurderes på nytt.** ADR0038 valgte bort Google Vertex AI. Dapla kjører på Google Cloud. KI i Dapla kan derfor kreve en egen vurdering.
- **Hvordan data holdes unna agentene** når kode og data ligger i samme miljø.
- **Hvem som eier innholdet.** Sannsynligvis S724 sammen med noen fra statistikkproduksjonen, ikke bare utviklerne.

## Det som allerede finnes som utkast

Fra versjon 1 av ssb-ki-utvikling finnes et [utkast til inngang](utkast.md): den viktigste regelen, fem ting KI er god til, tre ting den ikke skal gjøre, et eksempel og kontroll av tall. Utkastet er ikke forankret, men kan brukes som utgangspunkt når sporet starter.

## Hva som kan gjenbrukes

Mye av ki-praksis gjelder statistikere også: *skriv-presise-prompts*, *forsta-eksisterende-kode*, *verifiser-og-test* og *styrker-og-begrensninger*. Inngangen for statistikere bør lenke dit, ikke skrive det på nytt. Det nye er det som gjelder data, notebooks og faglige valg.
