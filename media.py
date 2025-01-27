n = 0
somma = 0
numero_ins = input("inserisci un numero e ti farò la media: ")

while   numero_ins.isdigit():
    
    n += 1
    somma += float(numero_ins)
    numero_ins = input("inserisci un altro numero: ")

print("la media totale dei" , n , "numeri inseriti è" , somma/n)
