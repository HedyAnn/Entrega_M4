from persona import *
from guardar_datos import *
from leer_datos import *

crear_vehiculos()

auto = automovil("Ford", "Fiesta", "4", "180", "500") 

guardar("ejemplo.csv", auto) 

automoviles = recuperar("ejemplo.csv") 

print(automoviles)
# for auto in automoviles: 
#     print(auto)

print("\n")    

particular1 = particular("Ford", "Fiesta", 4, "180", "500", 5)
carga1 = carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta1 = bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta1 = motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble viga",21)

print(particular1)
print(carga1)
print(bicicleta1)
print(motocicleta1)

print("\n") 

print("Motocicleta es instancia de Vehículo:", isinstance(motocicleta1, vehiculo))
print("Motocicleta es instancia de Automóvil:", isinstance(motocicleta1, automovil))
print("Motocicleta es instancia de Vehículo particular:", isinstance(motocicleta1, particular))
print("Motocicleta es instancia de Vehículo de Carga:", isinstance(motocicleta1, carga))
print("Motocicleta es instancia de Bicicleta:", isinstance(motocicleta1, bicicleta))
print("Motocicleta es instancia de Motocicleta:", isinstance(motocicleta1, motocicleta))

print("\n")

particular1.guardar_datos_csv("vehiculos.csv")

carga1.guardar_datos_csv("vehiculos.csv")

bicicleta1.guardar_datos_csv("vehiculos.csv")

motocicleta1.guardar_datos_csv("vehiculos.csv")


leer_datos_csv("vehiculos.csv")