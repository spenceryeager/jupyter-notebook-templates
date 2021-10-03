import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

workingfile = ENTER FILE
data = pd.read_csv(workingfile, skiprows=ENTER NUMBER)
plt.plot(data['Potential/V'], data[' Current/A'], color='red')
plt.ylabel("Current (A)")
plt.xlabel('Potential (V)')
plt.show()