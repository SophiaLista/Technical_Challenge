def validar_tablero(tablero):
    if not tablero or len(tablero) == 0:
        return False, "El tablero está vacío"
    
    longitud_fila = len(tablero[0])
    for fila in tablero:
        if len(fila) != longitud_fila:
            return False, "Las filas no tienen la misma longitud"
    
    for fila in tablero:
        for celda in fila:
            if celda not in [0, 1]:
                return False, "El tablero solo debe contener 0 y 1"
    
    return True, "Tablero válido"

def contar_minas(tablero):
    filas = len(tablero)
    columnas = len(tablero[0])
    
    resultado = [[0 for _ in range(columnas)] for _ in range(filas)]
    
    direcciones = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    
    for f in range(filas):
        for c in range(columnas):
            if tablero[f][c] == 1:
                resultado[f][c] = 9
                continue
            
            contador_minas = 0
            for df, dc in direcciones: 
                nueva_f, nueva_c = f + df, c + dc
                
                if (0 <= nueva_f < filas) and (0 <= nueva_c < columnas):
                    if tablero[nueva_f][nueva_c] == 1:
                        contador_minas += 1
            
            resultado[f][c] = contador_minas
    
    return resultado

def procesar_tablero(tablero):
    es_valido, mensaje = validar_tablero(tablero)
    
    if not es_valido:
        print(f"Error: {mensaje}")
        return None
    
    return contar_minas(tablero)


tablero_entrada = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 0]
]


print("Tablero de entrada:")
for fila in tablero_entrada:
    print(fila)

tablero_resultado = procesar_tablero(tablero_entrada)

print("\nTablero de resultados:")
if tablero_resultado:
    for fila in tablero_resultado:
        print(fila)