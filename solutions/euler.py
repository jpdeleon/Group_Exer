from math import sin
from numpy import arange
from matplotlib import pyplot as plt

def f(x,t):
    return (t**5/5.0)-t**2+t

a = 0.0           # Start of the interval
b = 2.0           # End of the interval
N = 1000          # Number of steps
h = (b-a)/N       # Size of a single step
x = 0.0           # Initial condition

tpoints = arange(a,b,h)
xpoints = []
for t in tpoints:
    xpoints.append(x)
    x += h*f(x,t)

plt.plot(tpoints,tpoints**4-2*tpoints+1,label='orig. func.')
plt.plot(tpoints,xpoints,label='derivative')
plt.xlabel("t")
plt.ylabel("x(t)")
plt.legend(loc='best')
plt.show()
