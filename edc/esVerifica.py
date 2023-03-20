import csv
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('TkAgg')

anno = []
valore = []

data_file = open("/Users/simonebasso/Desktop/python/edcCSV/Temperature_Anomaly.csv")
data_reader = csv.reader(data_file, delimiter=',')

# "skippa" l'intestazione
for i in range(5):
    next(data_reader)

for row in data_reader:
    print(row) # stampo il contenuto del file
    anno.append(int(row[0]))
    valore.append(float(row[1]))

# suddivisione foglio
fig, (ax1) = plt.subplots(1, 1)
ax1.plot(anno, valore, "o-b")
ax1.set_xlabel("anno")
ax1.set_ylabel("valore")

plt.show()