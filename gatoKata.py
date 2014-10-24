# coding: utf8
template = " 1 │ 2 │ 3 \n───┼───┼───\n 4 │ 5 │ 6 \n───┼───┼───\n 7 │ 8 │ 9 "
turn = 0
winner = ""

def GetTablero():
    """
        Esta funcion debe regresar el tablero en forma de cadena
        Nota: Usar el template de arriba
    """
    global template
    return template
    
    raise NotImplementedError

def JuegoContinua():
    """
        Debe de regresar verdadero si el juego continua o false si ha terminado
    """
    global winner
    global template
    
    data = template.replace(" ","").replace("{","").replace("}","").replace("│","").replace("┼","").replace("─","").replace("\n","")
    datawonum = data.replace("X","").replace("O","")

    if  datawonum == "":
        winner = "Tie"
        return False
    elif (data[0]+data[1]+data[2]) == "XXX" or (data[3]+data[4]+data[5]) == "XXX" or (data[6]+data[7]+data[8]) == "XXX" or (data[0]+data[3]+data[6]) == "XXX" or (data[1]+data[4]+data[7]) == "XXX" or (data[2]+data[5]+data[8]) == "XXX" or (data[0]+data[4]+data[8]) == "XXX" or (data[2]+data[4]+data[6]) == "XXX":
        winner = "X"
        return False
    elif (data[0]+data[1]+data[2]) == "OOO" or (data[3]+data[4]+data[5]) == "OOO" or (data[6]+data[7]+data[8]) == "OOO" or (data[0]+data[3]+data[6]) == "OOO" or (data[1]+data[4]+data[7]) == "OOO" or (data[2]+data[5]+data[8]) == "OOO" or (data[0]+data[4]+data[8]) == "OOO" or (data[2]+data[4]+data[6]) == "OOO":
        winner = "O"
        return False
    else:
        return True
    raise NotImplementedError

def IntentarTirada(casilla):
    """
        Esta funcion recibe el intento del jugador por ocupar una casilla
        y regresa una cadena segun los siguientes criterios:
        Si esta fuera de rango: "La tirada debe de estar entre 1 y 9"
        Si la casilla esta ocupada: "La casilla ya esta ocupada"
        Si x a ganado: "Felicidades X as ganado. weeee"
        Si o a ganado: "Felicidades O as ganado. weeee"
        Si el juego a quedado empatado: "Juego empatado. :("
        Ninguna de las anteriores: "" (cadena vacia)
    """
    global turn
    global winner
    global template
    
    if int(casilla) > 9 or int(casilla) < 1:
        return "La tirada debe de estar entre 1 y 9"
    elif template.find(str(casilla)) == -1:
        return "La casilla ya esta ocupada"
    else:
        if turn % 2 == 0:
            template = template.replace(str(casilla),"X")
            turn += 1
            JuegoContinua()
            if winner == "X":
                return "Felicidades X as ganado. weeee"
        elif turn % 2 == 1:
            template = template.replace(str(casilla),"O")
            turn += 1
            JuegoContinua()
            if winner == "O":
                return "Felicidades O as ganado. weeee"
        if turn == 9:       
            return "Juego empatado. :("
        return ""
    
    
    raise NotImplementedError

def IniciaJuego():
    """
        Esta function se puede utilizar para re iniciar variables.
        Si no se usa se puede dejar vacia
    """
    global template
    global turn
    global winner
    template = " 1 │ 2 │ 3 \n───┼───┼───\n 4 │ 5 │ 6 \n───┼───┼───\n 7 │ 8 │ 9 "
    turn = 0
    winner = ""
    return None

if __name__ == '__main__':
    IniciaJuego() 
    while(JuegoContinua()):
        print(GetTablero())
        msg = ""
        casilla = int(input("Escoge una casilla: "))
        msg = IntentarTirada(casilla)
        if msg != "":
            print(msg)