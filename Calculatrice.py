def calculatrice():
  #boite du  programme
  continuer_logiciel = True 
  print("Bienvenue sur une calcultrice  basique.")
  #ajout de while pour la condition 'tant que' 
  while continuer_logiciel:
    try:
      #permettre a  l'utilisateur d'entrer des données
      num1 = float(input("entrez votre  premier nombre"))
      operateur = input("Entrez l'opérateur (+, -, *, /) : ")
      num2 = float(input("entrez votre second nombre"))
      if operateur == "+":
        resulta = num1 + num2
      elif operateur == "-":
        resultat = num1 - num2
      elif operateur == "*":
            resultat = num1 * num2
      elif operateur == "/":
              if num2 == 0:
                print("ERREUR : Division par zéro impossible.")
                #utilisation de continue  pour   retourne  au debut.
                continue
                resulta =  num1/num2
      else: 
                  print("Erreur")
    except ValueError:
      print("veuillez entrez des formules correctes")  
      #la logigue des calculs
