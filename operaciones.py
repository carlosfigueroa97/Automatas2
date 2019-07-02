# Nombre: Operaciones.py
# Objetivo: Muestra como trabajan los métodos o funciones de python
# Autor: Carlos Alejandro Figueroa Bazán
# Fecha: 29 de Junio de 2019

#----------------------------------------------------------------------
#               Función para sumar dos enteros
#----------------------------------------------------------------------
def suma(num1, num2):
    return num1+num2

#----------------------------------------------------------------------
#               Función para restar dos enteros
#----------------------------------------------------------------------
def resta(num1, num2):
    return num1-num2

#----------------------------------------------------------------------
#               Función para multiplicar dos enteros
#----------------------------------------------------------------------
def multiplicacion(num1, num2):
    return num1*num2

#----------------------------------------------------------------------
#               Función para dividir dos enteros
#----------------------------------------------------------------------
def division(num1, num2):
    return num1/num2

#----------------------------------------------------------------------
#               Función para comparar dos enteros
#----------------------------------------------------------------------
def comparacion(num1, num2):
    if (num1 > num2):
        print("El mayor número es: ", num1)
    elif (num2 > num1):
        print("El número mayor es: ", num2)
    else:
        print("Los dos numeros son iguales: ", num1 , ",", num2)

# Función main
def main():
    ciclo = True
    while (ciclo == True):
        print("Operaciones básicas con numeros enteros")
        print("\n")
        n1 = int(input("Introduce el primer número: "))
        n2 = int(input("Introduce el segundo número: "))

        # Invocación de las funciones
        print("La suma es: " + str(suma(n1, n2)))
        print("La resta es: " + str(resta(n1, n2)))
        print("La multiplicación es: " + str(multiplicacion(n1, n2)))
        print("La división es: " + str(division(n1, n2)))
        comparacion(n1, n2)

        cad = input("Otro cálculo (s/n)? ")
        if (cad == "S" or cad == "s"):
            ciclo = True
        else:
            ciclo = False
        print("\n")

if __name__ == "__main__":
    main()