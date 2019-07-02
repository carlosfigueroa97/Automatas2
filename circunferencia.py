# Nombre: Circunferencia.py
# Objetivo: Calcula el área de una circunferencia e importar la libreria math
# Autor: Carlos Alejandro Figueroa Bazán
# Fecha: 01 de Julio de 2019

import math as mat
import os

# Función para calcular el area
def calcularArea(r):
    area = mat.pi*(pow(r, 2))
    return area

# Función para calcular el diametro
def calculaDiametro(d):
    diam = d * 2
    return diam

# Método main
def main():
    ciclo = True
    while(ciclo == True):
        print("--------------------------------------------------------")
        print("Script para calcular el area de una circunferencia")
        print("--------------------------------------------------------")
        radio = float(input("Introduce el valor del radio "))
        # invocar un método
        print("El area es: ", calcularArea(radio))
        print("El diametro es: ", calculaDiametro(radio))
        pregunta = input("Desea hacer otro cálculo(S/N)? ")
        if pregunta == "S" or pregunta == "s":
            ciclo = True
        else:
            ciclo = False
    else:
        print("Fin del programa")

if __name__ == "__main__":
    main()
    os.system("cls")