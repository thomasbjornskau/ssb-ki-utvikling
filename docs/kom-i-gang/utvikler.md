# Kom i gang for utviklere

<p class="ingress">Du kan sannsynligvis allerede få Copilot til å fullføre en funksjon. Denne siden handler om neste steg: å gi agenten nok kontekst til at den passer inn i SSBs måte å gjøre ting på, og nok grenser til at du kan stole på det den gjør.</p>

## 1. Skaff tilgang

<span class="status avklares">Avklares</span> Hvordan du får GitHub Copilot-lisens i SSB, og hvilke modeller som er tilgjengelige. Lenke til bestilling kommer her.

## 2. Legg til instruksjoner i repoet

Uten instruksjoner gir agenten generiske råd. Med en fil som `.github/copilot-instructions.md` i repoet kan du fortelle den:

- hvilke språk, rammeverk og versjoner repoet bruker
- hvordan tester kjøres
- navnekonvensjoner og mønstre teamet følger
- hva den ikke skal røre (for eksempel genererte filer eller infrastruktur)

Start med ti linjer. Legg til når du ser at agenten gjør samme feil to ganger. I [katalogen](../katalog/tilpasninger.md) finner du eksempler fra andre team.

## 3. Bruk agentmodus med grenser

Agentmodus lar Copilot lese flere filer, kjøre kommandoer og endre kode. Før du slår det på:

- Sjekk at repoet ikke inneholder hemmeligheter eller data.
- Slå av automatisk godkjenning av kommandoer.
- Les [Agenter og isolasjon](../retningslinjer/agenter.md).

## 4. Be om plan før kode

Ved større endringer: be agenten beskrive planen før den skriver kode. Les planen. Det er mye billigere å rette en plan enn å rette tjue filer. Det er her du eier arkitekturen og agenten implementerer.

## 5. Bruk KI i review, ikke i stedet for review

KI er god til å finne ting du ikke så: manglende feilhåndtering, inkonsekvente navn, tester som ikke tester noe. Den er dårlig til å vite om endringen var en god idé. La den lese først, og les selv etterpå.

## Neste steg

- [Kontroll før bruk](kontroll.md)
- [Instruksjoner og skills i katalogen](../katalog/tilpasninger.md)
