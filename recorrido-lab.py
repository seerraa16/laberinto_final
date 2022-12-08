def recorre_laberinto(laberinto):
    columna = fila = 0 #Coordenadas iniciales
    n = 5
    movimientos = ['Abajo']
    while (fila < n-1 and columna < n-1): #Definimos los movimientos arriba, abajo, derecha e izquierda
        if movimientos[-1] != 'Arriba' and fila + 1 < n and laberinto[fila + 1][columna] != 'X':
            fila += 1
            movimientos.append('Abajo')
        elif movimientos[-1] != 'Abajo' and fila - 1 > 0 and laberinto[fila - 1][columna] != 'X':
            fila -= 1
            movimientos.append('Arriba')
        elif movimientos[-1] != 'Izquierda' and columna + 1 < n and laberinto[fila][columna + 1] != 'X':
            columna += 1
            movimientos.append('Derecha')
        elif movimientos[-1] != 'Derecha' and columna - 1 > 0 and laberinto[fila][columna - 1] != 'X':
            columna -= 1
            movimientos.append('Izquierda')
        else:
            movimientos.append('No hay salida')