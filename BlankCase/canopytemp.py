import numpy as np
import csv
from matplotlib import pyplot as plt

#Get data
roadsT = np.loadtxt('postProcessing/surfaces/3000/T_roads.raw',dtype='float',delimiter=' ',skiprows=2,usecols=[0,1,3])
roadsU = np.loadtxt('postProcessing/surfaces/3000/U_roads.raw',dtype='float',delimiter=' ',skiprows=2,usecols=[0,1,3,4,5])

grassT = np.loadtxt('postProcessing/surfaces/3000/T_grass.raw',dtype='float',delimiter=' ',skiprows=2,usecols=[0,1,3])
grassU = np.loadtxt('postProcessing/surfaces/3000/U_grass.raw',dtype='float',delimiter=' ',skiprows=2,usecols=[0,1,3,4,5])

#Get validation data
valT = np.loadtxt('./outdata/T17.csv',dtype='float',delimiter=',',skiprows=1,usecols=[1,2])
valU = np.loadtxt('./outdata/U17.csv',dtype='float',delimiter=',',skiprows=1,usecols=[1,2])

roadsTavg = np.mean(roadsT[:,2]-273.15)
roadsTstd = np.std(roadsT[:,2])
grassTavg = np.mean(grassT[:,2]-273.15)
grassTstd = np.std(grassT[:,2])

roadsUavg = np.mean(np.sqrt(np.sum(np.square(roadsU[:,2:4]),axis=1)))
roadsUstd = np.std(np.sqrt(np.sum(np.square(roadsU[:,2:4]),axis=1)))
grassUavg = np.mean(np.sqrt(np.sum(np.square(grassU[:,2:4]),axis=1)))
grassUstd = np.std(np.sqrt(np.sum(np.square(grassU[:,2:4]),axis=1)))

#Print data
print('Temperatures: Roads ',roadsTavg,'+-',roadsTstd,'; Grass ',grassTavg,'+-',grassTstd)
print('Wind speeds: Roads ',roadsUavg,'+-',roadsUstd,'; Grass ',grassUavg,'+-',grassUstd)

#Plot
cases = ['Roads','Grass']
x = np.arange(len(cases))
bar_width = 0.35
plt.figure(facecolor='w')

#Temperature
plt.subplot(1,2,1)
Tavg = [roadsTavg,grassTavg]
Tstd = [roadsTstd,grassTstd]
plt.bar(x,Tavg,yerr=Tstd,width=bar_width,align='center',alpha=0.5,color='gray',error_kw=dict(ecolor='gray', lw=2, capsize=5, capthick=2),label='Simulated')
plt.bar(x+bar_width,valT[0,:],yerr=valT[1,:],width=bar_width,align='center',alpha=0.5,color='blue',error_kw=dict(ecolor='gray', lw=2, capsize=5, capthick=2),label='Measured')
plt.xticks(x+bar_width/2.0,cases)
plt.ylabel('Temperature (C)')
plt.title('(a) Air Temperature at 2 m')

#Wind speed
plt.subplot(1,2,2)
Uavg = [roadsUavg,grassUavg]
Ustd = [roadsUstd,grassUstd]
plt.bar(x,Uavg,yerr=Ustd,width=bar_width,align='center',alpha=0.5,color='gray',error_kw=dict(ecolor='black', lw=2, capsize=5, capthick=2),label='Simulated')
plt.bar(x+bar_width,valU[0,:],yerr=valU[1,:],width=bar_width,align='center',alpha=0.5,color='blue',error_kw=dict(ecolor='black', lw=2, capsize=5, capthick=2),label='Measured')
plt.xticks(x+bar_width/2.0,cases)
plt.ylabel('Wind Speed (m/s)')
plt.title('(a) Wind Speed at 2 m')
plt.legend(loc='upper center')


plt.show()

#Write Data
np.savetxt('./outdata/roadsT.csv', roadsT, delimiter=',')
np.savetxt('./outdata/roadsU.csv', roadsU, delimiter=',')
np.savetxt('./outdata/grassT.csv', grassT, delimiter=',')
np.savetxt('./outdata/grassU.csv', grassU, delimiter=',')
