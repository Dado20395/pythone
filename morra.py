PlayerA = 0
PlayerB = 0
pareggio = 0
partita = True


while partita :
    punto = input("Giochiamo a Morra! Inserisci C per Carta, F per Forbice o S per Sasso, separati da uno spazio! ")
    punto.upper()
    if punto == "C C" or punto == "F F" or punto == "S S" :
        pareggio += 1
    if punto == "C S" or punto == "F C" or punto == "S F"  :
        PlayerA += 1
    if punto == "S C" or punto == "C F" or punto == "F S" :
        PlayerB += 1
    else :
       print("Hai sbagliato ad inserire il risultato!")
    print("Sta" , PlayerA , " - " , PlayerB)
    print("Il numero dei pareggi è : " , pareggio)

    if PlayerB == 3 :
        print("Il vincitore è PlayerB che ha raggiunto per primo i" ,  PlayerB , "punti")
        partita = False
    elif PlayerA == 3 :
        print("Il vincitore è PlayerA che ha raggiunto per primo i" ,  PlayerA , "punti")
        partita = False
