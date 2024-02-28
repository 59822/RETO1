tam = int(input("Escribir el tamaño de la lista: "))
lista = []
a = 0       #Creates variables for the list and the pivot
while a < tam:
    a+=1
    lis = input("Escribir las palabras para la lista: ")
    if type(lis) == str:  # Corrección aquí
        lista.append(lis)
    else:
        print("Escribir una palabra válida")
    if a == tam:
        break

def mismos_caracteres(lista):
    resultado = []
    for i in lista:
        if len(i) != len(lista[0]):
            if sorted(i) == sorted(lista[0]):  
                resultado.append(i)
    return resultado

print(mismos_caracteres(lista))
