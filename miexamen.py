import csv
from decimal import Decimal

class Vehiculo:
    def __init__(self, codigo, marca, modelo, precio, kilometraje):
        self.codigo = codigo
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.kilometraje = kilometraje

def guardar_vehiculo(vehiculo, archivo):
    with open(archivo, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([vehiculo.codigo, vehiculo.marca, vehiculo.modelo, vehiculo.precio, vehiculo.kilometraje])

def listar_vehiculos(archivo):
    with open(archivo, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Código: {row[0]}, Marca: {row[1]}, Modelo: {row[2]}, Precio: {row[3]}, Kilometraje: {row[4]}")

def editar_vehiculo(codigo, nuevo_marca, nuevo_modelo, nuevo_precio, nuevo_kilometraje, archivo):
    vehiculos = []
    with open(archivo, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == codigo:
                row[1] = nuevo_marca
                row[2] = nuevo_modelo
                row[3] = nuevo_precio
                row[4] = nuevo_kilometraje
            vehiculos.append(row)

    with open(archivo, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for vehiculo in vehiculos:
            writer.writerow(vehiculo)

def eliminar_vehiculo(codigo, archivo):
    vehiculos = []
    with open(archivo, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != codigo:
                vehiculos.append(row)

    with open(archivo, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for vehiculo in vehiculos:
            writer.writerow(vehiculo)

if __name__ == "__main__":
    archivo = "vehiculos.csv"

    while True:
        print("\nSeleccione una opción:")
        print("a. Crear vehículo")
        print("b. Editar vehículo")
        print("c. Eliminar vehículo")
        print("d. Listar vehículos")
        print("e. Cargar vehículos desde la línea de comandos")
        print("q. Salir")

        opcion = input("Ingrese la letra correspondiente a la opción: ")

        if opcion == 'a':
            # crear vehículo
            pass
        elif opcion == 'b':
            # editar vehículo
            pass
        elif opcion == 'c':
            # eliminar vehículo
            pass
        elif opcion == 'd':
            listar_vehiculos(archivo)
        elif opcion == 'e':
            datos_str = input("Ingrese los datos de los vehículos (separados por comas): ")
            # Cargar vehículos desde la línea de comandos
            pass
        elif opcion == 'q':
            break
        else:
            print("Opción no válida.")
