# Nombre: listas.py
# Objetivo: Muestra el funcionamiento de las listas en python
# Autor: Carlos Alejandro Figueroa Bazán
# Fecha: 02 de Julio de 2019

lista = []
global con

# Método para agregar items
def AddItemList(dato):
    lista.append(dato)

# Método para imprimir items
def PrintList():
    j=0
    for i in lista:
        print("Item: ", j, ", ", i)
        j += 1

# Método para borrar item
def DeleteItem(dato):
    if (dato in lista):
        lista.remove(dato)
        print("Dato removido")
    else:
        print("El dato no existe")

# Método para modificar item
def ModifyItem(dato, con):
    for i in range(5):
        if (dato == lista[i]):
            lista.remove(dato)
            datoNuevo = input("Ingrese el nuevo dato: ")
            lista.insert(i, datoNuevo)

def FindItem(dato):
    if (dato in lista):
        print("El dato ha sido encontrado")
    else:
        print("El dato no existe")

def main():
    ciclo = True
    while(ciclo == True):
        opc = int(input("1.- Agregar item  2.- Imprimir Items  3.- Buscar Item  4.- Borrar Item  5.- Modificar Item  6.- Salir"))

        if (opc == 1):
            n = int(input("Ingrese el numero de datos que desea ingresar: "))
            con = n
            for i in range(n):
                item = input("Introduce el valor del elemento: ")
                AddItemList(item)
        elif(opc == 2):
            PrintList()
        elif (opc == 3):
            buscar = input("Ingrese el dato que desea borrar: ")
            FindItem(buscar)
        elif (opc == 4):
            borrar = input("Ingrese el dato que desea borrar: ")
            DeleteItem(borrar)
        elif(opc == 5):
            dato = input("Ingrese el dato que desea modificar: ")
            ModifyItem(dato, con)
        elif (opc == 6):
            ciclo = False
            print("Adios")

if __name__ == "__main__":
    main()