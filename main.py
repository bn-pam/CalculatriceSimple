from addition import addition
from soustraction import soustraction
from multiplication import multiplication
from squarred import squarred
from division import division

choix = ""
while choix != "q":
    print("A pour addition, S pour soustraction, M pour multiplication, D pour division, R pour racine_carrée")
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

    elif choix == "R" or choix == "r" :
        nombre1 = int(input("donner le nombre: "))
        result = squarred(nombre1)
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
