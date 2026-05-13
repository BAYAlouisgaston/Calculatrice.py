def calculatrice():
    continuer_logiciel = True
    print("Bienvenue sur une calculatrice basique.")

    # ajout de while pour la condition 'tant que'
    while continuer_logiciel:
        try:
            # permettre a l'utilisateur d'entrer des données
            num1 = float(input("Entrez votre premier nombre : "))
            operateur = input("Entrez l'opérateur (+, -, *, /) : ")
            num2 = float(input("Entrez votre second nombre : "))
            if operateur == "+":
                resultat = num1 + num2
            elif operateur == "-":
                resultat = num1 - num2
            elif operateur == "*":
                resultat = num1 * num2
            elif operateur == "/":
                if num2 == 0:
                    print("ERREUR : Division par zéro impossible.")
                    continue
                resultat = num1 / num2
            else:
                print("Erreur : opérateur non reconnu.")
                continue

            # utilisation du fstring pour une simplification du calcul final
            print(f"RÉSULTAT : {num1} {operateur} {num2} = {resultat}")

        except ValueError:
            print("Veuillez entrer des formules correctes.")
            continue 
        choix = input("Voulez vous  continuer ? (O/N):").lower()
        if choix == 'o':
          continuer_logiciel = True
        else:
          continuer_logiciel = False 
    print("Merci d'avoir testé ma première calculatrice, à bientôt !")
# lancement de la calculatrice
calculatrice()
      
