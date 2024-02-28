
def repo(x:int,y:int,z:str):
    print("Salida: ")
    if z == "+":
        return x+y
    elif z== "-":
        return x-y
    elif z== "*":
        return x*y
    elif z== "/":
        if y==0:
            return "Operación no válida"
        else:
            return x/y
    else:
        return "Operación no válida"
    

print("Elija la operación que desea realizar: +, -, *, /")
x= int(input("Ingrese el primer número: "))
y= int(input("Ingrese el segundo número: "))
z= input("Ingrese el operador: ")

print(repo(x,y,z))