import random

ultima_partida = []  

def pedir_opcion(nombre):
    opcion = input(f"{nombre}, elige: piedra, papel o tijeras: ").lower()
    while opcion not in ["piedra", "papel", "tijeras"]:
        print("Opción no válida.")
        opcion = input(f"{nombre}, elige: piedra, papel o tijeras: ").lower()
    return opcion

def jugar_contra_computadora():
    jugador = pedir_opcion("Jugador")
    computadora = random.choice(["piedra", "papel", "tijeras"])
    print("La computadora eligió:", computadora)

    if jugador == computadora:
        resultado = "Empate"
    elif (jugador == "piedra" and computadora == "tijeras") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijeras" and computadora == "papel"):
        resultado = "Ganaste"
    else:
        resultado = "Perdiste"

    print(resultado)
    ultima_partida[:] = ["Computadora", jugador, computadora, resultado]

def jugar_multijugador():
    nombre1 = input("Nombre del Jugador 1: ")
    nombre2 = input("Nombre del Jugador 2: ")

    j1 = pedir_opcion(nombre1)
    print("\n" * 50)  
    j2 = pedir_opcion(nombre2)

    if j1 == j2:
        resultado = "Empate"
    elif (j1 == "piedra" and j2 == "tijeras") or \
         (j1 == "papel" and j2 == "piedra") or \
         (j1 == "tijeras" and j2 == "papel"):
        resultado = f"Ganó {nombre1}"
    else:
        resultado = f"Ganó {nombre2}"

    print(resultado)
    ultima_partida[:] = ["Multijugador", f"{nombre1} ({j1})", f"{nombre2} ({j2})", resultado]

def ver_estadisticas():
    print("Última Partida")
    print("Modo:", ultima_partida[0])
    print("Jugador 1:", ultima_partida[1])
    print("Jugador 2:", ultima_partida[2])
    print("Resultado:", ultima_partida[3])

def menu():
    while True:
        print("Menú Principal ")
        print("1. Contra la computadora")
        print("2. Multijugador (2 jugadores)")
        if ultima_partida:  
            print("3. Ver estadísticas de la última partida")
            print("4. Regresar al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            jugar_contra_computadora()
        elif opcion == "2":
            jugar_multijugador()
        elif opcion == "3" and ultima_partida:
            ver_estadisticas()
        elif opcion == "4" and ultima_partida:
            print("Reiniciando menú...")
        else:
            print("Opción no válida.")

menu()

