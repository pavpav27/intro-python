main = True

handleliste = []

while main:
    print("")
    print("######## MENY ########")
    print("1. legg til vare      #")
    print("2. skriv ut alle varene   #")
    print("3. fjern vare fra listen  #")
    print("0. avslutt            #")
    print("######################")
    print("")

    valg = input("velg ett nummer fra menyen: ")

    if valg == "0":
        break

    elif valg == "1":
        nyVare = input("legg til en vare: ")
        handleliste.append(nyVare)

    elif valg == "2":
        print(handleliste)

    elif valg == "3":
        vare = input("skriv inn vare du ønsker å fjerne: ")
        handleliste.remove(vare)

    input("trykk enter for å fortsette")