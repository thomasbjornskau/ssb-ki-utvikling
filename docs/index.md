# KI i utvikling i SSB

<p class="ingress">KI-verktøy skriver allerede kode, forklarer feilmeldinger og foreslår tester hos oss. Denne portalen sier hva som er lov, hvordan det gjøres godt, og hvor vi deler det vi lærer. Den samler regler, oppsett og guider på ett sted, forankret i SSBs arkitekturbeslutninger.</p>

!!! warning "Versjon 2: forslag til samlet struktur"
    Dette er et forslag til hvordan **ki-praksis** kan få en overordnet struktur med innganger og områder. Guidene finnes allerede i ki-praksis. Merkene viser hva som kommer derfra <span class="status kp">Fra ki-praksis</span>, hva som foreslås endret <span class="status endres">Endres</span>, hva som er nytt <span class="status nytt">Nytt</span> og hva som venter <span class="status venter">Venter</span>. Les mer i [Om forslaget](forslag/index.md).

## Hovedregelen

**Start med dataene, ikke med verktøyet.** Spør først om det du arbeider med er åpent, internt eller taushetsbelagt. Deretter hvilket verktøy som er tillatt for det. Et tillatt verktøy gjør ikke taushetsbelagte data trygge å lime inn. <span class="status nytt">Nytt</span> <span class="status avklares">Ingen ADR dekker dette ennå</span>

## Hvem er du?

<div class="kort" markdown>
<div markdown>
[Utvikler](kom-i-gang/index.md)

Du lager applikasjoner, plattformer eller tjenester. Begynn med å sette opp verktøyet, og les deretter om filene som tilpasser agentene.

<span class="status kp">Fra ki-praksis</span>
</div>
<div markdown>
[Statistiker som koder](statistikere/index.md)

Du skriver Python eller R i Dapla for å produsere statistikk. Egen inngang kommer. Til da: les reglene om data først.

<span class="status venter">Venter</span>
</div>
<div markdown>
[Leder](regler/index.md)

Du har ansvar for at teamet bruker KI forsvarlig. Les reglene og om KI-kompetanse.

<span class="status nytt">Nytt</span>
</div>
</div>

## Hvor bør du begynne?

| Du vil … | Begynn her | Deretter |
|---|---|---|
| Vite om noe er lov | [Regler](regler/index.md) | [Verktøy og datanivå](regler/verktoy.md) |
| Komme i gang med Copilot | [Kom i gang](kom-i-gang/index.md) | [Tilpasning](tilpasning/index.md) |
| Få agenten til å følge teamets regler | [Tilpasning](tilpasning/index.md) | [Filer agentene leser](tilpasning/filer.md) |
| Løse en konkret oppgave med KI | [Praksis](praksis/index.md) | [Bevisst bruk](bevisst-bruk/index.md) |
| Vite hva som er nytt | [Endringslogg](regler/endringslogg.md) | [Nytt og innsikt](innsikt/index.md) |
| Bidra | [Om](om/index.md) | |

## Områdene

<figure class="figur" id="figur-0" markdown="span">
  [![Samlet struktur for ki-praksis. Ni områder med guidene fra ki-praksis og de nye delene plassert](figurer/0-samlet-struktur.svg){ loading=lazy }](figurer/0-samlet-struktur.svg)
  <figcaption>Figur 0. Samlet struktur for ki-praksis · <a href="figurer/0-samlet-struktur.svg" download>Last ned SVG</a></figcaption>
</figure>

<div class="kort" markdown>
<div markdown>
[Regler](regler/index.md)

Hva som er tillatt, hvilke data som kan gå hvor, og hvordan du beskytter repoet.
</div>
<div markdown>
[Kom i gang](kom-i-gang/index.md)

Tilgang, oppsett av editor og terminal, valg av modell og kostnader.
</div>
<div markdown>
[Tilpasning](tilpasning/index.md)

AGENTS.md, instruksjonsfiler, promptfiler, skills og agenter. Slik får verktøyet kontekst.
</div>
<div markdown>
[Praksis](praksis/index.md)

Prompter, forstå kode, store endringer, feilsøking, test og review.
</div>
<div markdown>
[Bevisst bruk](bevisst-bruk/index.md)

Når KI sparer tid, og når den tar fra deg forståelsen du trenger.
</div>
<div markdown>
[For statistikere](statistikere/index.md)

Inngang for dem som koder statistikkproduksjon i Dapla. Kommer.
</div>
</div>
