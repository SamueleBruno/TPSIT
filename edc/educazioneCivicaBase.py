import matplotlib as mpl # riga inutile si utilizza SO windows
mpl.use('TkAgg') # riga inutile si utilizza SO windows

import matplotlib.pyplot as plt
import csv

# LETTURA FILE, inserire i dati nelle varie liste
mese = []
temperaturaMedia = []
giorniUtilizzoGiacca = []
giorniFrequentazioneScuola = []
giorniGiocoVideogame = []
data_file = open("/Users/simonebasso/Desktop/python/edcCSV/datiEducazioneCivica.csv")
data_reader = csv.reader(data_file, delimiter=',')

for row in data_reader:
    mese.append(int(row[0]))
    temperaturaMedia.append(float(row[1]))
    giorniUtilizzoGiacca.append(float(row[2]))
    giorniFrequentazioneScuola.append(int(row[3]))
    giorniGiocoVideogame.append(int(row[4]))

"""
# DISEGNO GRAFICO
fig, (ax1, ax2) = plt.subplots(2, 1) # fig = figura ed sta indicare il nostro foglio; plt.subplots(2, 1) suddivisione del foglio in due a metà 2 sta per la divisione orizzontale 1 sta per quante colonne ci sono; (ax1, ax2) asse1 = primo grafico asse2 = secondo grafico
# SB: fig.suptitle('Media dei voti di tutte le materie e ore di studio giornaliere medie nel periodo Gennaio-Giugno') # titolo della figura

# GRAFICO A LINEA ASSE 1
ax1.plot(mese, giorniUtilizzoGiacca, 'o-g') # metodo plot() utilizzato per i grafici a linea, serve a vedere l'andatura di una variabile nel tempo; prima si passa la lista che va in x poi quella che va in y; o-g specifica lo stile del grafico e il colore
ax1.set_xlabel('Mese')
ax1.set_ylabel('Giorni utilizzo Giacca')

# GRAFICO A LINEA ASSE 2
ax2.plot(mese, temperaturaMedia, 'o-r')
ax2.set_xlabel('Mese')
ax2.set_ylabel('Temperatura media')
"""

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
ax1.plot(mese, giorniUtilizzoGiacca, 'o-g')
ax1.set_xlabel('Mese')
ax1.set_ylabel('Giorni utilizzo Giacca')

ax2.plot(mese, temperaturaMedia, 'o-r')
ax2.set_xlabel('Mese')
ax2.set_ylabel('Temperatura media')

ax3.plot(mese, giorniFrequentazioneScuola, 'o-b')
ax3.set_xlabel('Mese')
ax3.set_ylabel('Giorni frequentazione scuola')

ax4.plot(mese, giorniGiocoVideogame, 'o-y')
ax4.set_xlabel('Mese')
ax4.set_ylabel('Giorni gioco videogame')

plt.show()

# metodo scatter() serve per il grafico a dispersione, serve a confrontare due variabili
