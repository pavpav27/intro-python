import requests

while True:
    by = input("Skriv en by eller 'avbryt': ")

    if by.lower() == "avbryt":
        print("Programmet avsluttes.")
        break

    try:
        geo = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": by, "count": 1}
        ).json()

        if "results" not in geo:
            print("Byen finnes ikke.")
            continue

        lat = geo["results"][0]["latitude"]
        lon = geo["results"][0]["longitude"]

        vaer = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lon,
                "current": "temperature_2m"
            }
        ).json()

        temperatur = vaer["current"]["temperature_2m"]

        print("Temperaturen i", by, "er", temperatur, "°C")

    except:
        print("Kunne ikke hente været.")