print("Bienvenue dans la calculatrice simple. Quelle opération souhaitez-vous faire ? ") #message de bienvenue et guide 

# imports des fichiers de fonction

from division import division
from soustraction import soustraction
from addition import addition
from multiplication import multiplication
from squarred import squarred
from math import sqrt

# affichage de la fonctionnalité à l'écran et initialisation du résultat vide
operation = input("un nom d'opération suivi de 2 nombres entre parenthèses séparés par une virgule : ")
x=0

# définition de la fonction générale de la calculatrice : appel des 4 opérations différentes
def operation(chiffre_1, chiffre_2):
    if operation is division :
        division(chiffre_1, chiffre_2)

    elif operation is soustraction :
        soustraction(chiffre_1, chiffre_2)

    elif operation is addition :
        addition(chiffre_1, chiffre_2)

    elif operation is multiplication :
        multiplication(chiffre_1, chiffre_2)
    
    elif operation is squarred :
        squarred(chiffre_1, chiffre_2)

    return x



# if input is not str():
#     print("il faudrait rentrer un nom d'opération suivi de 2 nombres entre parenthèses séparés par une virgule
#           "/soit soustraction(chiffre_1, chiffre_2), 
#           "/soit addition(chiffre_1, chiffre_2), 
#           "/soit multiplication(chiffre_1, chiffre_2)
#           "/s'il vous plaît")
