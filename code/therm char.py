import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv(r'D:\Python\Battery charger\data\Therm amp ckt.txt', delimiter= ',')
print(df.head())

df2 = pd.read_csv(r'D:\Python\Battery charger\data\Therm amp ckt therm.txt', delimiter= ',')
print(df2.head())

df3 = pd.read_csv(r'D:\Python\Battery charger\data\Therm amp ckt corr2.txt', delimiter= ',')

f1 = plt.figure()
plt.plot(df['r'], df['V(n004)'], label = 'V out of op-amp part 1')
plt.plot(df['r'], df['V(n006)'], label = 'V out of op-amp part 2')
plt.plot(df['r'], df['V(n007)'], label = 'Chopped output')
plt.xlabel('Resistance of potentiometer (Ohm)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.grid(True)

f2 = plt.figure()
plt.subplot(121)
plt.plot(df2['temperature'], df2['V(n004)'], label = 'V out of op-amp part 1')
plt.plot(df2['temperature'], df2['V(n006)'], label = 'V out of op-amp part 2')
plt.plot(df2['temperature'], df2['V(n007)'], label = 'Chopped output')
plt.xlabel('Temperature (deg C)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.legend()

plt.subplot(122)
temp = df3.iloc[3:22,0]
print(temp)
volt = df3.iloc[3:22,2]
m,b = np.polyfit(temp, volt, 1)
lbl = "y=%fx+%f"%(m,b)
plt.scatter(df3['temperature'], df3['V(n005)'], label = 'V out of op-amp part 2')
plt.scatter(df3['temperature'], df3['V(n006)'], label = 'Chopped output')
plt.plot(temp, m*temp+b, color = 'red', label = lbl)
plt.xlabel('Temperature (deg C)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.grid(True)

plt.show()

