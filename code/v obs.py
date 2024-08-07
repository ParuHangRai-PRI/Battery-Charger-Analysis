import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns

df = pd.read_csv(r'D:\Python\Battery charger\data\Charging data\DATA_RD26.txt', delimiter= ',')
df2 = pd.read_csv(r'D:\Python\Battery charger\data\Charging data\DATA_RD25.txt', delimiter= ',')

count = np.arange(df['V_+(V)'].size) 
f1 = plt.figure()
plt.scatter(count,df['V_+(V)'])
plt.scatter(count,df['Cell2(V)'])
plt.scatter(count,df['Cell1(V)'])
plt.scatter(count,df['CHARGING_I(A)'])
plt.scatter(count,df['INPUT_I(A)'])
plt.scatter(count,df['BUCK_I(V)'])
plt.scatter(count,df['TEMPERATURE(deg C)'])
plt.grid(True)

count = np.arange(df2['V_+(V)'].size) 
f2 = plt.figure()
plt.scatter(count,df2['V_+(V)'])
plt.scatter(count,df2['Cell2(V)'])
plt.scatter(count,df2['Cell1(V)'])
plt.grid(True)
plt.show()