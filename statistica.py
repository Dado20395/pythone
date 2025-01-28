voti = []
valutazioni = input("Inserisci una valutazione da 1 a 10 del film! ")

while valutazioni.isdigit() :
    voti.append(int(valutazioni))
    valutazioni = input("Inserisci una valutazione da 1 a 10 del film! ")
    
print(voti)
voti.remove(min(voti))
print(voti)
voti.remove(max(voti))
print(voti)

print  ("La media della valutazione dei clienti é ",sum(voti)/len(voti))
