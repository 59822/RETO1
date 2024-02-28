palabra = input("Ingrese una palabra: ") #El usuario digita una palabra. 
palabra = list(palabra) #Esa palabra se convierte en una lista para poder acceder a ella luego.  

def repo2(x: list): #Utilizamos una función que recibe una lista.
    palindroma = True #Variable de booleano que cambiará si la condición de palindroma no se cumple.
    i = 0 #Inicializador para el loop.

    while i < len(x)//2:  #Loop  que se ejecuta si el inicializador es menor a la mitad de la longitud de la lista.
        if x[i] != x[-(i+1)]:  #Condición que corta el booleano y transforma el booleano si al leer los caracteres desde adelante y desde atrás no coinciden.
            palindroma = False #Transformación del booleano a Falso si no cumple la idea de palindromo.
            break 
        i += 1 #Se aumenta el incializador si la condición se cumple.

    if palindroma: #Si palindroma sigue siendo True se enseñará en la terminal.
        print("Es palíndroma")
    else: #Y si no se enseñará en terminal que no es.
        print("No es palíndroma")

repo2(palabra) #Ejecución de la función.