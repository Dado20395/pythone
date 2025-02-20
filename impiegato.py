class Employee :
    def __init__ (self, nome, cognome, salario) :
        self.nome = nome
        self.cognome = cognome
        self.salario = salario

    def __repr__(self):
        return ("Employee " + self.nome + " " + self.cognome + " " + str(self.salario))
        
class Manager(Employee):
    def __init__(self, nome, cognome, salario, reparto):
         self.nome = nome
         self.cognome = cognome
         self.salario = salario
         self.reparto = reparto
    def __repr__(self):
         return ("Manager " + self.nome + " " + self.cognome + " " +  str(self.salario) + " "  + self.reparto)
    
impiegato = Employee("Mario", "Rossi", 1500)
manager = Manager("Lucio", "Corsi", 2000, "Marketing")

print(impiegato)
print(manager)
