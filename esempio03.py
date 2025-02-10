# esempio_03 #partita tennis #riprodurre game, deuce, set
PlayerA = 1
PlayerB = 2
punteggio_gameA = [0 , 15 , 30 , 40 ]
punteggio_gameB = [0 , 15 , 30 , 40 ]
punteggio_PlayerA = 0
punteggio_PlayerB = 0
vantaggioA = 0
vantaggioB = 0
partita = True

while partita : 
    punto = int(input("Chi ha fatto punto? Indica con 1 se ha fatto punto il PlayerA e con 2 se ha fatto punto il PlayerB! "))
    if punto not in [PlayerA , PlayerB] :
        print("!!!!Hai sbagliato ad inserire il numero!!!!")

    if punto == PlayerA :
        punteggio_PlayerA = punteggio_gameA[min(punteggio_gameA.index(punteggio_PlayerA) + 1 , 3)]
        print("Sta " , punteggio_PlayerA , " - " , punteggio_PlayerB)
        
        if punteggio_PlayerA == 40 :
            vantaggioA += 1
            if punteggio_PlayerB == 40 and punteggio_PlayerA == 40 :
              print("Deuce!")
              if vantaggioA == vantaggioB + 1 :
               print("PlayerA é in vantaggio!")
              if vantaggioA == vantaggioB + 2 :
               print("PlayerA ha vinto ai vantaggi il game!")
               break
        if punteggio_PlayerB <= 30 and punteggio_PlayerA + vantaggioA == 42 :
            print("PlayerA ha vinto il game!")
            break


  
    if punto == PlayerB :
        punteggio_PlayerB = punteggio_gameB[min(punteggio_gameB.index(punteggio_PlayerB) + 1 , 3)]
        print("Sta " , punteggio_PlayerA , " - " , punteggio_PlayerB)
        
        if punteggio_PlayerB == 40 :
            vantaggioB += 1
            if punteggio_PlayerA == 40 and punteggio_PlayerB == 40 :
              print("Deuce!")
              if vantaggioB == vantaggioA + 1 :
               print("PlayerB é in vantaggio!")
              if vantaggioB == vantaggioA + 2 : 
               print("PlayerB ha vinto ai vantaggi il game!")
               break
        if punteggio_PlayerA <= 30 and punteggio_PlayerB + vantaggioB == 42 :
            print("PlayerB ha vinto il game!")
            break
