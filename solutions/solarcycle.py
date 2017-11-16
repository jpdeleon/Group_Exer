#import plt and np
from matplotlib import pyplot as plt
import numpy as np

#load file located in data/sunspots.txt and call it `data` with float data type
data = np.loadtxt('data/sunspots.txt', dtype= float)

#assign first column as t
t = data[:,0]

#convert t into month that starts from Jan, 1749; use timedelta library
import datetime as dt

start = dt.date(1749, 1, 1)
month = []

#this for loop converts the first column into proper dates
for i in t:
    time = dt.timedelta(i)
    month.append(start + dt.timedelta(i*365/12))

#assign second column as count
count = data[:,1]

#plot up to first 1000 data points as instructed
plt.plot(month[:1000],count[:1000], 'b-') #b- means blue line

#add labels
plt.xlabel("Time")
plt.ylabel("Sunspot Counts")

#optional: add grid
plt.grid(True)

#show plot
plt.show()