# Hacer una calculadora. Para ello el programa iniciará y contará con un menú de opciones:
# 1. Ingresar 1er operando (A=x)
# 2. Ingresar 2do operando (B=y)
# 3. Calcular todas las operaciones
# a) Calcular la suma (A+B)
# b) Calcular la resta (A-B)
# c) Calcular la división(A/B)
# d) Calcular la multiplicación(A*B)
# e) Calcular factorial(A!)
# 4. Informar resultados
# a) “El resultado de A+B es: r”
# b) “El resultado de A-B es: r”
# c) “El resultado de A/B es: r” o “No es posible dividir por cero”
# d) “El resultado de A*B es: r”
# e) “El factorial de A es: r1 y El factorial de B es: r2”
# 5. Salir
# • Todas las funciones matemáticas del menú se deberán realizar en una biblioteca aparte,que contenga las funciones
# para realizar las cinco operaciones.
# • En el menú deberán aparecer los valores actuales cargados en los operandos A y B(donde dice “x” e “y” en el ejemplo,
# se debe mostrar el número cargado)
# • Deberán contemplarse los casos de error (división por cero, etc.)
# • Documentar todas las funciones
import math
def menu()->str:
    limpiar_pantalla()
    print(f"{'Menu de opciones':^100s}")#:^100s imprime msj de 10 caracteres y menu de opciones queda centrado en el
    print("1- Ingrese los numeros a calcular: ")
    print("2- calcular suma: ")
    print("3- calcular resta: ")
    print("4- calcular division: ")
    print("5- calcular multiplicacion: ")
    print("6- calcular factoias: ")
    print("7- Salir: ")
    
    return input("Ingrese opcion: ")

def limpiar_pantalla():
    import os
    os.system("cls")# PARA LIMPIAR PANTALLA
    
def pedir_numeros(x:int, y:int):
    """pide numeros al ususario

    Args:
        x (int): primer numero 
        y (int): segundo numero
        
    returns: devuelce los numeros
    """
    x = int(input("Ingrese un numero: "))
    y= int(input("Ingrese otro numero: "))
    return x,y
        
def sumar(x:int, b:int)->int:
    """suma dos numeros

    Args:
        x (int): primer numero entero
        b (int): segundo numero entero

    Returns:
        int: retorna suma
    """
    
    
    return x + b
def restar(x:int, b:int)->int:
    """resta dos numeros
     Args:
        x (int): primer numero entero
        b (int): segundo numero entero

    Returns:
        int: retornar resta
    """
    return x - b
def dividir(x:int, b:int)->int:
    """divide dos numeros

    Args:
        x (int): primer numero entero
        b (int): segundo numero entero

    Returns:
        int: division
    """
    if b == 0:
        return "No es posible dividir por cero"
    return x / b
            
    
def multiplicacion(x:int, b:int)->int:
    """multiplica dos numeros

    Args:
        x (int): primer numero entero
        b (int): segundo numero entero

    Returns:
        int: multiplicacion
    """  
    return x * b 

def factorial(n:int) -> int:
    """

    Args:
        x (int): primer numero entero
        b (int): segundo numero entero

    Returns:
        int: prevee que el factorial de dos numero no sea negativo
    """
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def pausar():
    import os
    os.system("pause")
    
def pedir_confirmacion(mensaje:str)->bool:
    rta = input(mensaje).lower()#lo que me respondan lo paso a miniscula si el usuario pone S
    return rta == "s"
   
    
    
    

