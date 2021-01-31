#Graphs
import matplotlib.pyplot as plt
#Arrays
import numpy as np
#Find peaks
from scipy.signal import find_peaks
#Fancy Text
from matplotlib import rc


#THIS CODE IS JUST TO GET LATEX FONT IN THE GRAPH
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
rc('font',**{'family':'serif','serif':['Computer Modern Roman']})
rc('text', usetex=True)
plt.rcParams.update({'font.size': 10.5})
plt.rcParams['figure.dpi'] = 150


#Where is our data
data_path = "test.csv"
#Look up the numpy documentation for how this function works
#Delimiter = ',' is common as is the command to ignore the first n lines. You will need to change this to get this code to work. Open the csv in notepad or whatever the fuck mac uses and see how many lines to ignore (skip_header= is your friend here)
data2 = np.genfromtxt(data_path, dtype=float , delimiter=None, encoding='utf-8' ,autostrip=True)



#Lets get the first column in array x
x=data2[0:,0]
#Now the same for my y data but 1- this shit beacuse the data is an ir spectrum. IR data goes down but we want it going up to find the peaks ( in  this case troughs)
y=1-data2[0:,1]

#creating an array called peaks containing the results of the function scipy.signal.find_peaks(). Look up the documentation to see what it returns. Note the comma in front of the = as we are definint two variables as the function gives us back two things
peaks, _ = find_peaks(y, height=-94)
#Obvious here
plt.plot(x,y)
#Subtle but important feature. Im only plotting the points in my x data which were peaks.  THIS IS SUPER USEFUL and make sure you understand what Im doing to my arrays x and y
plt.plot(x[peaks], y[peaks], "x")
#print what I just plotted
print([x[peaks], y[peaks])
plt.show()

