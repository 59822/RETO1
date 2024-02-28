ln = int(input("Escribir el tamaño de la lista: ")) #Se elige el tamaño de la lista.
numbers = [] #La lista donde se van a anexar los valores que el usuario desee posteriormente.
a : int = 0  #El valor con el que va a comparar el loop while para su funcionamiento.
while a < ln:
    a += 1
    number = int(input("Escribir un número: "))
    if type(number) != int:
        print("Escribir un número válido")
    else:
        numbers.append(number) #Se conforma la lista con los valores del usuario de tipo int.


def repo3(numb : list):
    primolist = []
    for i in numb: #Se itera sobre la lista de números.
        primo = True #El booleano que permite saber si un número es primo o no.
        if i <= 1:
            continue
        for j in range(2, i):
            if i % j == 0:
                primo = False
                break
        if primo:
            primolist.append(i)
    return primolist


print("Los números primos son:", repo3(numbers))
  
