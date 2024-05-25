# Una veterinaria quiere llevar un registro de los animales que atiende y para esto quieren crear un
# programa que un empleado completará con los datos de cada mascota que ingrese.
#  Nombre
#  Edad
#  Raza (Perro - gato - otro)
#  Género (Macho – Hembra)
#  Peso (Entre 6kg y 65kg)
# B) Deben cargarse 10 animales a través de la terminal.
# C) Determinar:
#  La cantidad de gatos macho de entre 3 y 6 años que se ingresaron
#  El porcentaje de animales ingresados de cada raza

# A) Los datos requeridos de cada animal son:
ANIMALES = 3
bandera_hembra = True
mas_pesado_hembra = 0
contador_edad = 0
contador_otro = 0
contador_perro = 0
contador_gato = 0
acumulador_peso = 0
contador_gatos = 0

for i in range(ANIMALES):
    
    nombre = input("Ingrese nombre de mascota: ") 
    while not nombre.isalpha():
        nombre = input("ERROR: reingrese nombre de mascota: ")
        
    while True:
        edad = input("Ingrese edad: ")
        if edad.isdigit():
            edad = int(edad)
            if edad > 20:
                print("Edad invalida")
            else:
                break
        else:
            edad = ("ERROR: reingrese edad: ")
    raza = input("Ingrese Raza del animal: ")
    
    while not (raza == "perro" or raza == "gato" or raza =="otro"):
        raza = input("Reingrese Raza del animal: ")
        
    
    genero = input("Ingrese su género (macho o hembra): ")
    while not (genero == "hembra" or genero == "macho"):
        genero = input("Ingrese un género válido (macho o hembra): ")

         
    while True:
        peso = input("Ingrese peso: ")
        if peso.isdigit():
            peso = int(peso)
            if peso < 6 or peso > 65:
                print("Peso invalida")
            else:
                break
        else:
            peso = input("ERROR: reingrese peso: ")
            
#  La perra hembra mas pesada
    if genero =="hembra" and raza == "perro":
        if peso > mas_pesado_hembra or bandera_hembra:
            bandera_hembra = False
            mas_pesado_hembra = peso

   
        
#  El promedio de peso de los animales mayores a 7 años que no sean gatos ni perros
    if edad > 7 and raza == "otro":
        acumulador_peso += peso
        contador_edad += 1
        
#  La cantidad de gatos macho de entre 3 y 6 años que se ingresaron
    if genero == "macho":
        if raza == "gato" and edad > 3 and edad < 6:
            contador_gatos += 1
#  El porcentaje de animales ingresados de cada raza
    if raza == "perro":
        contador_perro += 1
    elif raza == "gato":
        contador_gato += 1
    else:
        contador_otro += 1
   

porcentaje_perro = (contador_perro  / ANIMALES) * 100
porcentaje_gato = (contador_gato  / ANIMALES ) * 100
porcentaje_otro = (contador_otro  / ANIMALES ) * 100

if contador_edad > 0:
    promedio = acumulador_peso / contador_edad
    print(f"El promedio de peso de animales mayores a 7 años que no son ni perro ni gato: {promedio}")
else:
    print("No se encontraron animales mayores a 7 años que no sean perros ni gatos.")

print(f"La perra mas pesa es {mas_pesado_hembra}")
print(f"machos gatos ingresados: {contador_gatos}")
print(f"porcentaje de animales que ingresaron de perro: {porcentaje_perro}% gatos: {porcentaje_gato}% y otros: {porcentaje_otro}%")



