# Nombre: Circunferencia.py
# Objetivo: Indentifica el tipo de triangulo de acuerdo al valor dado
# Autor: Carlos Alejandro Figueroa Bazán
# Fecha: 01 de Julio de 2019

def triangulo(l1, l2, l3):
    if(l1 == l2 and l1 == l3):
        perimetro = 3 * l1
        print("El triangulo es equilatero y su perimetro es: " + str(perimetro))
    elif(l1 != l2 and l1 != l3):
        perimetro = l1 + l2 + l3
        print("El triangulo es escaleno y su perimetro es: " + str(perimetro))
    else:
        perimetro = (2*l1) + l2
        print("El triangulo es isósceles y su perimetro es: " + str(perimetro))


def main():
    l1 = float(input("Ingrese el primer valor "))
    l2 = float(input("Ingrese el segundo valor "))
    l3 = float(input("Ingrese el tercer valor "))
    triangulo(l1, l2, l3)

if __name__ == "__main__":
    main()