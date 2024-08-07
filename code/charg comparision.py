import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

alpha = 0.1

def exp_smth(dat, p_cal):
    p_cal = p_cal + alpha*(dat - p_cal)
    return(p_cal)

df1C = pd.read_csv(r'D:\Python\Battery charger\data\Charging data\DATA_RD43.txt')
df0C5 = pd.read_csv(r"D:\Python\Battery charger\data\Charging data\DATA_RD39.txt")
dffh = pd.read_csv(r"D:\Python\Battery charger\data\Charging data\DATA_RD43.txt")
dfsh = pd.read_csv(r"D:\Python\Battery charger\data\Charging data\DATA_RD44.txt")
#print(df0C5.head())
#print(df1C.head())
print(dffh.head())
print(dfsh.head())


row2cpy = 0
for i in range(20):
    if df1C['CHARGING_I(A)'].iloc[i] < 0.01:
        row2cpy = row2cpy + 1

init1C = df1C.loc[0:row2cpy-1]
df1C.drop([0,row2cpy-1], inplace = True)

row2cpy = 0
for i in range(20):
    if df0C5['CHARGING_I(A)'].iloc[i] < 0.01:
        row2cpy = row2cpy + 1
init0C5 = df0C5.loc[0:row2cpy-1]
df0C5.drop([0,row2cpy-1], inplace = True)

row2cpy = 0
for i in range(20):
    if dfsh['CHARGING_I(A)'].iloc[i] < 0.01:
        row2cpy = row2cpy + 1
dfsh.drop([0,row2cpy-1], inplace = True)

row2cpy = 0
for i in range(20):
    if dffh['CHARGING_I(A)'].iloc[i] < 0.01:
        row2cpy = row2cpy + 1
dffh.drop([0,row2cpy-1], inplace = True)

print(dffh.head())
print(dfsh.head())

frames = [dffh, dfsh]
dfquatC = pd.concat(frames)
print(dfquatC[5158:5300])


time1C = np.arange(1, df1C['TIME(hr:min:sec)'].size+1, 1)
time0C5 = np.arange(1, df0C5['TIME(hr:min:sec)'].size+1, 1)
timequatC = np.arange(1, dfquatC['TIME(hr:min:sec)'].size+1, 1)
print(timequatC)

smot_i = []
smot_v = []
smot_tt = []
smot_i.append(df1C['CHARGING_I(A)'].iloc[0])
smot_v.append(df1C['V_+(V)'].iloc[0])
smot_tt.append(df1C['TEMPERATURE(deg C)'].iloc[0])

for i in range(1,df1C['CHARGING_I(A)'].size):
    tm1 = smot_i[i - 1]
    tm1 = exp_smth(df1C['CHARGING_I(A)'].iloc[i], tm1)
    smot_i.append(tm1)

    temp = smot_v[i - 1]
    temp = exp_smth(df1C['V_+(V)'].iloc[i], temp)
    smot_v.append(temp)

    temp = smot_tt[i - 1]
    temp = exp_smth(df1C['TEMPERATURE(deg C)'].iloc[i], temp)
    smot_tt.append(temp)

smot_i = np.array(smot_i)
smot_v = np.array(smot_v)
smot_tt = np.array(smot_tt)

smoth_i = []
smoth_v = []
smoth_i.append(df0C5['CHARGING_I(A)'].iloc[0])
smoth_v.append(df0C5['V_+(V)'].iloc[0])

for i in range(1,df0C5['CHARGING_I(A)'].size):
    tm1 = smoth_i[i - 1]
    tm1 = exp_smth(df0C5['CHARGING_I(A)'].iloc[i], tm1)
    smoth_i.append(tm1)

    temp = smoth_v[i - 1]
    temp = exp_smth(df0C5['V_+(V)'].iloc[i], temp)
    smoth_v.append(temp)

smoth_i = np.array(smoth_i)
smoth_v = np.array(smoth_v)

smotQ_i = []
smotQ_v = []
smotQ_t = []
smotQ_i.append(dfquatC['CHARGING_I(A)'].iloc[0])
smotQ_v.append(dfquatC['V_+(V)'].iloc[0])
smotQ_t.append(dfquatC['TEMPERATURE(deg C)'].iloc[0])

