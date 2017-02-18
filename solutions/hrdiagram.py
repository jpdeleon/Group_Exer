import matplotlib.pyplot as plt
import numpy as np

#load file and call it `data` in float data type
data = np.loadtxt("data/stars.txt", dtype=float)
#assign first column as x and second column as y
x = data[:,0]
y = data[:,1]

#scatter plot and set data point transparency alpha=0.5
plt.scatter(x,y, alpha=0.5)
#add appropriate labels
plt.xlabel("Temperature (K)")
plt.ylabel("Magnitude")
plt.xlim(0,13000)
plt.ylim(-5,20)
#optional: add grid
plt.grid()
plt.show()