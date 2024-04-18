# Dans le fichier main.py sur la branche main
from addition import addition


while True:
    print("Menu:")
    print("1. Opération membre 1")
    print("2. Opération membre 2")
    print("3. Opération membre 3")
    choice = input("Entrez votre choix (1/2/3) : ")

    if choice == '1':
        # Appel de la fonction pour l'opération du membre 1
        print(addition(10, 5))
 
    else:
        print("Choix invalide. Veuillez choisir 1, 2 ou 3.")