from calculadora import *


seguir = "si"
flag_numero = False
numero1 = 0
numero2 = 0

while seguir == "si":
    opcion = menu()
    print(f"Opción seleccionada: {opcion}")
    match opcion:
        case "1":
            numero1, numero2 = pedir_numeros(numero1, numero2)
            flag_numero = True
            
            
        case "2":
           
            if flag_numero:
                suma = sumar(numero1, numero2)
                print(f"La suma es: {suma}")
            else:
                print("Primero tiene que ingresar dos numeros.")
        case "3":
            
            if flag_numero:
                resta = restar(numero1, numero2)
                print(f"La resta es: {resta}")
            else:
                print("Primero tiene que ingresar dos numeros.")
        case "4":
        
            if flag_numero:
                division = dividir(numero1, numero2)
                print(f"La division es: {division}")
            else:
                print("Primero tiene que ingresar dos numeros.")
        case "5":
        
            if flag_numero:
                multiplicar = multiplicacion(numero1, numero2)
                print(f"La multiplicar es: {multiplicar}")
            else:
                print("Primero tiene que ingresar dos numeros.")
        case "6":
        
            if flag_numero:
                print(f"La factorial es: {factorial(numero1)}")
            else:
                print("Primero tiene que ingresar dos numeros.")
        case "7":
            if pedir_confirmacion("¿Confirma salida? si/no: "):
                seguir = "no"
            continue
    pausar()
               
            
          
                
