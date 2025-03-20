import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery') #grafico a scalini (chiamato anche "step plot"), che viene utilizzato per rappresentare dati che cambiano in modo discontinui


y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 6.6] #Sull'asse verticale vengono rappresentati i valori della lista y, che vanno da un minimo di 2.6 a un massimo di 6.6. 


fig, ax = plt.subplots()

ax.stairs(y, linewidth=2.5)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),   #Sull'asse orizzontale vengono rappresentati gli indici dei dati. In questo caso, gli indici vanno da 0 a 7, corrispondenti agli 8 valori nella lista y.
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()

# Il grafico a scalini è utile per rappresentare un cambiamento netto nei valori, senza interpolazione tra i punti. 
# In altre parole, il grafico mostra i valori come se fossero mantenuti costanti fino al punto successivo, dove il valore "salta" verso il nuovo valore.
# Questo tipo di grafico è molto utile per osservare e visualizzare le variazioni improvvise di un valore o per tracciare cambiamenti che avvengono in modo discreto, come il prezzo di un prodotto che cambia a intervalli regolari o la variazione di un parametro in un esperimento.
