
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

def cantidad_de_butacas_libres(matriz):
    cont=0
    for fila in matriz:
        for col in fila:
            if col=="L":
                cont+=1
    print("cantidad de butacas LIBRES en la SALA: ",cont)

def reservar(matriz,letras,numeros_filas):
    butaca=input("Ingrese butaca a reservar, filas 1 a 6, posicion A a I , 0 para terminar: ")
    while butaca!="0":
        butaca = validar_butaca(butaca,letras,numeros_filas)

        if butaca != "0":
            numero = butaca[:-1]
            letra = butaca[-1]
            f = int(numero) - 1
            c = letras.index(letra)

        
            if matriz[f][c]=="L":
                if numero in ("3", "4"):
                    valor = 2000
                else:
                    valor = 1500
                print(f"Se ha reservado butaca: {numero}{letra} - ${valor}")
                matriz[f][c]="R"

            else:
                print("Butaca no disponible!")
            butaca = input("Ingrese butaca a reservar, filas 1 a 6, posicion A a I , 0 para terminar: ")


def cancelar_reserva(matriz,letras,numeros_filas):
    mostrar_sala(matriz)
    mostrar_butacas_reservadas(matriz,numeros_filas,letras)
    butaca=input("Ingrese butaca que desea cancelar la reserva (Ej 3C), filas 1 a 6, posicion A a I , 0 para terminar: ")

    while butaca!="0":
        butaca = validar_butaca(butaca,letras,numeros_filas)


        if butaca != "0":
            numero = butaca[:-1]
            letra = butaca[-1]
            f = int(numero) - 1
            c = letras.index(letra)
            
            if matriz[f][c]=="R":
                print("Se ha cancelado su reserva con exito")
                matriz[f][c]="L"

            else:
                print("La butaca elegida no esta reservada!")
            
            mostrar_butacas_reservadas(matriz,numeros_filas,letras)
            butaca = input("Ingrese butaca que desea cancelar la reserva (Ej 3C), filas 1 a 6, posicion A a I , 0 para terminar: ")


def validar_opcion_menu(opcion):
    posibilidades=["0","1","2","3","4","5","6","7"]
    while opcion not in posibilidades:
        opcion = input("⚠️ Opcion no valida, vuelva a intentarlo: ")
    return opcion

def validar_butaca(butaca,letras,numeros_filas):
    butaca=butaca.upper()
    letra=butaca[-1]
    numero=butaca[:-1]

    while (letra not in letras or numero not in numeros_filas) and butaca != "0":
        print("⚠️ Entrada inválida. Use número+letra (ej: 3C).")
        butaca = input("Ingrese butaca (ej. 3C) o 0 para salir: ").upper()
        letra = butaca[-1]
        numero = butaca[:-1]
    
    return butaca

def mostrar_butacas_reservadas(matriz,numeros_filas,letras):
    butacas_reservadas=[]
    valores = []

    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == "R":
                butacas_reservadas.append (f"{numeros_filas[i]}{letras[j]}")
                if numeros_filas[i] in ("3", "4"):
                    valores.append (2000)
                else:
                    valores.append (1500)        

    if len(butacas_reservadas) >0:
        print(f"BUTACAS RESERVADAS: {len(butacas_reservadas)}")
        for k in range (len(butacas_reservadas)):
            print(f"{butacas_reservadas[k]} ${valores[k]}")
    
    else:
        print("NO HAY BUTACAS RESERVADAS.")

def confirmar_venta(matriz, recaudacion,butacas_vendidas,numeros_filas, letras):
    mostrar_butacas_reservadas(matriz,numeros_filas,letras)
    butaca=input("Ingrese reserva que desea abonar, Ej: 1C (filas 1 a 6, posicion A a I) 0 para terminar: ")
    while butaca!="0":
        butaca = validar_butaca(butaca,letras,numeros_filas)
        numero = butaca[:-1]
        letra = butaca[-1]
        f = int(numero) - 1
        c = letras.index(letra)
        numero = int(numero)
        if matriz[f][c] == "R":
            print("Su compra ha sido CONFIRMADA")
            butacas_vendidas.append (f"{numeros_filas[f]}{letras[c]}")

            matriz[f][c] = "O"
            if numero in (3, 4):
                recaudacion += 2000
            else:
                recaudacion += 1500
            mostrar_butacas_reservadas(matriz,numeros_filas,letras)
            butaca=input("Ingrese reserva que desea abonar, Ej: 1C (filas 1 a 6, posicion A a I) 0 para terminar: ")

        else:
            print("La butaca seleccionada no se encuentra reservada!")
            butaca = input("Ingrese reserva que desea abonar, Ej: 1C (filas 1 a 6, posicion A a I) 0 para terminar: ")
    return recaudacion

