import numpy as np
import matplotlib.pyplot as plt
import math

a = 0.05553260432/1000
b = 3.961211323/10000
c = -3.703921147/10000000
datT = [31, 44, 66]
datR = [6610, 4090, 2290]
beta = 2370.4
betaC = 3124.14
rC = 8127.82
r0=10000
t0=298
r = np.array([2540,
4610,
6930,
7410,
8120,
8870,
9530,
10430,
11220,
12020,
12770,
14450,
16900,
20000,
20800])
adc = np.array([3824,
3802,
3696,
3450,
3012,
2550,
2142,
1596,
1116,
624,
174,
53,
51,
51,
51])
def steinhart(R):
    sth = a + b * math.log(R) + c * math.pow(math.log(R), 3)
    return (1/sth-273)

def betafun(R,r0, bta):
    val = (1/t0)+(math.log(R/r0)/bta)
    return (1/val-273)
def betafit(R,T):
    bta = math.log(R/r0)/((1/T)-(1/t0))
    return(bta)

tempr = []
for i in range(r.size):
    temp = steinhart(r[i])
    tempr.append(temp)

print(tempr)
res = np.arange(200, 10000, 200)
rest = np.arange(1200, 10000, 200)

stv = []
betav = []
betan = []

for i in range(res.size):
    temp = steinhart(res[i])
    stv.append(temp)

for i in range(res.size):    
    temp = betafun(res[i], r0, beta)
    betav.append(temp)  

for i in range(res.size):    
    temp = betafun(res[i], rC, betaC)
    betan.append(temp) 

plt.plot(stv, res, label = 'S-H model')
plt.scatter(datT, datR)
lbl = r'${\beta}\ $ model'
plt.plot(betav, res, label = lbl)
lbl = r'${\beta}\ $calc model '
plt.plot(betan, res, label = lbl)
plt.xlabel('Temperature (deg C)')
plt.ylabel('Resistance (ohm)')
plt.grid(True)
plt.legend()

f2= plt.figure()
m, b = np.polyfit(adc[4:12], tempr[4:12],1)
lbl = "y=%fx+%f"%(m,b)
plt.plot(adc, m*adc + b, label = lbl, color = 'red')
plt.scatter(adc, tempr)
plt.ylabel('Temperature (deg C)')
plt.xlabel('ADC read')
plt.legend()
plt.show()
