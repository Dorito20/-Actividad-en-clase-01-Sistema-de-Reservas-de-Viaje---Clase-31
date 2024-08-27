# Lista global que almacenará los usuarios registrados
usuarios = []


def menu():
    print("\nBienvenido al Sistema de reseva de viajes")
    print("1. Registrar nuevo usuario")
    print("2. Mostrar reserva un viaje")
    print("3. Actualizar información de un estudiante")
    print("4. Eliminar un estudiante")
    print("5. Salir")
    opcion = input("Elige una opción (1/2/3/4/5): ")
    return opcion

def registrar_usuario():
    nombre = input("Ingresa el nombre del usuario: ")
    usuarios.append(nombre)
    print(f"usuario {nombre} registrado con éxito.")

def main():
    while True:
        opcion = menu()
        if opcion == '1':
           registrar_usuario()
        elif opcion == '2':
            print("registrar")
            registrar_viaje()
        elif opcion == '3':
            print("registrar")
            #actualizar_estudiante()
        elif opcion == '4':
            print("registrar")
            #eliminar_estudiante()
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

def registrar_usuario():
    nombre = input("Ingresa el nombre del usuario: ")
    usuarios.append(nombre)
    print(f"usuario {nombre} registrado con éxito.")
    
    
main()