from calculatrice.src.addition import addition
from calculatrice.src.soustraction import soustraction
from calculatrice.src.multiplication import multiplication
from calculatrice.src.squarred import squarred
from calculatrice.src.division import division


def calculatrice():
    choix = ""
    while choix != "q":
        print("A pour addition, S pour soustraction, M pour multiplication, D pour division, R pour racine_carrée")
        print("q pour sortir")
        choix = input("indiquer votre choix : ")
        if choix == "A" or choix == "a" :
            nombre1_str = input("donner le premier nombre : ")
            while not nombre1_str.isdigit():
                nombre1_str = input("merci de rentrer un nombre :")
            nombre1 = int(nombre1_str)
            nombre2_str = input("donner un autre nombre : ")
            while not nombre2_str.isdigit() :
                nombre2_str = input("merci de rentrer un nombre")
            nombre2 = int(nombre2_str)
            
            result = addition(nombre1, nombre2)
            print(f"le résultat est {result}")
            print("")
            
        elif choix == "S" or choix == "s" :
            nombre1_str = input("donner le premier nombre : ")
            while not nombre1_str.isdigit():
                nombre1_str = input("merci de rentrer un nombre :")
            nombre1 = int(nombre1_str)
            nombre2_str = input("donner un autre nombre : ")
            while not nombre2_str.isdigit() :
                nombre2_str = input("merci de rentrer un nombre")
            nombre2 = int(nombre2_str)
            result = soustraction(nombre1, nombre2)
            print(f"le résultat est {result}")
            print("")

        elif choix == "R" or choix == "r" :
            nombre1_str = input("donner le premier nombre : ")
            while not nombre1_str.isdigit():
                nombre1_str = input("merci de rentrer un nombre :")
            nombre1 = int(nombre1_str)
            result = squarred(nombre1)
            print(f"le résultat est {result}")
            print("")

        elif choix == "M" or choix == "m" :
            nombre1_str = input("donner le premier nombre : ")
            while not nombre1_str.isdigit():
                nombre1_str = input("merci de rentrer un nombre :")
            nombre1 = int(nombre1_str)
            nombre2_str = input("donner un autre nombre : ")
            while not nombre2_str.isdigit() :
                nombre2_str = input("merci de rentrer un nombre")
            nombre2 = int(nombre2_str)
            result = multiplication(nombre1, nombre2)
            print(f"le résultat est {result}")
            print("")
            
        elif choix == "D" or choix == "d" :
            nombre1_str = input("donner le premier nombre : ")
            while not nombre1_str.isdigit():
                nombre1_str = input("merci de rentrer un nombre :")
            nombre1 = int(nombre1_str)
            nombre2_str = input("donner un autre nombre : ")
            while not nombre2_str.isdigit() :
                nombre2_str = input("merci de rentrer un nombre")
            nombre2 = int(nombre2_str)
            result = division(nombre1, nombre2)
            print(f"le résultat est {result}")
            print("")
            
        else :
            print("le choix n'est pas correct")
            print("")

if __name__ == "__main__":
    calculatrice()