import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_excel(r"D:\Python\Battery charger\data\Battery charge current mes.xlsx")

#print(data)

v_buck=pd.to_numeric(data.iloc[:14,1])
i_buck=pd.to_numeric(data.iloc[:14,2])
i_charg=pd.to_numeric(data.iloc[:14,3])
i_input=pd.to_numeric(data.iloc[:14,4])


v_buck_i=pd.to_numeric(data.iloc[16:31,1])
i_buck_i=pd.to_numeric(data.iloc[16:31,2])
i_charg_i=pd.to_numeric(data.iloc[16:31,3])
i_input_i=pd.to_numeric(data.iloc[16:31,4])

v_buck_ii=pd.to_numeric(data.iloc[16:36,8])
i_buck_ii=pd.to_numeric(data.iloc[16:36,9])
i_charg_ii=pd.to_numeric(data.iloc[16:36,10])
i_input_ii=pd.to_numeric(data.iloc[16:36,11])

#print(i_input_ii)

f1 = plt.figure()
plt.subplot(121)
m,b=np.polyfit(i_charg,i_buck,1)
lbl = "y=%fx+%f"%(m,b)
plt.scatter(i_charg,i_buck)
plt.ylabel("Current measured (A)")
plt.xlabel("ADC read of CHARGE_CURRENT_SIG")
plt.plot(i_charg, m*i_charg+ b,color='red', label=lbl)
plt.legend()
plt.grid(True)

plt.subplot(122)
m1,b1=np.polyfit(i_input,i_buck,1)
lbl1 = "y=%fx+%f"%(m1,b1)
plt.scatter(i_input,i_buck)
plt.ylabel("Current measured (A)")
plt.xlabel("ADC read of INPUT_CURRENT_SIG")
plt.plot(i_input, m1*i_input+ b1,color='red', label= lbl1)
plt.legend()
plt.grid(True)

f2 = plt.figure()
plt.subplot(121)
m2,b2=np.polyfit(i_charg_i,i_buck_i,1)
lbl2 = "y=%fx%f"%(m2,b2)
plt.scatter(i_charg_i,i_buck_i)
plt.ylabel("Current measured (A)")
plt.xlabel("ADC read of CHARGE_CURRENT_SIG")
plt.plot(i_charg_i, m2*i_charg_i+ b2,color='red', label=lbl2)
plt.legend()
plt.grid(True)

plt.subplot(122)
m3,b3=np.polyfit(i_input_i,i_buck_i,1)
lbl3 = "y=%fx+%f"%(m3,b3)
plt.scatter(i_input_i,i_buck_i)
plt.ylabel("Current measured (A)")
plt.xlabel("ADC read of INPUT_CURRENT_SIG")
plt.plot(i_input_i, m3*i_input_i+ b3,color='red', label=lbl3)
plt.legend()
plt.grid(True)

f3 = plt.figure()
plt.subplot(121)
m4,b4=np.polyfit(i_charg_ii,i_buck_ii,1)
lbl4 = "y=%fx+%f"%(m4,b4)
plt.scatter(i_charg_ii,i_buck_ii)
plt.ylabel("Current measured (A)")
plt.xlabel("ADC read of CHARGE_CURRENT_SIG")
plt.plot(i_charg_ii, m4*i_charg_ii+ b4,color='red', label=lbl4)
plt.legend()
plt.grid(True)

plt.subplot(122)
m5,b5=np.polyfit(i_input_ii,i_buck_ii,1)
lbl5 = "y=%fx+%f"%(m5,b5)
plt.scatter(i_input_ii,i_buck_ii)
plt.ylabel("Current measured (A)")
plt.xlabel("ADC read of INPUT_CURRENT_SIG")
plt.plot(i_input_ii, m5*i_input_ii+ b5,color='red', label=lbl5)
plt.legend()
plt.grid(True)


f3=plt.figure()
adc = np.arange(0,4095, 100, dtype= int)
icalc = adc * m +b
icalc_i = adc * m1 +b1
icalc_ii = adc * m2 +b2
icalc_iii = adc * m3 +b3
icalc_iv = adc * m4 +b4
icalc_v = adc * m5 +b5
plt.title('Line fit comparision')
plt.subplot(121)
plt.plot(adc, icalc, color = 'red',  marker = '^', label = 'inital calibration')
plt.plot(adc, icalc_ii, marker = 'o', label = 'Recalibration with 1A range')
plt.plot(adc, icalc_iv, color = 'green' , marker = 'x', label = 'Recalibration with 2A range')
plt.xlabel('ADC Values')
plt.ylabel('Current calculated (A)')
plt.title('ADC read vs Charging current')
plt.legend()

plt.subplot(122)
plt.plot(adc, icalc_i, color = 'red', marker = '^', label = 'inital calibration')
plt.plot(adc, icalc_iii, marker = 'o', label = 'Recalibration with 1A range')
plt.plot(adc, icalc_v, color = 'green', marker = 'x', label = 'Recalibration with 2A range')
plt.xlabel('ADC Values')
plt.ylabel('Current calculated (A)')
plt.title('ADC read vs Input current')
plt.legend()

d_recal_chg = icalc_iv - icalc
d_recal_in = icalc_v - icalc_i

av_chg = np.mean(d_recal_chg)
max = np.max(d_recal_chg)
min = np.min(d_recal_chg)
med = np.median(d_recal_chg)
print(av_chg)
print(max)
print(med)
print(min)

av_in = np.mean(d_recal_in)
max = np.max(d_recal_in)
min = np.min(d_recal_in)
med = np.median(d_recal_in)
print(av_in)
print(max)
print(med)
print(min)

f4= plt.figure()
#plt.title('Box plot of difference between line fit of initial and recalibrated to 0-2.6A')
plt.subplot(121)
plt.title('Chaging current')
plt.boxplot(d_recal_chg)
plt.subplot(122)
plt.title('Input current')
plt.boxplot(d_recal_in)

plt.show()