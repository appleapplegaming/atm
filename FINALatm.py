import csv


def atm_machine():
    # main program loop
    while True:
        # display the main menu and get the user's language preference
        print("Welcome to the ATM Machine")
        print("1. English")
        print("2. Español")
        print("3. Français")
        print("4. Deutsch")
        print("5. Quit")
        choice = int(input("Enter your choice: "))

        # handle the language choice
        if choice == 1:
            # set the language to English
            language = "en"
            break
        elif choice == 2:
            # set the language to Spanish
            language = "es"
            break
        elif choice == 3:
            # set the language to French
            language = "fr"
            break
        elif choice == 4:
            # set the language to German
            language = "de"
            break
        elif choice == 5:
            # quit the program
            exit()
        else:
            # if an invalid choice is entered, display an error message
            print("Invalid choice. Please try again.")

    # open the database file and read the records
    with open("atm_folder/atm_database.txt", "r") as file:
        records = file.readlines()

    # prompt the user for their username and password
    if language == "en":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
    elif language == "es":
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
    elif language == "fr":
        username = input("Entrez votre nom d'utilisateur: ")
        password = input("Entrez votre mot de passe: ")
    elif language == "de":
        username = input("Geben Sie Ihren Benutzernamen ein: ")
        password = input("Geben Sie Ihr Passwort ein: ")

    # check if the username and password match any records in the database
    match = False
    with open("atm_folder/atm_database.txt") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for data in csv_reader:
            if data[0] == username and data[1] == password:
                name = data[2]
                balance = float(data[3])
                match = True
                break
            # if no match is found, prompt the user to register
    if not match:
        if language == "en":
            print("No account found with that username and password.")
            print("Would you like to register a new account?")
            print("1. Yes")
            print("2. No")
        elif language == "es":
            print(
                "No se encontró ninguna cuenta con ese nombre de usuario y contraseña."
            )
            print("¿Te gustaría registrar una nueva cuenta?")
            print("1. Sí")
            print("2. No")
        elif language == "fr":
            print(
                "Aucun compte trouvé avec ce nom d'utilisateur et ce mot de passe.")
            print("Voulez-vous enregistrer un nouveau compte?")
            print("1. Oui")
            print("2. Non")
        elif language == "de":
            print("Kein Konto mit diesem Benutzernamen und Passwort gefunden.")
            print("Möchten Sie ein neues Konto registrieren?")
            print("1. Ja")
            print("2. Nein")

        # handle the register choice
        reg_choice = int(input("Enter your choice: "))
        if reg_choice == 1:
            # prompt the user for their name and starting balance
            if language == "en":
                name = input("Enter your name: ")
                balance = float(input("Enter your starting balance: "))
            elif language == "es":
                name = input("Ingrese su nombre: ")
                balance = float(input("Ingrese su saldo inicial: "))
            elif language == "fr":
                name = input("Entrez votre nom: ")
                balance = float(input("Entrez votre solde initial: "))
            elif language == "de":
                name = input("Geben Sie Ihren Namen ein: ")
                balance = float(input("Geben Sie Ihren Anfangskontostand ein: "))

            # add the user's record to the database
            with open("atm_folder/atm_database.txt", "a") as file:
                file.write(username + "," + password + "," + name + "," + str(balance))
                file.write("\n")
                # display a success message
            if language == "en":
                print("Your account has been registered!")
            elif language == "es":
                print("¡Su cuenta ha sido registrada!")
            elif language == "fr":
                print("Votre compte a été enregistré!")
            elif language == "de":
                print("Ihr Konto wurde registriert!")
        elif reg_choice == 2:
            # quit the program
            exit()
        else:
            # if an invalid choice is entered, display an error message
            if language == "en":
                print("Invalid choice. Please try again.")
            elif language == "es":
                print("Opción inválida. Inténtalo de nuevo.")
            elif language == "fr":
                print("Choix invalide. Veuillez réessayer.")
            elif language == "de":
                print("Ungültige Auswahl. Bitte versuche es erneut.")

    # if a match is found, display a welcome message
    if match:
        if language == "en":
            print("Welcome", name)
        elif language == "es":
            print("Bienvenido", name)
        elif language == "fr":
            print("Bienvenue", name)
        elif language == "de":
            print("Willkommen", name)

    while True:
        # handle ATM transactions
        # display the transaction menu
        if language == "en":
            print("ATM Transactions")
            print("1. Check Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Quit")
        elif language == "es":
            print("Transacciones del cajero automático")
            print("1. Ver saldo")
            print("2. Retirar")
            print("3. Depositar")
            print("4. Salir")
        elif language == "fr":
            print("Transactions ATM")
            print("1. Vérifier le solde")
            print("2. Retirer")
            print("3. Dépôt")
            print("4. Quitter")
        elif language == "de":
            print("ATM-Transaktionen")
            print("1. Kontostand prüfen")
            print("2. Abheben")
            print("3. Einzahlen")
            print("4. Beenden")

        tr_choice = int(input("Enter your choice: "))

        # handle the transaction choice
        if tr_choice == 1:
            # display the current balance
            if language == "en":
                print("Your current balance is:", balance)
            elif language == "es":
                print("Tu saldo actual es:", balance)
            elif language == "fr":
                print("Votre solde actuel est de:", balance)
            elif language == "de":
                print("Ihr aktueller Kontostand beträgt:", balance)
        elif tr_choice == 2:
            # prompt the user for the withdrawal amount
            if language == "en":
                amount = float(input("Enter the withdrawal amount: "))
            elif language == "es":
                amount = float(input("Ingrese el monto a retirar: "))
            elif language == "fr":
                amount = float(input("Entrez le montant à retirer: "))
            elif language == "de":
                amount = float(
                    input("Geben Sie den Betrag ein, den Sie abheben möchten: "))

            # make sure the withdrawal amount is not greater than the current balance
            if amount > balance:
                if language == "en":
                    print("Insufficient balance!")
                elif language == "es":
                    print("Saldo insuficiente!")
                elif language == "fr":
                    print("Solde insuffisant!")
                elif language == "de":
                    print("Unzureichender Kontostand!")
            else:
                # update the balance and display the new balance
                balance -= amount
                if language == "en":
                    print("Your new balance is:", balance)
                elif language == "es":
                    print("Tu nuevo saldo es:", balance)
                elif language == "fr":
                    print("Votre nouveau solde est:", balance)
                elif language == "de":
                    print("Ihr neuer Kontostand beträgt:", balance)
        elif tr_choice == 3:
            # prompt the user for the deposit amount
            if language == "en":
                amount = float(input("Enter the deposit amount: "))
            elif language == "es":
                amount = float(input("Ingrese el monto a depositar: "))
            elif language == "fr":
                amount = float(input("Entrez le montant à déposer: "))
            elif language == "de":
                amount = float(
                    input("Geben Sie den Betrag ein, den Sie einzahlen möchten: "))

            # update the balance and display the new balance
            balance += amount
            if language == "en":
                print("Your new balance is:", balance)
            elif language == "es":
                print("Tu nuevo saldo es:", balance)
            elif language == "fr":
                print("Votre nouveau solde est:", balance)
            elif language == "de":
                print("Ihr neuer Kontostand beträgt:", balance)
        elif tr_choice == 4:
            # quit the program
            exit()
        else:
            # if an invalid choice is entered, display an error message
            if language == "en":
                print("Invalid choice. Please try again.")
            elif language == "es":
                print("Opción inválida. Inténtalo de nuevo.")
            elif language == "fr":
                print("Choix invalide. Veuillez réessayer.")
            elif language == "de":
                print("Ungültige Auswahl. Bitte versuche es erneut.")


# run the ATM machine
atm_machine()
