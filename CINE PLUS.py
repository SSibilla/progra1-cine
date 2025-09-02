
import random

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
    letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    butaca=input("Ingrese butaca a reservar, filas 1 a 6, posicion A a I , 0 para terminar: ")
    #tomo al string como una lista, donde el primer elem es la fila y el segundo la col
    while butaca!="0":
        f=int(butaca[0])-1 #butaca[0] es la fila y butaca[1] es la columna
        c=letras.index(butaca[1]) #para la columna, uso lista auxiliar de letras
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


