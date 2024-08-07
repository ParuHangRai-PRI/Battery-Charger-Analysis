import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv(r'D:\Python\Battery charger\data\Charging data\DATA_RD19.txt', delimiter= ',')
print('\n')

tim = pd.to_datetime(df["TIME(hr:min:sec)"])
counter = np.arange(2, tim.size+1, 1)

inputI = df["INPUT_I(A)"]
chargI = df["CHARGING_I(A)"]
c1 = df['Cell1(V)']
c2 = df['Cell2(V)']
c3 = df['V_+(V)']
tempr = df['TEMPERATURE(deg C)']

av2 = c2.mean()
chargI = np.delete(chargI, 0)
c1 = np.delete(c1, 0)
c2 = np.delete(c2, 0)
c3 = np.delete(c3, 0)
tempr = np.delete(tempr, 0)
print(tempr.size)
for i  in range(1,c2.size):
	if c2[i] < 3.6:
		c2[i] = av2 


ct3 = c3 - c2 
c2 = c2 - c1

av1 = c1.mean();
av2 = c2.mean();
av3 = ct3.mean();
print(av1)
print(av2)
print(av3)

interval = 20 * 60  # 1200 seconds

fig1, ax1 = plt.subplots()
plt.title('Charging Time vs Voltages', fontsize = 20)
ax1.plot(counter, c1, label = 'B1 Voltage')

ax1.plot(counter, c2, color = 'tab:olive', label = 'B2 Voltage')

ax1.plot(counter, ct3, color = 'grey', label = 'P+ Voltage')

ax1.set_xlabel('Time (minutes)', fontsize = 16)
ax1.set_ylabel('Voltage (V)', fontsize = 16 )

ax1.plot(np.arange(0, 8401, interval), np.full(8,  av1), ls = '--', color = 'purple')
ax1.text(4000, av1+0.005, r'B1 = 4.239 V', fontsize=16, color = 'purple')
ax1.plot(np.arange(0, 8401, interval), np.full(8,  av2), ls = '--', color = 'red')
ax1.text(5000, av2+0.005, r'B2 = 4.169 V', fontsize=16, color = 'red')
ax1.plot(np.arange(0, 8401, interval), np.full(8,  av3), ls = '--', color = 'black')
ax1.text(7000, av3+0.005, r'P+ = 4.190 V', fontsize=16, color = 'black')
ax1.set_xticks(np.arange(0, 8401, interval))

# Format the x-axis labels to show time in minutes
ax1.set_xticklabels([(int(x) // 60) for x in np.arange(0, 8401, interval)], fontsize=16)
ax1.set_yticks(np.arange(3.6, 4.8, 0.3))
ax1.set_yticklabels([ x for x in np.arange(3.6, 4.8, 0.3)], fontsize=16)
ax1.legend(loc='lower right', fontsize=16)
ax1.grid(True)

fig2, ax2 = plt.subplots()
plt.title('Charging time vs charging current and voltage', fontsize = 20)

ax2.set_xticks(np.arange(0, 8401, interval))
ax2.set_xticklabels([(int(x) // 60) for x in np.arange(0, 8401, interval)], fontsize=16)
ax2.set_xlabel('Time (minutes)', fontsize = 16)

#ax2.plot(np.full(16, 672), np.arange(0, 16, 1), ls = '--', color = 'black')
ax3 = ax2.twinx()

ax3.set_ylabel('Voltage (V) )', fontsize = 16) 
ax3.plot(counter, c3, label = 'Battery voltage', color = 'orange')
ax3.set_yticks(np.arange(10, 15, 1))
ax3.set_yticklabels([ x for x in np.arange(10, 15, 1)], fontsize=16) 
ax2.set_ylabel('Current (A)', fontsize = 16 )
ax2.plot(counter, chargI, label = 'Charging current')
ax2.plot(np.arange(0, 8401, interval), np.full(8,  2.602), ls = '--', color = 'black')
ax2.text(6000, 2.7, r'I = 2.602 A', fontsize=16)
ax3.plot(np.arange(0, 8401, interval), np.full(8,  12.624), ls = '--', color = 'black')
ax3.text(6000, 12.7, r'V = 12.624 V', fontsize=16)
ax2.plot(np.full(8, 672), np.arange(0, 4, 0.5), ls = '--', color = 'black')
ax2.text(680, 3, r'$t_c = 11.2 min$', fontsize=16)
ax2.set_yticks(np.arange(0, 4, 0.5))
ax2.set_yticklabels([ x for x in np.arange(0, 4, 0.5)], fontsize=16)


ax2.grid(True)
ax2.legend(loc = 'upper left', fontsize = 16)
#ax3.grid(True)
ax3.legend(loc = 'upper right', fontsize = 16)

fig3, ax4 = plt.subplots()
plt.title('Charging time vs battery temperature', fontsize = 20)

ax4.set_xticks(np.arange(0, 8401, interval))
ax4.set_xticklabels([(int(x) // 60) for x in np.arange(0, 8401, interval)], fontsize=16)
ax4.set_xlabel('Time (minutes)', fontsize = 16)

#ax2.plot(np.full(16, 672), np.arange(0, 16, 1), ls = '--', color = 'black')

ax4.set_ylabel('Voltage (V) )', fontsize = 16) 
ax4.plot(counter, tempr)
ax4.set_yticks(np.arange(25, 41, 5))
ax4.set_yticklabels([ x for x in np.arange(25, 41, 5)], fontsize=16) 
ax4.set_ylabel('Temperature (°C)', fontsize = 16 )

#ax2.grid(True)
ax4.grid(True)

plt.show()
avd = chargI[0:673]
print(avd.mean())

avv = c3[672:]
print(avv.mean())