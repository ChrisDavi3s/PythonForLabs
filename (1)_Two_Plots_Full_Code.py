import matplotlib.pyplot as plt
#import csv
#import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks
from scipy.signal import argrelextrema
import peakutils
from BaselineRemoval import BaselineRemoval



from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
rc('font',**{'family':'serif','serif':['Computer Modern Roman']})
rc('text', usetex=True)
plt.rcParams.update({'font.size': 10.5})

plt.rcParams['figure.dpi'] = 150


'get the Measured ir spectrum into good shape'
data_path_ir_g = "11 dichloro ethene IR.txt"
data_ir_g = np.genfromtxt(data_path_ir_g, dtype=float , delimiter=None, encoding='utf-8' ,autostrip=True , skip_header=21)
const_ir_trans = 0.01  #constant for scaling transmittance
const_ir_x = 0.95
x_ir_g=data_ir_g[0:,0] * const_ir_x
y_ir_g=np.exp(-data_ir_g[0:,1]*const_ir_trans)

'fit the gauss view ir spectrum'
data_path_ir = "gem_dce_ir.csv"
data_ir = np.genfromtxt(data_path_ir, dtype=float , delimiter=',', encoding='utf-8' ,autostrip=True , skip_header=2)
x_ir=data_ir[0:,0]
input_array_ir = 1-data_ir[0:,1]
baseObj_ir=BaselineRemoval(input_array_ir)
y_ir=((1-baseObj_ir.ZhangFit())/100) + 1

'plot the gauss raman spectrum'
data_path_ra_g = "11 dichloro raman.txt"
data_ra_g = np.genfromtxt(data_path_ra_g, dtype=float , delimiter=None, encoding='utf-8' ,autostrip=True , skip_header=21)
const_ra_trans = 700  #constant for scaling transmittance
const_ra_x = 0.95
x_ra_g=data_ir_g[0:,0] * const_ir_x
y_ra_g=(data_ra_g[0:,1]*const_ra_trans)


'fit the measured view ra spectrum'
data_path_ra = "dce_isomer_C_raman.csv"
data_ra = np.genfromtxt(data_path_ra, dtype=float , delimiter=',', encoding='utf-8' ,autostrip=True , skip_header=2)
x_ra=(data_ra[0:,0] - 0.28)
y_ra=(data_ra[0:,1] - 100) 
















#y_ir_g=(data_ir_g[0:,1] / 100)




#peaks, _ = find_peaks(y, height=-94)







fig, ax1 = plt.subplots()


ax1.set_xlabel('time (s)')
ax1.set_ylabel('exp')
ax1.plot(x_ir,y_ir, color = 'black', linewidth = 0.9)
ax1.plot(x_ir_g,y_ir_g, linestyle = ':', color = 'red', linewidth = 1)
ax1.tick_params(axis='y')
ax1.set_ylim([-0.8,1.2])

ax = plt.gca()  
yticks = ax.yaxis.get_major_ticks()
yticks[0].set_visible(False)
yticks[1].set_visible(False)
yticks[2].set_visible(False)
#yticks[3].set_visible(False)
















ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

ax2.set_ylabel('sin', )  # we already handled the x-label with ax1
ax2.tick_params(axis='y',)
ax2.set_ylim([-100,4000])
ax2.plot(x_ra,y_ra, color = 'black', linewidth = 0.9)
ax2.plot(x_ra_g,y_ra_g, linestyle = ':', color = 'red', linewidth = 1)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()


#plt.plot(x[peaks], y[peaks], "x")
#print([x[peaks], y[peaks])
plt.show()

