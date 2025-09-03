
import random
letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
numeros_filas=["1","2","3","4","5","6"]

#creo SALA de cine e inicializo la SALA en libre
def crear_sala():
    matriz=[]
    for fila in range(6):
        matriz.append([])
        for col in range(9):
            matriz[fila].append("L")
    return matriz


#imprimo en pantalla la SALA, pongo las letras como columnas para visualizar + facil
def mostrar_sala(matriz):
    print ("CINEPLUS SALA de cine")
    print ("  A B C D E F G H I")
    for i,fila in enumerate(matriz):
        print(i+1," ".join(fila)) #join une todos los elementos de la fila y los separa con un espacio


#simular ocupacion de la SALA
def precarga_aleatoria(matriz):
    for f in range(1,4):#entre fila 2 y 4 (recordar que nuestra fila 1 es la 0 realmente)
        for c in range(1,8): #entre columna 2 y 8
            if random.random()<0.7: #aprox 70%
                matriz[f][c]="O"


def reservar(matriz):
    butaca=input("Ingrese butaca a reservar, filas 1 a 6, posicion A a I , 0 para terminar: ")
    while butaca!="0":
        butaca = validar_butaca(butaca)
        numero = butaca[:-1]
        letra = butaca[-1]
        f = int(numero) - 1
        c = letras.index(letra)
        if matriz[f][c]=="L":
            print("Se ha reservado su butaca")
            matriz[f][c]="R"
        else:
            print("Butaca no disponible!")
        butaca = input("Ingrese butaca a reservar, filas 1 a 6, posicion A a I , 0 para terminar: ")
    return matriz

def cantidad_de_butacas_libres(matriz):
    cont=0
    for fila in matriz:
        for col in fila:
            if col=="L":
                cont+=1
    print("cantidad de butacas LIBRES en la SALA: ",cont)

def validar_opcion_menu(opcion):
    posibilidades=["0","1","2","3","4","5","6","7"]
    while opcion not in posibilidades:
        opcion = input("⚠️ Opcion no valida, vuelva a intentarlo: ")
    return opcion

def validar_butaca(butaca):
    butaca=butaca.upper()
    letra=butaca[-1]
    numero=butaca[:-1]
    if butaca=="0":
        return None
    while letra not in letras or numero not in numeros_filas:
        print("⚠️ Entrada inválida. Use número+letra (ej: 3C).")
        butaca = input("Ingrese butaca (ej. 3C) o 0 para salir: ").upper()
        letra = butaca[-1]
        numero = butaca[:-1]
    return butaca

def menu():
    SALA=crear_sala()
    precarga_aleatoria(SALA)
    recaudacion=0
    opcion=" "
    while opcion != "0":
        print("\n=== MENÚ CINEPLUS ===")
        print("1) Mostrar SALA")
        print("2) Reservar butaca")
        print("3) Cancelar reserva")
        print("4) Confirmar venta")
        print("5) Buscar butacas juntas")
        print("6) Estadísticas")
        print("7) Recaudación")
        print("0) Salir")

        opcion = input("Elegí una opción: ")
        validar_opcion_menu(opcion)

        if opcion == "1":
            mostrar_sala(SALA)
        elif opcion == "2":
            mostrar_sala(SALA)
            SALA = reservar(SALA)
            mostrar_sala(SALA)
        elif opcion == "3":
            SALA = cancelar_reserva(SALA)
        elif opcion == "4":
            SALA, recaudacion = confirmar_venta(SALA, recaudacion)
        elif opcion == "5":
            buscar_butacas_juntas(SALA)
        elif opcion == "6":
            cantidad_de_butacas_libres(SALA)
        elif opcion == "7":
            mostrar_recaudacion(recaudacion)
        elif opcion == "0":
            print("¡Gracias por usar CINEPLUS! 👋")
        else:
            print("Opción inválida.")
    return SALA,recaudacion

menu()


