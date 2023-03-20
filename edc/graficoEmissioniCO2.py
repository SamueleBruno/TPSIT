import matplotlib as mpl
mpl.use('TkAgg') 

import matplotlib.pyplot as plt
import csv

# LETTURA FILE
year = []
total = []
gasFuel = []
liquidFuel = []
solidFuel = []
cement = []
gasFlaring = []
preCapita = []

data_file = open("/Users/simonebasso/Desktop/python/edcCSV/CO2_emissions.csv")
data_reader = csv.reader(data_file, delimiter=',')
next(data_reader)

for row in data_reader:
    year.append(int(row[0]))
    total.append(int(row[1]))
    gasFuel.append(float(row[2]))
    liquidFuel.append(float(row[3]))
    solidFuel.append(float(row[4]))
    cement.append(float(row[5]))
    gasFlaring.append(float(row[6]))
    
    if (row[7] != ''):
        preCapita.append(float(row[7]))
    else:
        preCapita.append(0.0)
    

# SUDDIVISIONE DEL FOGLIO IN 6 PARTI
fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = plt.subplots(7, 1)

# GRAFICO GAS FUEL
ax1.plot(year, gasFuel, "o-b")
ax1.set_xlabel("year")
ax2.set_ylabel("gas fuel")

# GRAFICO TOTAL
ax2.plot(year, liquidFuel, "o-b")
ax2.set_xlabel("year")
ax2.set_ylabel("total")

# GRAFICO LIQUID FUEL
ax3.plot(year, liquidFuel, "o-b")
ax3.set_xlabel("year")
ax3.set_ylabel("liquid fuel")

# GRAFICO SOLID FUEL
ax4.plot(year, solidFuel, "o-b")
ax4.set_xlabel("year")
ax4.set_ylabel("solid fuel")

# GRAFICO CEMENT
ax5.plot(year, cement, "o-b")
ax5.set_xlabel("year")
ax5.set_ylabel("cement")

# GRAFICO GAS FLARING
ax6.plot(year, gasFlaring, "o-b")
ax6.set_xlabel("year")
ax6.set_ylabel("gas flaring")

# GRAFICO PRE CAPITA
ax7.plot(year, preCapita, "o-b")
ax7.set_xlabel("year")
ax7.set_ylabel("pre capita")

plt.show()