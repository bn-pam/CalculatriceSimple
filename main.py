from multiplication import multiplication
choix = ""
while choix != "q":
    print("A pour addition, S pour soustraction, M pour mulitplication, D pour division")
    print("q pour sortir")
    choix = input("indiquer votre choix : ")
    if choix == "M" or choix == "m" :
        nombre1 = int(input("donner le premier nombre : "))
        nombre2 = int(input("donner un autre nombre : "))
        result = multiplication(nombre1, nombre2)
        print(f"le résultat est {result}")