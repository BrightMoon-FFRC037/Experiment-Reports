import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_excel('a Larger range.xlsx')
voltage = np.array(data['Voltage'])

voltage_of_source = np.linspace(2.5,5.3,29)
resistor = 1
current = voltage/1
voltage_of_LED = voltage_of_source - voltage
plt.plot(voltage_of_LED ,current)
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.show()