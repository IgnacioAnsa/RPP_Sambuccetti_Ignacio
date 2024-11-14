def inicializar_matriz(cant_filas: int, cant_col: int, valor_inicial: any = 0)-> list:

    matriz = []

    for _ in range(cant_filas):

        filas = [valor_inicial] * cant_col

        matriz += [filas]
    
    return matriz

def calcular_totales(stocks: list, depositos: list, camisetas: list)-> list:

    totales = inicializar_matriz(len(depositos), len(camisetas))
    
    for i in range(len(stocks)):
        acumulador = 0
        for j in range(len(stocks[i])):
            acumulador += stocks[i][j]
            totales = acumulador
            print(f"hay un total de {acumulador} camisetas en {depositos[i]}")
        
    return totales

    


