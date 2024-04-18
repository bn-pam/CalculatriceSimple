# main.py
from addition import addition
from soustraction import soustraction
from multiplication import multiplication
from division import division

while True:
    print("Menu:")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Entrez votre choix (1/2/3/4) : ")

    if choice == '1':
        a = int(input("Entrez le premier nombre : "))
        b = int(input("Entrez le deuxième nombre : "))
        print("Résultat de l'addition :", addition(a, b))
    elif choice == '2':
        # Appel pour la soustraction
        pass
    elif choice == '3':
        # Appel pour la multiplication
        pass
    elif choice == '4':
        # Appel pour la division
        pass
    else:
        print("Choix invalide. Veuillez choisir 1, 2, 3 ou 4.")
