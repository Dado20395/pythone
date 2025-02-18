
class Message :
    def __init__(self, mittente, destinatario):
        self.mittente = mittente
        self.destinatario = destinatario
        self.testo = ""
    def append(self, riga):
        self.testo += riga + "\n"
    def toString(self):
        return "Mittente: "  + self.mittente + "\nDestinatario: " + self.destinatario + "\n" + self.testo

messaggio = Message("Luca@example.com", "Franco@example.com")
messaggio.append("Ciao, come stai?")
messaggio.append("Spero che tu stia passando una buona giornata.")
messaggio.append("A presto!")

print(messaggio.toString())