for i in range(1,dfquatC['CHARGING_I(A)'].size):
    tm1 = smotQ_i[i - 1]
    tm1 = exp_smth(dfquatC['CHARGING_I(A)'].iloc[i], tm1)
    smotQ_i.append(tm1)

    temp = smotQ_v[i - 1]
    temp = exp_smth(dfquatC['V_+(V)'].iloc[i], temp)
    smotQ_v.append(temp)

    temp = smotQ_t[i - 1]
    temp = exp_smth(dfquatC['TEMPERATURE(deg C)'].iloc[i], temp)
    smotQ_t.append(temp)

smotQ_i = np.array(smotQ_i)
smotQ_v = np.array(smotQ_v)
smotQ_tt = np.array(smotQ_t)

meanI1C = smot_i[:700].mean()
meanV1C = smot_v[700:].mean()
meanI0C5 = smoth_i[:3530].mean()
meanV0C5 = smoth_v[3550:].mean()
print(meanI0C5)
print(meanI1C)
print(meanV0C5)
print(meanV1C)

fig1 =plt.figure()
c2 = df1C['Cell2(V)']
print(c2)
for i in range(3,time1C.size):
    if c2[i] < 7 :
        c2[i] = c2[i-1]
plt.plot(time1C, c2)

fig, ax = plt.subplots(figsize=(20,12))
p1, = ax.plot(time1C, smot_i, label = 'Charging current at 1C', color = 'blue')
p2, = ax.plot(time0C5, smoth_i, label = 'Charging current at 0.5C', color = 'cyan')
p3, = ax.plot(timequatC, smotQ_i, label = 'Charging current at 0.25C', color = 'purple')
ax.set_xlabel('Time (sec)', fontsize = 16)
ax.set_ylabel('Current (A)', fontsize = 16)
ax.tick_params(axis='both', which='major', labelsize=16)
#ax.set_yticklabels(fontsize = 16)
leg1 = ax.legend(handles = [p1, p2, p3], bbox_to_anchor=(0.94, 1.11), fontsize = 16)
ax.add_artist(leg1)
ax.grid(True)

l1, = ax.plot(time0C5, np.full(time0C5.size, meanI0C5), color = 'red' , ls = '--', label = 'Average 0.5C current = %.3f A'%(meanI0C5))
l2, = ax.plot(time1C, np.full(time1C.size, meanI1C), color = 'black', ls = '--', label = 'Average 1C current = %.3f A'%(meanI1C))
l3, = ax.plot(np.full(26, 700), np.arange(0, 2.6, 0.1), ls = '-.', color = 'black', label = '1C charging time = 700 sec')
l4, = ax.plot(np.full(26, 3550), np.arange(0, 2.6, 0.1), ls = '-.', color = 'red', label = '0.5C charging time = 3500 sec')
ax.legend(handles = [l2, l3, l1, l4], bbox_to_anchor=(0.3, 1.2), title = 'Line values', fontsize = 16)

vax = ax.twinx()
vax.plot(time1C, smot_v, label = 'Battery voltage charging at 1C', color = 'orange')
vax.plot(timequatC, smotQ_v, label = 'Battery voltage charging at 0.25C', color = 'brown')
#vax.plot(time1C, np.full(time1C.size, meanV1C), color = 'black', ls = '--')
vax.set_ylabel('Voltage(V)', fontsize = 16)
vax.tick_params(axis='both', which='major', labelsize=16)
#ax.subplot(122)
vax.plot(time0C5, smoth_v, label = 'Battery voltage charging at 0.5C', color = 'green')
#vax.plot(time0C5, np.full(time0C5.size, meanV05C), color = 'red', ls = '--')
vax.legend(loc='upper right', bbox_to_anchor=(1, 1.2), fontsize = 16)

# Get the current reference
#ax = ax.gca()

# Create a Rectangle patch
#rect = patches.Rectangle((5000,12),3200,0.4,linewidth=1,edgecolor='black',facecolor='none')

# Add the patch to the Axes
#ax.add_patch(rect)


#y = 12.35
#ax.text(5050, y, r'Average 1C current = %.3f A'%meanI1C, fontsize=14, color = 'black')
#y -= 0.1
#ax.text(5050, y, r'Average 0.5C current = %.3f A'%meanI1C, fontsize=14, color = 'black')
#y -= 0.1
#ax.text(5050, y, r'1C charging time = 700 sec', fontsize=14, color = 'black')
#y -= 0.1
#ax.text(5050, y, r'0.5C charging time = 3500 sec', fontsize=14, color = 'black')
plt.show()