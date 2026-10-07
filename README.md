# intro-python

## pavlo pavlovskyi

## Værapplikasjon

Jeg laget et enkelt program som viser været i en by.

Først spør programmet brukeren om å skrive navnet på en by.

Programmet bruker `requests` for å hente data fra internett. Værdata kommer fra Open-Meteo API, som er en tjeneste for værinformasjon.

Først bruker programmet Open-Meteo for å finne koordinatene til byen. Etterpå bruker det koordinatene for å hente dagens værdata. Programmet viser temperaturen som er nå.

Jeg bruker en `while`-løkke slik at programmet fortsetter å spørre om nye byer. Etter at temperaturen vises, kan brukeren skrive en ny by.

Hvis brukeren skriver en by som ikke finnes, viser programmet en enkel feilmelding.

Jeg bruker også `try` og `except`. Hvis programmet ikke klarer å hente værdata fra internett, får brukeren en feilmelding.

For å stoppe programmet skriver brukeren `avbryt`. Da bruker programmet `break`, og løkken stopper.