def mostrar_recaudacion (recaudacion,butacas_vendidas):
    if len(butacas_vendidas)>0:
        print (f"BUTACAS VENDIDAS: {len(butacas_vendidas)}")
        for i in range (len(butacas_vendidas)):
            print (f"{butacas_vendidas[i]}")
        print ("La recaudacion diaria de la sala es: $", recaudacion)
    
    else:
        print ("NO HUBO BUTACAS VENDIDAS")
        print ("La recaudacion diaria de la sala es: $", recaudacion)

def mostrar_estadisticas (matriz, numeros_filas):
    libres     = sum(1 for fila in matriz for x in fila if x == "L")
    ocupadas   = sum(1 for fila in matriz for x in fila if x == "O")
    reservadas = sum(1 for fila in matriz for x in fila if x == "R")

    total_butacas = len(matriz) * len(matriz[0])
    ocupacion_total = ocupadas + reservadas
    porcentaje = round((ocupacion_total * 100) / total_butacas) if total_butacas > 0 else 0

    # Ocupación por fila (O + R por fila)
    ocup_por_fila = []
    for i, fila in enumerate(matriz):
        cant = sum(1 for x in fila if x in ("O", "R"))
        ocup_por_fila.append((i, cant))

    # Fila con más y menos ocupación
    fila_mas   = max(ocup_por_fila, key=lambda t: t[1])
    fila_menos = min(ocup_por_fila, key=lambda t: t[1])

    # Ranking de filas por ocupación
    ranking = ocup_por_fila[:]  # copio
    ranking.sort(key=lambda t: (-t[1], t[0]))  # primero más ocupadas, empate por índice

    ranking_mostrable = []
    for par in ranking:
        indice_fila = par[0]                 
        numero_de_fila = int(numeros_filas[indice_fila])  
        ranking_mostrable.append(numero_de_fila)

    print("\n=== ESTADÍSTICAS ===")
    print(f"Butacas libres: {libres}")
    print(f"Butacas ocupadas: {ocupadas}")
    print(f"Butacas reservadas: {reservadas}")
    print(f"Porcentaje de ocupación: {porcentaje}%")
    print(f"Fila con más ocupación: fila {numeros_filas[fila_mas[0]]} ({fila_mas[1]} butacas)")
    print(f"Fila con menos ocupación: fila {numeros_filas[fila_menos[0]]} ({fila_menos[1]} butacas)")
    print(f"Ranking de filas por ocupación: {ranking_mostrable}")

def menu(letras,numeros_filas,SALA,recaudacion,butacas_vendidas):
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
        opcion = validar_opcion_menu(opcion)

        if opcion == "1":
            mostrar_sala(SALA)
        elif opcion == "2":
            mostrar_sala(SALA)
            reservar(SALA,letras,numeros_filas)
            mostrar_sala(SALA)
        elif opcion == "3":
            cancelar_reserva(SALA,letras,numeros_filas)
        elif opcion == "4":
            recaudacion=confirmar_venta(SALA, recaudacion,butacas_vendidas,numeros_filas, letras)
        elif opcion == "5":
            buscar_butacas_juntas(SALA)
                        
        elif opcion == "6":
            mostrar_estadisticas (SALA, numeros_filas)

        elif opcion == "7":
            mostrar_recaudacion (recaudacion, butacas_vendidas)

        elif opcion == "0":
            print("¡Gracias por usar CINEPLUS! 👋")
        else:
            print("Opción inválida.")
    return SALA,recaudacion

def main ():
    letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    numeros_filas=["1","2","3","4","5","6"]
    butacas_vendidas = []

    SALA=crear_sala()
    precarga_aleatoria(SALA)
    recaudacion=0

    menu (letras,numeros_filas,SALA,recaudacion,butacas_vendidas)

main()


