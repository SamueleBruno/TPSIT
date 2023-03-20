import csv
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('TkAgg')

# LETTURA FILE
year = []
value = []

data_file = open("/Users/simonebasso/Desktop/python/edcCSV/Temperature_Anomaly.csv")
data_reader = csv.reader(data_file, delimiter=',')

for i in range(5):
    next(data_reader)

for row in data_reader:
    print(row)
    year.append(int(row[0]))
    value.append(float(row[1]))

# SUDDIVISIONE DEL FOGLIO IN 6 PARTI
fig, (ax1) = plt.subplots(1, 1)

# GRAFICO
ax1.plot(year, value, "o-b")
ax1.set_xlabel("year")
ax1.set_ylabel("value")

plt.show()