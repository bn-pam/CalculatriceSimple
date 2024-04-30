from calculatrice.src.soustraction import soustraction
from calculatrice.src.addition import addition
from calculatrice.src.division import division
from calculatrice.src.multiplication import multiplication
from calculatrice.src.squarred import squarred

import pytest

#### TEST ADDITION ####
def test_addition():
   assert addition (1,2) == 3
   assert addition (0,0) == 0
   assert addition (-1,1) == 0
   assert addition (-1,-1) == -2

# def test_addition_error_mixed_type():
#     with pytest.raises(TypeError): #erreur si le deuxième est un caractère
#         addition(1,"a")
#     with pytest.raises(TypeError): #erreur si le deuxième est une liste
#         addition(2,[1,2])
#     with pytest.raises(TypeError): #erreur si le premier est un caractère et le deuxième une liste de caractères
#         addition("2",["1","2"])
#     with pytest.raises(TypeError): #erreur si les deux sont des caractères
#         addition("a"+"b")

#### TEST SOUSTRACTION ####
def test_soustraction():
   assert soustraction (1,2) == -1
   assert soustraction (-1,3) == -4
   assert soustraction (-1,-3) == 2
   assert soustraction (1,-3) == 4
   assert addition (0,0) == 0


# def test_soustraction_error_mixed_type():
#     with pytest.raises(TypeError): #erreur si le deuxième est un caractère
#         soustraction(1,"a")
#     with pytest.raises(TypeError): #erreur si le deuxième est une liste
#         soustraction(2,[1,2])
#     with pytest.raises(TypeError): #erreur si le premier est un caractère et le deuxième une liste de caractères
#         soustraction("2",["1","2"])
#     with pytest.raises(TypeError): #erreur si les deux sont des caractères
#         soustraction("a"+"b")
   

#### TEST MULTIPLICATION ####

def test_multiplication():
   assert multiplication (1,2) == 2
   assert multiplication (-1,3) == -3
   assert multiplication (-1,-3) == 3
   assert multiplication (1,-3) == -3
   assert multiplication (0,0) == 0

# def test_multiplication_error_mixed_type():
#     with pytest.raises(TypeError): #erreur si le deuxième est un caractère
#         multiplication(1,"a")
#     with pytest.raises(TypeError): #erreur si le deuxième est une liste
#         multiplication(2,[1,2])
#     with pytest.raises(TypeError): #erreur si le premier est un caractère et le deuxième une liste de caractères
#         multiplication("2",["1","2"])
#     with pytest.raises(TypeError): #erreur si les deux sont des caractères
#         multiplication("a"+"b")


#### TEST DIVISION ####
def test_division():
   assert division (1,2) == 0.5
   assert division (-1,4) == -0.25
   assert division (-1,-4) == 0.25
   assert division (1,-4) == -0.25
   assert division (0,5) == 0

# def test_division_error_mixed_type():
#     with pytest.raises(TypeError): #erreur si le deuxième est un caractère
#         division(1,"a")
#     with pytest.raises(TypeError): #erreur si le deuxième est une liste
#         division(2,[1,2])
#     with pytest.raises(TypeError): #erreur si le premier est un caractère et le deuxième une liste de caractères
#         division("2",["1","2"])
#     with pytest.raises(TypeError): #erreur si les deux sont des caractères
#         division("a"+"b")

def test_division_zero():
   with pytest.raises(ZeroDivisionError): #cas particulier de l'erreur générée par une division par zero
       division(8,0) #donner un cas pour lequel on a une division par zero


#### TEST RACINE CARREE ####
def test_squarred():
   assert squarred (4) == 2
   assert squarred (0) == 0

def test_negative_squarred():
    with pytest.raises(ValueError): #erreur si le chiffre rentré est négatif
        squarred (-4)

# def test_squarred_error_mixed_type():
#     with pytest.raises(TypeError): #erreur si le deuxième est un caractère
#         squarred("a")
#     with pytest.raises(TypeError): #erreur si le deuxième est une liste
#         squarred(2,[1,2])
#     with pytest.raises(TypeError): #erreur si le premier est un caractère et le deuxième une liste de caractères
#         squarred("2",["1","2"])
#     with pytest.raises(TypeError): #erreur si les deux sont des caractères
#         squarred("a"+"b")