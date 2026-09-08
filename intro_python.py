# generer ett random tall

# 10 forsøk

import random

rettTall = random.randint(0, 1000)


for forsok in range(1, 11):
    gjett = int(input("Gjett et tall mellom 0 og 1000: "))

    if gjett == rettTall:
        print("Riktig! Du fant tallet!")
        break

    forsok_igjen = 10 - forsok
    print("Du har", forsok_igjen, "forsøk igjen.")

else:
    print("Du har brukt opp alle forsøkene.")
    print("Du har tapt.")