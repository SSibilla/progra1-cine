"""5. Desarrollar un programa que permita realizar reservas en una sala de cine de N
filas con M butacas por cada fila. Desarrollar las siguientes funciones y utilizarlas
en un mismo programa:
mostrar_butacas: Mostrará por pantalla el estado de cada una de las butacas
del cine. Esta función deberá ser invocada antes de que se realice la reserva, y
se volverá a invocar luego de la misma con los estados actualizados.
reservar: Deberá recibir una matriz y la butaca seleccionada, y actualizará la
sala en caso de estar disponible dicha butaca. La función devolverá True/False
si logró o no reservar la butaca.
cargar_sala: Recibirá una matriz como parámetro y la cargará con valores
aleatorios para simular una sala con butacas ya reservadas.
butacas_libres: Recibirá como parámetro la matriz y retornará cuántas butacas
desocupadas hay en la sala.
butacas_contiguas: Buscará la secuencia más larga de butacas libres contiguas
en una misma fila y devolverá las coordenadas de inicio de la misma."""

import random

#creo sala de cine e inicializo la sala en libre
def crear_sala():
    matriz=[]
    for fila in range(6):
        matriz.append([])
        for col in range(9):
            matriz[fila].append("L")
    return matriz


#imprimo en pantalla la sala, pongo las letras como columnas para visualizar + facil
def mostrar_Sala(matriz):
    print ("CINEPLUS sala de cine")
    print ("  A B C D E F G H I")
    for i,fila in enumerate(matriz):
        print(i+1," ".join(fila))


#simular ocupacion de la sala
def precarga_aleatoria(matriz):
    for f in range(1,4):#entre fila 2 y 4 (recordar que nuestra fila 1 es la 0 realmente)
        for c in range(1,8): #entre columna 2 y 8
            if random.random()<0.7:
                matriz[f][c]="O"


def reservar(matriz):
    letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    butaca=input("Ingrese butaca a reservar, filas 1 a 6, posicion A a I , 0 para terminar: ")
    #tomo al string como una lista, donde el primer elem es la fila y el segundo la col
    while butaca!="0":
        f=int(butaca[0])-1 #butaca[0] es la fila y butaca[1] es la columna
        c=letras.index(butaca[1])
        if matriz[f][c]=="L":
            print("Se ha reservado su butaca")
            matriz[f][c]="R"
        else:
            print("Butaca no disponible!")
        butaca = input("Ingrese butaca a reservar, filas 1 a 6, posicion A a I , 0 para terminar: ")
    return matriz #no devuelve T o F, sino que directamente devuelve la matriz modificada

def cantidad_de_butacas_libres(matriz):
    cont=0
    for fila in matriz:
        for col in fila:
            if col=="L":
                cont+=1
    print("cantidad de butacas LIBRES en la sala: ",cont)



SALA=crear_sala()
mostrar_Sala(SALA)
precarga_aleatoria(SALA)
mostrar_Sala(SALA)
reservar(SALA)
mostrar_Sala(SALA)
cantidad_de_butacas_libres(SALA)

