def vis_startmeny():
    print("\n--- STARTMENY ---")
    print("1. Logg inn")
    print("2. Registrer bruker")
    print("3. Avslutt")

    valg = input("Velg: ")

    if valg == "1":
        return "innlogget"
    elif valg == "2":
        print("Registrering kommer senere")
        return "start"
    elif valg == "3":
        return "quit"
    else:
        print("Feil valg")
        return "start"


def vis_innlogget_meny():
    print("\n--- INNLOGGET ---")
    print("1. Få en vits")
    print("2. Logg ut")

    valg = input("Velg: ")

    if valg == "1":
        print("Vits kommer senere")
        return "innlogget"
    elif valg == "2":
        return "start"
    else:
        print("Feil valg")
        return "innlogget"


def main():
    state = "start"

    while state != "quit":

        if state == "start":
            state = vis_startmeny()

        elif state == "innlogget":
            state = vis_innlogget_meny()

    print("Programmet avsluttes")


main()