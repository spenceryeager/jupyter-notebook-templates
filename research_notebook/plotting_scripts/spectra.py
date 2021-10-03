import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

workingfile = '/home/spenceryeager/Documents/calculations/cv/PF6_RUN1.TXT'
time_total = 24
scan_rate = 0.050 # mV/s
starting_potential = -0.4
# generate potential list
potentials = np.round((np.round(np.linspace(0, time_total, time_total),0) * scan_rate) + starting_potential, 2)

# generate color list
colors = plt.cm.Purples(np.linspace(0, 1, len(potentials)))
# colors =colors[len(potentials):]

data = pd.read_csv(workingfile, sep='\t', skiprows=5)
index = 0
while index < len(potentials):
    plt.plot(data.iloc[:,[0]], data.iloc[:,[index+1]], label=(str(potentials[index])+'V'), color=colors[index])
    index += 1

plt.xlim(330, 1000)
plt.xlabel('Wavelength (nm)')
plt.ylabel('Delta Absorbance (Arb. Units)')
plt.legend(loc='best', ncol=4, prop={'size': 6})
plt.show()