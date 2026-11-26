# Data og taushetsplikt

<p class="ingress">SSB får opplysninger om personer og foretak fordi vi lover å beskytte dem. Det løftet gjelder også når vi bruker KI. Denne siden deler dataene våre i tre nivåer, så det blir enklere å vite hva som kan gå hvor.</p>

<span class="status endres">Endres</span> Forslag til tillegg i guiden [data-og-personvern](https://ki-praksis.intern.ssb.no/praksis/data-og-personvern) i ki-praksis. Guiden er ikke lest ennå, så noe av dette kan stå der allerede.

!!! danger "Ingen ADR dekker dette"
    Verken ADR0035 eller ADR0038 sier noe om hvilke data som kan gå inn i KI-verktøyene. Denne siden er derfor et forslag, både til guiden og til et tillegg i ADR0035. Se [Regler](index.md#det-som-mangler-data).

!!! warning "Forslag"
    Inndelingen er gruppens forslag til en praktisk tommelfingerregel. Den erstatter ikke SSBs informasjonsklassifisering eller statistikklovens regler, og må stemmes av med sikkerhet og personvernombud. Etter kildekravet i ki-praksis står den som forslag til den har en kilde. <span class="status avklares">Avklares</span>

## Tre nivåer

| Nivå | Eksempler | KI-verktøy |
|---|---|---|
| **Åpent** | Publisert statistikk, statistikkbanken, åpen kode på GitHub, offentlige dokumenter | Alle tillatte verktøy |
| **Internt** | Intern dokumentasjon, kode i interne repo uten data, møtenotater, metadata og variabelbeskrivelser | Tillatte verktøy, med reglene i *beskytt-repoet* |
| **Taushetsbelagt** | Mikrodata, opplysninger om enkeltpersoner og enkeltforetak, upubliserte tall, prikket informasjon før prikking | Ingen. Om det skal finnes en egen løsning, er uavklart |

## Upubliserte tall er et eget problem

Statistikk som ikke er publisert, er ikke bare et personvernspørsmål. Den er markedssensitiv, og den er omfattet av løftet om lik tilgang ved publisering. Et KI-verktøy som får se tallene før publisering, er et brudd på det løftet. Det gjelder også om tallene er aggregerte og ikke sier noe om enkeltpersoner.

Tommelfingerregelen er enkel: **før publisering er alle tall taushetsbelagte**, uansett aggregeringsnivå.

## Slik jobber du uten å dele data

- **Vis strukturen, ikke innholdet.** Kolonnenavn, datatyper og antall rader holder ofte for at KI skal hjelpe.
- **Lag syntetiske data.** Be KI lage et testdatasett med samme struktur. Da har du også noe å skrive tester mot.
- **Hent metadata, ikke data.** Variabeldefinisjoner fra metadatasystemene er som regel åpne eller interne.
- **Hold notebooks rene.** En notebook som er delt med KI, tar med seg output. Tøm output før du ber om hjelp med en notebook.
- **Hold data utenfor det agenten leser.** Se [beskytt-repoet](https://ki-praksis.intern.ssb.no/praksis/beskytt-repoet). Hvordan dette gjøres i Dapla Lab, venter på statistikersporet. <span class="status venter">Venter</span>

## Hvis noe har gått galt

Har du limt inn noe du ikke skulle, si fra med det samme. Det er bedre å melde et avvik som viser seg å være ufarlig, enn å la være. Bruk vanlig avviksrutine. <span class="status avklares">Avklares: lenke til avviksrutine</span>
