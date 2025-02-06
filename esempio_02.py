num = int(input("Inserisci unn numero"))
letter = input("Inserisci una lettera")

for i in range(1 + num) :
    linea = letter * (2 * i - 1)
    print(linea.center(4 * num - 1))
