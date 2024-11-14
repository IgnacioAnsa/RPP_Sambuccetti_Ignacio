from funciones.funciones import *

# Ejercicio 1:
# Se debe modularizar correctamente, utilizar parámetros opcionales y cumplir reglas de estilo.
# No puede haber código repetido, ni funciones que realicen múltiples tareas. No se puede
# utilizar sets, diccionarios, ni tuplas.
# Una empresa se dedica al almacenamiento y posterior distribución de camisetas de fútbol en
# todo el país. Para ello cuentan con 6 depósitos: Tierra del Fuego, Tucumán, Mendoza, Bs
# As, Misiones y Santa Fé.
# Los depósitos almacenan camisetas de 5 equipos que son las que más se venden:
# Barcelona, Inter Miami, PSG, Manchester City y Real Madrid.

depositos = ["Tierra del Fuego","Tucumán","Mendoza","BsAs","Misiones","Santa Fé"]
camisetas = ["Barcelona","Inter Miami","PSG","Manchester City","Real Madrid"]
stocks = [[5,8,78,4,123],[466,646,87,98,787],[454,654,556,112,56],[456,1232,546,546,564],[232,132,454,546,565],[45,45,132,122,45]]
totales = [500,400,666,999,555,213]


# Los puntos 2 y 3 deben utilizar la misma función (calcular_totales). La misma debe poder
# sumar por filas o por columnas. Además, deberán utilizar la función estimar_stock que recibe
# una lista de totales, una lista de strings con el nombre de cada total y reciba por parámetro
# cuál es el límite que debe tomar para informar.
# Realizar un menú de opciones:

# 1. Obtener existencias: para ello deberá generar una función que cargue
# secuencialmente, de tal forma que la intersección de cada fila y cada columna
# corresponda a la cantidad de camisetas de un equipo en un depósito. Esto es carga
# secuencial.
# 2. Mostrar depósitos que tienen en stock más de 10.000 camisetas.
# 3. Mostrar equipos que hay en stock más de 5.000 camisetas.
# 4. Obtener máxima cantidad de camisetas de cada equipo. Mostrar en qué depósito se
# encuentra.
# 5. Cargar ventas: se deberá poder cargar ventas de un determinado producto para un
# determinado depósito. Esto es carga distribuida o aleatoria. Al cargarse las ventas
# se deben restar los productos vendidos del stock y generar una matriz con la
# recaudación que reciba el listado de precios por parámetro, en caso de no recibir un
# listado deberá tener un precio de 100 cada producto. Utilizar parámetro opcional.

# Ejercicio 2:
# En este ejercicio deberán programar funciones para realizar operaciones sobre matrices
# cuadradas. Por ello se debe validar que las matrices que se reciben tengan la misma cantidad
# de filas y columnas.
# 1. Generar una función que calcule la media geométrica de filas o columnas de una matriz
# cuadrada.
# 2. Generar una función que calcule la suma de las diagonales principal y secundaria de una
# matriz.
# Ejemplo:
# 1 2 3
# 4 5 6
# 7 8 9
# Devuelve 30.
# 3. Generar una función que reciba una matriz y devuelva su transpuesta.
# 4. A la función del ejercicio 2 agregar un parámetro que permita seleccionar si lo que se
# pretende recibir como retorno es la suma de ambas diagonales, solo la de la diagonal
# principal o solo la de la diagonal secundaria.


ejecutar = True
cargar = False

while ejecutar == True:

    opcion = input("ingrese la opcion que desea realizar: ")
    
    print("1. Obtener existencias: ")
    print("2. Mostrar depósitos que tienen en stock más de 10.000 camisetas: ")
    print("3. Mostrar equipos que hay en stock más de 5.000 camisetas:  ")
    print("4. Obtener máxima cantidad de camisetas de cada equipo: ")
    print("5. Cargar ventas: ")

    match opcion:

        case "1":
            
            if cargar == False:

                stocks = inicializar_matriz(len(depositos), len(camisetas))
                for i in range(len(stocks)):
                    for j in range(len(stocks[i])):
                        valor = (input(f"ingrese la camiseta {camisetas[j]} en deposito {depositos[i]}  "))
                        stocks[i][j] = valor
                
                cargar = True
            else:
                for i in range(len(depositos)):
                    for j in range(len(camisetas)):
                        print(f"se encuentran {stocks[i][j]} camisetas del {camisetas[j]} en {depositos[i]}")

        case "2":

            # 2. Mostrar depósitos que tienen en stock más de 10.000 camisetas.
            # Los puntos 2 y 3 deben utilizar la misma función (calcular_totales). La misma debe poder
            # sumar por filas o por columnas. Además, deberán utilizar la función estimar_stock que recibe
            # una lista de totales, una lista de strings con el nombre de cada total y reciba por parámetro
            # cuál es el límite que debe tomar para informar.
            
            print(calcular_totales(stocks, depositos, camisetas))

            
            
        
        # case "4":
        #     # 4. Obtener máxima cantidad de camisetas de cada equipo. Mostrar en qué depósito se
        #     # encuentra.

            



                
                        








                



    
