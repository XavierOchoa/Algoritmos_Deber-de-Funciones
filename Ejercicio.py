# 5.13 Se tiene en un arreglo diez elementos representando calificaciones de
# los estudiantes de una escuela. Realice un algoritmo que lea el arreglo
# y calcule la calificación promedio del grupo, además, que cuente los estudiantes
# que obtuvieron calificaciones arriba del promedio del grupo.


def leer_calificaciones():
    print("Ingresa las calificaciones de los 10 estudiantes:")
    calificaciones = []
    for i in range(10):
        calificacion = float(input(f"Calificación del estudiante {i+1}: "))
        calificaciones.append(calificacion)
    return calificaciones

def calcular_promedio(calificaciones):
    if not calificaciones:
        print("Aún no se han ingresado calificaciones.")
        return
    
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"El promedio del grupo es: {promedio:.2f}")

def contar_calif_arriba_promedio(calificaciones):
    if not calificaciones:
        print("Aún no se han ingresado calificaciones.")
        return
    
    promedio = sum(calificaciones) / len(calificaciones)
    estudiantes_arriba_promedio = sum(1 for calif in calificaciones if calif > promedio)
    print(f"Estudiantes con calificaciones arriba del promedio: {estudiantes_arriba_promedio}")

def menu():
    calificaciones = []
    
    while True:
        print("\nSISTEMA DE NOTAS DE LA ESCUELA")
        print("\n--- Menú ---")
        print("1. Ingresar calificaciones")
        print("2. Calcular promedio del grupo")
        print("3. Contar estudiantes con calificaciones arriba del promedio")
        print("4. Salir")
        
        opcion = input("Selecciona una opción (1-4): ")
        
        if opcion == '1':
            calificaciones = leer_calificaciones()
        elif opcion == '2':
            calcular_promedio(calificaciones)
        elif opcion == '3':
            contar_calif_arriba_promedio(calificaciones)
        elif opcion == '4':
            print("Saliendo del menu. Gracias")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")


menu()
