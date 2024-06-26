# 5.10 Realice un algoritmo que lea dos vectores de diez elementos y que calcule
# la suma de éstos guardando su resultado en otro vector, el cual se
# debe presentar en forma impresa.


def leer_vectores():
    vector1 = []
    vector2 = []
    
    print("Ingresa los elementos del primer vector:")
    for i in range(10):
        elemento = int(input(f"Elemento {i+1}: "))
        vector1.append(elemento)
    
    print("Ingresa los elementos del segundo vector:")
    for i in range(10):
        elemento = int(input(f"Elemento {i+1}: "))
        vector2.append(elemento)
    
    return vector1, vector2

def sumar_vectores(vector1, vector2):
    suma = []
    
    for i in range(10):
        suma.append(vector1[i] + vector2[i])
    
    return suma

def menu():
    vector1 = []
    vector2 = []
    
    while True:
        print("\n--- Menu ---")
        print("1. Ingresar datos de los 2 vectores")
        print("2. Resultado de la suma de los dos vectores ")
        print("3. Salir")
        
        opcion = input("Selecciona una opción (1-3): ")
        
        if opcion == '1':
            vector1, vector2 = leer_vectores()
        elif opcion == '2':
            if not vector1 or not vector2:
                print("Debes ingresar primero los vectores.")
            else:
                resultado = sumar_vectores(vector1, vector2)
                print("Resultado de la suma de los vectores:", resultado)
        elif opcion == '3':
            print("Saliendo")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")


menu()
