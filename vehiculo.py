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

