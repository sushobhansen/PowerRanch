import numpy as np
from matplotlib import pyplot as plt

#Get data
roadsT = np.loadtxt('./postProcessing/surfaces/3000/T_roads.raw',dtype='float',delimiter=' ',skiprows=2,usecols=[3])
roadsUcomps = np.loadtxt('./postProcessing/surfaces/3000/U_roads.raw',dtype='float',delimiter=' ',skiprows=2,usecols=[3,4,5])
roadsU = np.sqrt(np.sum(np.square(roadsUcomps),axis=1))

grassT = np.loadtxt('./postProcessing/surfaces/3000/T_grass.raw',dtype='float',delimiter=' ',skiprows=2,usecols=[3])
grassUcomps = np.loadtxt('./postProcessing/surfaces/3000/U_grass.raw',dtype='float',delimiter=' ',skiprows=2,usecols=[3,4,5])
grassU = np.sqrt(np.sum(np.square(grassUcomps),axis=1))

#Get validation data. Use genfromtxt instead of loadtxt to handle missing values (set to NaN)
val = np.genfromtxt('./outdata/val17.csv',dtype='float',delimiter=',',skip_header=1,filling_values=np.nan) #RoadsT,GrassT,RoadsU,GrassU

#Aggregate data
dataT = {}
dataU = {}

dataT['Roads'] = {}
dataT['Grass'] = {}
dataT['Roads']['Measured'] = val[~np.isnan(val[:,0]),0]
dataT['Roads']['Simulated'] = roadsT-273.15
dataT['Grass']['Measured'] = val[~np.isnan(val[:,1]),1]
dataT['Grass']['Simulated'] = grassT-273.15

dataU['Roads'] = {}
dataU['Grass'] = {}
dataU['Roads']['Measured'] = val[~np.isnan(val[:,2]),2]
dataU['Roads']['Simulated'] = roadsU
dataU['Grass']['Measured'] = val[~np.isnan(val[:,3]),3]
dataU['Grass']['Simulated'] = grassU

#Plot data

fig, axes = plt.subplots(2,2,figsize=(10,10))
#Plot roads temperature
axes[0,0].boxplot([dataT['Roads'][item] for item in ['Measured','Simulated']],widths=0.5,notch=True,showmeans=True)
axes[0,0].set(xticklabels=['Measured','Simulated'],ylabel='Temperature (C)',title='(a) Roads',ylim=(40,45))
#Plot grass temperature
axes[0,1].boxplot([dataT['Grass'][item] for item in ['Measured','Simulated']],widths=0.5,notch=True,showmeans=True)
axes[0,1].set(xticklabels=['Measured','Simulated'],ylabel='Temperature (C)',title='(b) Grass',ylim=(40,45))
#Plot roads wind speed
axes[1,0].boxplot([dataU['Roads'][item] for item in ['Measured','Simulated']],widths=0.5,notch=True,showmeans=True)
axes[1,0].set(xticklabels=['Measured','Simulated'],ylabel='Wind Speed (m/s)',title='(c) Roads',ylim=(-1,8))
#Plot grass windspeed
axes[1,1].boxplot([dataU['Grass'][item] for item in ['Measured','Simulated']],widths=0.5,notch=True,showmeans=True)
axes[1,1].set(xticklabels=['Measured','Simulated'],ylabel='Wind Speed (m/s)',title='(d) Grass',ylim=(-1,8))
plt.show()
