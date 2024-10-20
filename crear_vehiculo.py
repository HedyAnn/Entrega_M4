from vehiculo import automovil

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