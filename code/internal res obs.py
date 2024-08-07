import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns

alpha = 0.1

def exp_smth(dat, p_cal):
    p_cal = p_cal + alpha*(dat - p_cal)
    return(p_cal)

df = pd.read_csv(r'D:\Python\Battery charger\data\Charging data\DATA_RD19.txt', delimiter= ',')

tempr = df['TEMPERATURE(deg C)'] 
v = df['V_+(V)']
tempr = np.delete(tempr, 0)
v = np.delete(v, 0)
counter = np.arange(1, tempr.size +1, 1)
print(counter.size)
smot_t = []
smot_v = []
smot_t.append(tempr[0])
smot_v.append(v[0])

for i in range(1,counter.size):
    tm1 = smot_t[i - 1]
    smot_t.append(exp_smth(tempr[i], tm1))

    temp = smot_v[i - 1]
    temp = exp_smth(v[i], temp)
    smot_v.append(temp)

smot_t = np.array(smot_t)
smot_v = np.array(smot_v)

print(smot_t.size)
plt.plot(counter, smot_t)

b = plt.twinx()
b.plot(counter, smot_v, color = 'orange')

plt.xlabel('Time(s)')
plt.show()


