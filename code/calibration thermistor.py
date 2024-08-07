import math as math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

beta=2370.84
t0=298
r0=10
betaC = 3124.14
rC = 8127.82
a = 0.05553260432/1000
b = 3.961211323/10000
c = -3.703921147/10000000
def steinhart(R):
    sth = a + b * math.log(R*1000) + c * math.pow(math.log(R*1000), 3)
    return (1/sth-273)

def fx(R):
    return (1/t0)+(math.log(R*1000/rC)/betaC)

df=pd.read_excel(r"D:\Python\Battery charger\data\Thermistor calibration.xlsx")
print(df.head())
R= pd.to_numeric(df.iloc[52:67, 1])
print(R.size)
#Tout = pd.to_numeric(df.iloc [35:49, 2])
ADC_Rd = pd.to_numeric(df.iloc [52:67, 2])
ADC_Rd = np.delete(ADC_Rd,0)
R = np.delete(R, 0)
print(R)
print(ADC_Rd)

temp = []
for i in range(R.size):
    cal=fx(R[i])
    temp.append(1/cal-273)

print(temp)

temp = np.array(temp)

plt.figure()
plt.plot(ADC_Rd, temp, marker="o")
plt.annotate('Breakpoint', xy=(3511, 40.2), xytext=(2500, 60),arrowprops=dict(facecolor='black', shrink=0.05),)
plt.xlabel('ADC Reading')
plt.ylabel('Temperature (°C)')
plt.title('ADC Reading vs Temperature calculated')
plt.grid(True)

#plt.figure()
#plt.plot(ADC_Rd, R, marker="o")
#plt.xlabel('ADC Reading')
#plt.ylabel('Resistance (Ohm)')
#plt.title('ADC Reading vs Resistance')
#plt.grid(True)

#plt.figure()
#plt.plot(temp, R, marker="o")
#plt.ylabel('Resistance (Ohm)')
#plt.xlabel('Temperature (°C)')
#plt.title('Resistance vs Temperature')
#plt.text(64, 8.46, r'$T = ( \frac{1}{T_0} + \frac{log( \frac{R_T}{R_0} )}{\beta}\ )^{-1} $', fontsize=16)
#plt.grid(True)

plt.figure()
fit_adc = ADC_Rd[2:12]
fit_temp = temp[2:12]
m,b = np.polyfit(fit_adc, fit_temp, 1)
print(m)
print(b)
lbl = "y=%fx+%f"%(m,b)
plt.plot(fit_adc, fit_temp, marker="o")
plt.plot(fit_adc, fit_adc*m+b, color='red', label=lbl)
plt.xlabel('ADC Reading')
plt.ylabel('Temperature (°C)')
plt.title('Line fitting the linear region of ADC vs Temperature')
plt.legend()
plt.grid(True)
plt.show()
adc = np.arange(0,4095, 100, dtype= int)
fitI = 0.0068009075524013895*adc + 13.026086906503549
fitR = m * adc + b

f3 = plt.figure()
plt.plot(adc, fitI, color = 'red', marker = 'o', label = 'Iinitial calibration')
plt. plot(adc, fitR, marker = '^', label = 'Recalibration')
plt.xlabel('ADC Reading')
plt.ylabel('Temperature (°C)')
plt.legend()

diff = fitI - fitR

av_in = np.mean(diff)
max = np.max(diff)
min = np.min(diff)
med = np.median(diff)

countn = 0
countp = 0
for i in range(diff.size):
    if diff[i] < 0:
        countn += 1
    else:
        countp += 1 

print(countn)
print(countp)
print(countn/diff.size)
print(countp/diff.size)
print(av_in)
print(max)
print(med)
print(min)
print(adc)
f4= plt.figure()
#plt.title('Box plot of difference between line fit of initial and recalibrated to 0-2.6A')
plt.title('Chaging current')
plt.boxplot(diff)




