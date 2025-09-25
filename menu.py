from logic import *
def mostrar_menu():
    print("\n" + "=" * 40)
    print("    VETERINARIA MASCOTAS FELICES")
    print("=" * 40)
    print("1. Ver veterinarios")
    print("2. Ver servicios")
    print("3. Pedir turno")
    print("4. Ver turnos")
    print("5. Buscar turno")
    print("6. Cancelar turno")
    print("7. Registrar mascota")
    print("8. Ver mascotas")
    print("0. Salir")
    print("=" * 40)


def main():
    print("Bienvenido a la Veterinaria")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_veterinarios()
        elif opcion == "2":
            mostrar_servicios()
        elif opcion == "3":
            pedir_turno()
        elif opcion == "4":
            ver_turnos()
        elif opcion == "5":
            buscar_turno()
        elif opcion == "6":
            cancelar_turno()
        elif opcion == "7":
            agregar_mascota()
        elif opcion == "8":
            ver_mascotas()
        elif opcion == "0":
            print("¡Gracias por visitarnos!")
            break
        else:
            print("Opción no válida")

        if opcion != "0":
            input("\nPresiona Enter para continuar...")