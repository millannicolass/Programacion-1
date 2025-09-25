from datos import veterinarios, servicios, turnos, mascotas
def mostrar_veterinarios():
    print("\n--- Nuestros Veterinarios ---")
    for vet in veterinarios:
        print(f"{vet['id']}. {vet['nombre']} - {vet['especialidad']}")


def mostrar_servicios():
    print("\n--- Servicios Disponibles ---")
    for serv in servicios:
        print(f"{serv['id']}. {serv['nombre']} - ${serv['precio']}")


def pedir_turno():
    print("\n--- Pedir Turno ---")

    nombre = input("Nombre de la mascota: ")
    if nombre == "":
        print("Error: ingresa un nombre")
        return

    mostrar_servicios()
    try:
        serv_id = int(input("Elige el servicio (número): "))
    except:
        print("Error: ingresa un número")
        return

    mostrar_veterinarios()
    try:
        vet_id = int(input("Elige el veterinario (número): "))
    except:
        print("Error: ingresa un número")
        return

    fecha = input("Fecha (dd/mm/aaaa): ")
    hora = input("Hora (hh:mm): ")

    # Buscar el servicio y veterinario elegidos
    servicio_elegido = None
    for serv in servicios:
        if serv['id'] == serv_id:
            servicio_elegido = serv
            break

    veterinario_elegido = None
    for vet in veterinarios:
        if vet['id'] == vet_id:
            veterinario_elegido = vet
            break

    if servicio_elegido and veterinario_elegido:
        nuevo_turno = {
            "id": len(turnos) + 1,
            "mascota": nombre,
            "servicio": servicio_elegido['nombre'],
            "veterinario": veterinario_elegido['nombre'],
            "fecha": fecha,
            "hora": hora
        }

        turnos.append(nuevo_turno)
        print(f"¡Turno agendado para {nombre}!")
    else:
        print("Error: servicio o veterinario no válido")


def ver_turnos():
    print("\n--- Turnos Agendados ---")
    if len(turnos) == 0:
        print("No hay turnos")
        return

    for turno in turnos:
        print(f"{turno['id']}. {turno['mascota']} - {turno['servicio']}")
        print(f"   con {turno['veterinario']} el {turno['fecha']} a las {turno['hora']}")


def buscar_turno():
    nombre = input("Nombre de la mascota: ")
    encontrados = []

    for turno in turnos:
        if turno['mascota'].lower() == nombre.lower():
            encontrados.append(turno)

    if encontrados:
        print(f"\nTurnos de {nombre}:")
        for t in encontrados:
            print(f"- {t['fecha']} {t['hora']}: {t['servicio']}")
    else:
        print("No se encontraron turnos")


def cancelar_turno():
    ver_turnos()
    if len(turnos) == 0:
        return

    try:
        id_turno = int(input("ID del turno a cancelar: "))
    except:
        print("Error: ingresa un número")
        return

    for i in range(len(turnos)):
        if turnos[i]['id'] == id_turno:
            turnos.pop(i)
            print("Turno cancelado")
            return

    print("No se encontró el turno")


def agregar_mascota():
    print("\n--- Registrar Mascota ---")
    nombre = input("Nombre: ")
    animal = input("Tipo (perro/gato/etc): ")
    raza = input("Raza: ")
    edad = input("Edad: ")
    dueño = input("Dueño: ")

    nueva_mascota = {
        "id": len(mascotas) + 1,
        "nombre": nombre,
        "animal": animal,
        "raza": raza,
        "edad": edad,
        "dueño": dueño
    }

    mascotas.append(nueva_mascota)
    print(f"¡{nombre} registrado/a!")


def ver_mascotas():
    print("\n--- Mascotas Registradas ---")
    if len(mascotas) == 0:
        print("No hay mascotas registradas")
        return

    for mascota in mascotas:
        print(f"{mascota['id']}. {mascota['nombre']} ({mascota['animal']})")
        print(f"   Raza: {mascota['raza']}, Edad: {mascota['edad']}")
        print(f"   Dueño: {mascota['dueño']}")