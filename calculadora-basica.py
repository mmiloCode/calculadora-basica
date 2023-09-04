# Crear una calculadora por linea de comandos que realice las operaciones básicas

print(
"""---------------------------------
CALCULADORA BÁSICA
---------------------------------""")

print("1 = Suma; \n2 = Resta; \n3 = Multiplicación; \n4 = División; \n5 = Salir.")

# Variables

op = int(input("Ingrese la operación que desea realizar: "))

# Funciones

def operacion(op) :

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if (num1.is_integer()) :
        num1 = int(num1) 

    if (num2.is_integer()) :
        num2 = int(num2) 

    if ( op == 1) :
        print (f"{num1} + {num2} = {num1 + num2}")
    elif (op == 2) :
        print (f"{num1} - {num2} = {num1 - num2}")
    elif (op == 3) :
        print (f"{num1} x {num2} = {num1 * num2}")
    else :
        print (f"{num1} / {num2} = {num1 / num2}")
        


while (op != 5) :

    print("---------------------------------")

    if ( op == 1) :
        print("Operación: Suma")
        operacion(op)
    elif (op == 2) :
        print("Operación: Resta")
        operacion(op)
    elif (op == 3) :
        print("Operación: Multiplicación")
        operacion(op)
    elif (op == 4) :
        print("Operación: División")
        operacion(op)
    else :
        print("Operación no válida.")

    op = int(input("Ingrese la operación que desea realizar: "))


print(
"""---------------------------------
CALCULADORA FINALIZADA
---------------------------------""")