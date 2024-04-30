from math import sqrt
def squarred(chiffre_1):
    if chiffre_1 <0 :
        raise ValueError ("vous devez saisir un nombre positif ou nul")
    x=sqrt(int(chiffre_1))
    return x
