row = 0
col = 0
cellrow = 0
cellcol = 0

def numadj(board):
    global cellcol
    global cellrow
    global col
    global row
    adj = 0
    if cellcol == 0:
        if cellrow == 0:
            if board[cellcol][cellrow+1] == "*":
                adj += 1
            if board[cellcol+1][cellrow] == "*":
                adj += 1
            if board[cellcol+1][cellrow+1] == "*":
                adj += 1
        elif cellrow == (row-1):
            if board[cellcol][cellrow-1] == "*":
                adj += 1
            if board[cellcol-1][cellrow] == "*":
                adj += 1
            if board[cellcol-1][cellrow-1] == "*":
                adj += 1
        else:
            if board[cellcol][cellrow-1] == "*":
                adj += 1
            if board[cellcol][cellrow+1] == "*":
                adj += 1
            for row2 in range(-1,2):
                if board[cellcol+1][cellrow+row2] == "*":
                    adj += 1
    elif cellcol == (col-1):
        if cellrow == 0:
            if board[cellcol][cellrow+1] == "*":
                adj += 1
            if board[cellcol-1][cellrow] == "*":
                adj += 1
            if board[cellcol-1][cellrow+1] == "*":
                adj += 1
        elif cellrow == (row-1):
            if board[cellcol-1][cellrow] == "*":
                adj += 1
            if board[cellcol-1][cellrow-1] == "*":
                adj += 1
            if board[cellcol][cellrow-1] == "*":
                adj += 1
        else:
            if board[cellcol][cellrow-1] == "*":
                adj += 1
            if board[cellcol][cellrow+1] == "*":
                adj += 1
            for row3 in range(-1,2):
                if board[cellcol-1][cellrow+row3] == "*":
                    adj += 1
    else:
        if cellrow == 0:
            for row4 in range(0,2):
                if board[cellcol-1][cellrow+row4] == "*":
                    adj += 1
            for row5 in range(0,2):
                if board[cellcol+1][cellrow+row5] == "*":
                    adj += 1
            if board[cellcol][cellrow+1] == "*":
                adj += 1                
        elif cellrow == (row-1):
            for row6 in range(-1,1):
                if board[cellcol-1][cellrow+row6] == "*":
                    adj += 1
            for row7 in range(-1,1):
                if board[cellcol+1][cellrow+row7] == "*":
                    adj += 1
            if board[cellcol][cellrow-1] == "*":
                adj += 1
        else:
            for row8 in range(-1,2):
                if board[cellcol-1][cellrow+row8] == "*":
                    adj += 1
            for row8 in range(-1,2):
                if board[cellcol+1][cellrow+row8] == "*":
                    adj += 1
            if board[cellcol][cellrow-1] == "*":
                adj += 1
            if board[cellcol][cellrow+1] == "*":
                adj += 1
    return adj

def NextOfspring(u):
    """
        Esta funcion recibe un universo y regresa la siguiente generacion segun las reglas
        Nota: La funcion recibe la cadena el el formato establecido y lo regresa en el mismo formato
    """
    global cellrow
    global cellcol
    global col
    global row
    u2 = GetUniverse(u)
    splt = u2.split("\n")
    del splt[-1]
    copy = u2.split("\n")
    del copy[-1]
    cellcol = -1
    for line in splt:
        cellrow = 0
        cellcol += 1
        copy[cellcol] = ""
        for cell in line:
            tot = numadj(splt)
            if tot == 3 and cell == ".":
                copy[cellcol] += "*"
            elif (tot == 1 or tot == 0) and cell == "*":
                copy[cellcol] += "."
            elif (tot == 2 or tot == 3) and cell == "*":
                copy[cellcol] += "*"
            elif tot > 3 and cell == "*":
                copy[cellcol] += "."
            else:
                copy[cellcol] += "."
            cellrow += 1
    final = ""
    for item in copy:
        final += item
    return (str(col)+str(row)+final)
    
    raise NotImplementedError

def GetUniverse(u):
    """
        Esta funcion debe de regresar el universo en el formato establecido 
        pero regresa el universo sin el renglon de las dimenciones y con los saltos
        de linea correspondientes
    """
    global row
    global col
    if u[0:2].isdigit() == True:
        row = int(u[1])
        col = int(u[0])
    u2 = ""
    for row2 in range(0,col):
        u2 += u[(row2*row)+2:(row2*row)+2+row] + "\n"
    u = u2
    return u
    
    raise NotImplementedError

if __name__ == '__main__':
    print("Captura un universo (Linea por linea segun el formato y vacio para terminar)")
    u = ""
    line = input()
    while(line != ""):
        u += line
        line = input()
    option = input("Teclee n para ver la siguiente generacion y s para deter la simulacion")
    while(option == "n"):
        u = NextOfspring(u)
        print(GetUniverse(u))
        option = input()
    