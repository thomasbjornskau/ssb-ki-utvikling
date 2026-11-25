# Agenter og isolasjon

<p class="ingress">En chatbot svarer. En agent handler: den leser filer, kjører kommandoer og gjør endringer. Det er derfor den er nyttig, og det er derfor den trenger grenser.</p>

!!! warning "Forslag"
    Kravene her er inspirert av Navs krav om sandkasse for agenter. Hvordan de skal løses teknisk i SSB, er ikke avklart. <span class="status avklares">Avklares</span>

## Hvorfor det er et eget tema

Når en agent kjører i terminalen din, har den de samme rettighetene som deg. Den kan lese det du kan lese, og den kan sende det videre til modellen. Den kan også bli lurt. Tekst i en fil, en nettside eller et issue kan inneholde instruksjoner som agenten følger. Dette kalles promptinjeksjon, og det finnes ingen fullgod beskyttelse mot det i dag.

Det betyr ikke at agenter er for farlige å bruke. Det betyr at de skal brukes i et rom der skaden er begrenset hvis noe går galt.

## Krav

1. **Avgrenset filtilgang.** Agenten skal bare se repoet den arbeider i, ikke hele hjemmeområdet.
2. **Ingen tilgang til hemmeligheter.** Tilgangsnøkler, tokens og passord skal ikke ligge der agenten kan lese dem.
3. **Ingen tilgang til data på taushetsbelagt nivå.** Agenter skal ikke kjøre i miljøer der de kan nå mikrodata. <span class="status avklares">Avklares: hva det betyr i Dapla Lab</span>
4. **Godkjenning av handlinger med konsekvens.** Push, sletting og kall mot eksterne tjenester skal kreve et ja fra deg.
5. **Endringer via pull request.** Agenter som jobber på egen hånd, leverer en pull request som et menneske godkjenner.

## Nivåer av selvstendighet

| Nivå | Hva agenten gjør | Krav |
|---|---|---|
| Forslag | Foreslår kode i editoren | Ingen utover vanlige regler |
| Agentmodus | Endrer filer og kjører kommandoer i repoet ditt, du ser alt | Avgrenset filtilgang, godkjenning av kommandoer |
| Selvstendig | Arbeider alene på en oppgave og leverer en pull request | Isolert miljø, review før fletting |

## Det vi ikke har løst

Nav har laget sin egen sandkasse for agenter. Vi har ikke det, og det er ikke sikkert vi trenger å lage en selv. Gruppen vil kartlegge hva verktøyene og plattformen allerede tilbyr, før vi foreslår noe nytt.
