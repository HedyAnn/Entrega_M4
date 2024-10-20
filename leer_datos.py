from vehiculo import particular, carga, bicicleta, motocicleta
import csv
import ast

def leer_datos_csv(archivo_csv):
        vehiculos_particular = []
        vehiculos_carga = []
        bicicletas = []
        motocicletas = []

        try:
            with open(archivo_csv, newline='') as archivo:
                lector_csv = csv.reader(archivo)
                for fila in lector_csv:
                    clase_vehiculo = fila[0]
                    atributos = ast.literal_eval(fila[1])  

                    if 'particular' in clase_vehiculo.lower():
                        vehiculos_particular.append({
                            'marca': atributos['marca'],
                            'modelo': atributos['modelo'],
                            'nro_ruedas': atributos['n_ruedas'],
                            'velocidad': atributos['velocidad'],
                            'cilindrada': atributos['cilindrada'],
                            'nro_puestos': atributos['n_puesto']
                        })
                    elif 'carga' in clase_vehiculo.lower():
                        vehiculos_carga.append({
                            'marca': atributos['marca'],
                            'modelo': atributos['modelo'],
                            'nro_ruedas': atributos['n_ruedas'],
                            'velocidad': atributos['velocidad'],
                            'cilindrada': atributos['cilindrada'],
                            'carga': atributos['carga']
                        })
                    elif 'bicicleta' in clase_vehiculo.lower():
                        bicicletas.append({
                            'marca': atributos['marca'],
                            'modelo': atributos['modelo'],
                            'nro_ruedas': atributos['n_ruedas'],
                            'tipo': atributos['tipo']
                        })
                    elif 'motocicleta' in clase_vehiculo.lower():
                        motocicletas.append({
                            'marca': atributos['marca'],
                            'modelo': atributos['modelo'],
                            'nro_ruedas': atributos['n_ruedas'],
                            'tipo': atributos['tipo'],
                            'motor': atributos['motor'],
                            'cuadro': atributos['cuadro'],
                            'nro_radios': atributos['nro_radios']
                        })
                    else:
                        print(f"Clase de vehículo no reconocida: {clase_vehiculo}")
                        continue

            print("Lista de Vehículos Particular")
            for vehiculo in vehiculos_particular:
                print(vehiculo)
            
            print("\nLista de Vehículos Carga")
            for vehiculo in vehiculos_carga:
                print(vehiculo)
            
            print("\nLista de Vehículos Bicicleta")
            for bicicleta in bicicletas:
                print(bicicleta)

            print("\nLista de Vehículos Motocicleta")
            for motocicleta in motocicletas:
                print(motocicleta)

        except FileNotFoundError:
            print(f"El archivo {archivo_csv} no fue encontrado.")
