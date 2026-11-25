# MCP-servere

<p class="ingress">En MCP-server gir et KI-verktøy tilgang til noe utenfor samtalen: en database, et API, et filsystem. Det gjør verktøyet mye mer nyttig, og det åpner en ny dør. Derfor bruker vi bare servere som står her.</p>

## Godkjente servere

| Server | Gir tilgang til | Datanivå | Status |
|---|---|---|---|
| SSB statistikkbank | Søk, metadata og uttrekk fra publiserte tabeller | Åpent | <span class="status avklares">Avklares: eier og godkjenning</span> |
| GitHub | Repoer, issues og pull requests i statisticsnorway | Åpent / internt | <span class="status avklares">Avklares</span> |

## Hva vi ser etter før en server godkjennes

- **Hva den kan lese.** Bare data på åpent eller internt nivå.
- **Hva den kan gjøre.** Lesetilgang er enklere å godkjenne enn skrivetilgang.
- **Hvem som har laget den.** Egenutviklet, fra leverandør vi har avtale med, eller fra en ukjent tredjepart.
- **Hvor den kjører.** Lokalt, i SSBs miljø, eller hos en ekstern tjeneste.

## Ønsker du en ny server?

Se [Slik bidrar du](bidra.md). Skriv hva serveren skal brukes til, og hvilke data den får tilgang til.
