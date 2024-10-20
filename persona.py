import csv

class vehiculo:
    def __init__(self,marca,modelo,n_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.n_ruedas = n_ruedas
    
    def __str__(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Ruedas: {self.n_ruedas}'
    
    def guardar_datos_csv(self, nombre_archivo): 
        with open(nombre_archivo, "a", newline='') as archivo:
            datos = [(self.__class__, str(self.__dict__))]
            archivo_csv = csv.writer(archivo)
            archivo_csv.writerows(datos)
            archivo.close()
            
class automovil(vehiculo):
    def __init__(self,marca,modelo,n_ruedas,velocidad,cilindrada):
        super().__init__(marca,modelo,n_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return f'{super().__str__()}, Velocidad: {self.velocidad} km/h, Cilindrada: {self.cilindrada} cc'
    
class particular(automovil):
    def __init__(self,marca,modelo,n_ruedas,velocidad,cilindrada,n_puesto):
        super().__init__(marca,modelo,n_ruedas,velocidad,cilindrada)
        self.n_puesto = n_puesto
        
    def __str__(self):
        return f'{super().__str__()}, N° de puestos: {self.n_puesto}'

class carga(automovil):
    def __init__(self,marca,modelo,n_ruedas,velocidad,cilindrada,carga):
        super().__init__(marca,modelo,n_ruedas,velocidad,cilindrada)
        self.carga = carga
        
    def __str__(self):
        return f'{super().__str__()}, Carga: {self.carga} kg'

class bicicleta(vehiculo):
    def __init__(self,marca,modelo,n_ruedas,tipo):
        super().__init__(marca,modelo,n_ruedas)
        self.tipo = tipo
        
    def __str__(self):
        return f'{super().__str__()}, Tipo: {self.tipo}'

class motocicleta(bicicleta):
    def __init__(self,marca,modelo,n_ruedas,tipo,nro_radios,cuadro,motor):
        super().__init__(marca,modelo,n_ruedas,tipo)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor
        
    def __str__(self):
        return f'{super().__str__()}, N° de radios: {self.nro_radios}, Cuadro: {self.cuadro}, Motor: {self.motor}'

def crear_vehiculos():
    vehiculos = []
    
    while True:
        try:
            n = int(input("Cuántos vehículos desea insertar: "))
            if n <= 0:
                raise ValueError("El número de vehículos debe ser un entero positivo.")
            break  # Salir del bucle si la entrada es válida
        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese un número válido.")

    for i in range(n):
        print(f"\nIngresando datos para el vehículo {i+1}:")
        try:
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            n_ruedas = int(input("Número de ruedas: "))
            velocidad = int(input("Velocidad (km/h): "))
            cilindrada = int(input("Cilindrada (cc): "))
            
            # Supongamos que 'automovil' es una clase previamente definida
            auto = automovil(marca, modelo, n_ruedas, velocidad, cilindrada)
            vehiculos.append(auto)
        
        except ValueError as e:
            print(f"Error de entrada en vehículo {i+1}: {e}. Intente nuevamente.")
            # Aquí puedes optar por repetir la iteración actual si deseas continuar
            continue  # Esto hará que se pida nuevamente la información del vehículo
    
    print("\nImprimiendo por pantalla los vehículos:\n")
    for i, vehiculo in enumerate(vehiculos, start=1):
        print(f"Datos de automóvil {i}: {vehiculo}\n\n")

