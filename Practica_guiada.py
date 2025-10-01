# Programa que pide nombre y año de nacimiento
# Calcula la edad y clasifica por tramos de edad
# Incluye manejo de errores y comentarios explicativos

from datetime import datetime

def main():
    # Obtener el año actual automáticamente
    anio_actual = datetime.now().year  

    # Pedir el nombre del usuario
    nombre = input("Introduce tu nombre: ")

    # Manejo de errores al pedir el año de nacimiento
    try:
        anio_nacimiento = int(input("Introduce tu año de nacimiento (ej: 1990): "))
    except ValueError:
        print("Error: Debes introducir un número válido para el año de nacimiento.")
        return  # Salir del programa si el dato no es válido

    # Calcular la edad
    edad = anio_actual - anio_nacimiento

    # Mostrar resultados
    print(f"\nHola {nombre}, tienes {edad} años.")

    # Clasificación por tramos de edad
    if edad < 18:
        print("Eres menor de edad.")
    elif 18 <= edad <= 65:
        print("Eres adulto.")
    else:
        print("Eres mayor de 65 años.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
