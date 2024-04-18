print("Bienvenue dans la calculatrice simple. ! ") #message de bienvenue et guide 

# imports des fichiers de fonction

from division import division
from soustraction import soustraction
from addition import addition
from multiplication import multiplication

choix = ""
while choix != "q":
    print("A pour addition, S pour soustraction, M pour mulitplication, D pour division")
    print("q pour sortir")
    choix = input("indiquer votre choix : ")
    if choix == "A" or choix == "a" :
        nombre1 = int(input("donner le premier nombre : "))
        nombre2 = int(input("donner un autre nombre : "))
        result = addition(nombre1, nombre2)
        print(f"le résultat est {result}")
        print("")
        
    elif choix == "S" or choix == "s" :
        nombre1 = int(input("donner le premier nombre : "))
        nombre2 = int(input("donner un autre nombre : "))
        result = soustraction(nombre1, nombre2)
        print(f"le résultat est {result}")
        print("")

    elif choix == "M" or choix == "m" :
        nombre1 = int(input("donner le premier nombre : "))
        nombre2 = int(input("donner un autre nombre : "))
        result = multiplication(nombre1, nombre2)
        print(f"le résultat est {result}")
        print("")
        
     elif choix == "D" or choix == "d" :
        nombre1 = int(input("donner le premier nombre : "))
        nombre2 = int(input("donner un autre nombre : "))
        result = division(nombre1, nombre2)
        print(f"le résultat est {result}")
        print("")
        
     else :
        print("le choix n'est pas correct")
        print("")
