def calculatrice():
  #boite du  programme
  continuer_logiciel = True 
  print("Bienvenue sur une calcultrice  basique.")
  #ajout de while pour la condition 'tant que' 
  while continuer_logiciel:
    try:
      #permettre a  l'utilisateur d'entrer des données
      num1 = float(input("entrez votre  premier nombre:"))
      operateur = input("Entrez l'opérateur (+, -, *, /) : ")
      num2 = float(input("entrez votre second nombre:"))
      if operateur == "+":
        resultat = num1 + num2
      elif operateur == "-":
        resultat = num1 - num2
      elif operateur == "*":
            resultat = num1 * num2
      elif operateur == "/":
              if num2 == 0:
                print("ERREUR : Division par zéro impossible.")
                #utilisation de continue  pour   retourne  au debut.
                continue
                resultat =  num1/num2
      else: 
               print("Erreur")
               continue
               #utilisation du fstring  pour une simplification du calcul  final.
      print(f"RÉSULTAT : {num1} {operateur} {num2} = {resultat}") 
    except ValueError: 
      print("veuillez entrez des formules correctes")  
    print("Merci d'avoir tester  ma première calculatrice   à bientot !")
    #lancement   de la calculatrice 
calculatrice()
      
