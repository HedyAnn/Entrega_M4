from persona import particular, carga, bicicleta, motocicleta, vehiculo, automovil
import csv

def guardar(nombre_archivo, automovil): 
    try:
        archivo = open(nombre_archivo, "w") 
        try:
            datos = [(automovil.__class__, automovil.__dict__)] 
            archivo_csv = csv.writer(archivo) 
            archivo_csv.writerows(datos)
        except AttributeError as e:
            print(f"Error: el objeto proporcionado no tiene los atributos esperados. {e}")
        finally:
            archivo.close()
    except IOError as e:
        print(f"Error al intentar abrir o escribir en el archivo '{nombre_archivo}': {e}")

def recuperar(nombre_archivo): 
    vehiculos = []
    try:
        archivo = open(nombre_archivo, "r") 
        try:
            archivo_csv = csv.reader(archivo)
            for vehiculo in archivo_csv: 
                vehiculos.append(vehiculo)
        except csv.Error as e:
            print(f"Error al leer el archivo CSV: {e}")
        finally:
            archivo.close()
    except IOError as e:
        print(f"Error al intentar abrir el archivo '{nombre_archivo}': {e}")
    
    return vehiculos



