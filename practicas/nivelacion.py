################  clase 2 video 2:45  ######################
# Una reconocida productora de contenidos audiovisuales está en busca de nuevas ideas
# para su próximo proyecto, que promete cautivar al público.
# Las posibles temáticas para explorar son las siguientes:
# • Comedia
# • Ciencia ficción
# • Drama
# Para ello, la empresa ha decidido realizar una encuesta entre sus empleados para
# recopilar información valiosa. Los datos para recopilar por cada empleado son los
# siguientes:
# A) Información a ingresar por cada empleado encuestado:
# • Nombre del empleado
# • Edad (debe ser mayor o igual a 18)
# • Género (Masculino - Femenino)
# • Temática de interés (Comedia, Ciencia ficción, Drama)
# B) Se deben cargar 10 encuestas a través de la terminal.
# C) Se requiere determinar:
# • La cantidad de empleados de género masculino que votaron por Ciencia ficción o
# Drama, cuya edad esté entre 25 y 50 años, inclusive.
# • El porcentaje de empleados que no votaron por Comedia, siempre y cuando su
# género no sea Femenino o su edad esté comprendida entre 30 y 40 años.
# • El nombre y la temática de interés votada por el empleado masculino de mayor
# edad.

DATOS =1

contador = 0
contador_no_comedia = 0
bandera  = True
tematica_mayor = None
mayor_edad = 0
nombre_mayor = None


for i in range(DATOS):
    
    nombre = input("ingrese nombre: ")
    #varias manera de validar
    while not nombre.isalpha():#uso while para validar, si no ingresa lo que quiero vuelve a pedir la info
        # (not) MIENTRAS NO SEA ALFABETICO VOLVE A PEDIR EL DATO
        nombre = input("ERROR. Reingrese nombre: ")
    while True:
        edad = input("ingrese edad mayor a 18: ")
        if edad.isdigit():
            edad = int(edad)
            if edad < 18:
                print("Edad INVALIDA")
            else:
                break
        else:
            print("No es un numero")
        
    print(edad)
    
    # varias manera de validar
    # Yo al while quiero entrar cuando esta mal ingresado el dato
    genero = input("ingrese genero: ").lower()
    while not ( genero == "masculino" or genero == "femenino" ):# Uso AND mientras todo lo que tengo en genero que no sea ninguno de los dos me siga pidiendo datos
        # MIENTRAS el genero sea invalido// no sea valido(usando not) vuelvo a entrar
        genero = input("ERROR genero invalido. Reingrese genero: ").lower() #CADA VEZ QUE PIDO EL DATO SE USA .LOWER()
    print(genero)
    #VIDEO 2:38
    tematica = input("ingrese tematica: ")
    while not ( tematica == "ciencia" or tematica == "comedia" or tematica == "drama"):# Uso AND mientras todo lo que tengo en tematica que no sea ninguno de los dos me siga pidiendo datos
        # MIENTRAS el tematica sea invalido// o no sea valido(usando not) vuelvo a entrar
        tematica = input("ERROR tematica invalido. Reingrese tematica: ") #CADA VEZ QUE PIDO EL DATO SE USA .LOWER()
    print(tematica)
    
    #CHEQUEAR ESTE CONDICION
    if genero == "Masculino" and \
    (tematica == "ciencia" or tematica == "drama") and (edad >= 25 and edad <= 50):
            contador += 1
        
    #video 3:10 
    if tematica != "comedia"and (genero == "masculino" and  (edad >= 30 and edad <= 40)):#distinto de comedoa
           
            contador_no_comedia += 1
    
    #CLASE 4 punto 3
    if genero == "masculino":
        if edad > mayor_edad or bandera:# si la edad es mayor a mayor edad o bandera true video 31:50
            bandera = False
            nombre_mayor = nombre
            mayor_edad = edad
            tematica_mayor = tematica
    
    
            
#DESPUES DEL FOR          
print(f"Respuesta punto 1: {contador}")
porcentaje_comedia =  contador_no_comedia * 100 / DATOS
print(f"El porcentaje de comedia es: {porcentaje_comedia}")
print(f"Masculino de mayor:\n edad: {mayor_edad} \n nombre: {nombre_mayor} \n tematica: {tematica_mayor}")


 #VIDEO  1:18 CONTINUAR AHI    
    # print(nombre)
    # while True:
    #     try:
    #         edad = int(input("Reingrese edad: "))#  si esta todo bien, entra en el TRY 
    #         if edad < 18:
    #             raise Exception("Edad menor a ")# seria como generar mi propia excepcion
    #             # print("Edad invalida")
    #         else: #entraria en el else si el dato es valido y sale del while con el break
    #             break
    #     except ValueError:#lo puedo especificar el error haceindo la prueba del error que me lanza la consola. SI NO ESPECIFICO ERROR AGARRA TODAS LAS EXCEPCIONES QUE PUEDEN EXISTIR
    #         print("Eso no es un numero...")
    #     except:
    #         print("Edad invalida")
    # print(edad)
    
    # def genero_valido(genero): # video 2:11
    #     return genero == "Masculino" or genero == "Femenino"
    # genero = input("ingrese genero: ")
    # while not genero_valido(genero):
    #     genero = input("ERROR genero invalido. Reingrese genero: ") 
    # print(genero)