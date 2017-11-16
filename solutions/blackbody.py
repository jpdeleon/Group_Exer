from matplotlib import pyplot as plt
%matplotlib inline
import numpy as np

#remove raised error = overflow in numpy
np.seterr(all='ignore')
#to reset
#np.seterr(all='warn', over='raise')

h = 6.626e-34
c = 3.0e+8
k = 1.38e-23

def planck(lambda_, T):
    a = 2.0*h*c**2
    b = h*c/(lambda_*k*T)
    return a/ ((lambda_**5) * (np.exp(b) - 1.0))

# generate x-axis in increments from 1nm to 3 micrometer in 1 nm increments
# starting at 1 nm to avoid wav = 0, which would result in division by zero.
wavelengths = np.arange(1e-9, 3e-6, 1e-9) 

# intensity at T=4000K, 5000K, 6000K, 7000K
temperature = [4.0e3,5.0e3,6.0e3,7.0e3]
I = []
for i in temperature:
    ii = planck(wavelengths, i)
    I.append(ii)
    
colors = ['r-', 'g-', 'b-', 'k-']
#pl.hold(True) # doesn't erase plots on subsequent calls of plt.plot()
counter = 0
for j,c in zip(I,colors):
    plt.plot(wavelengths*1e9, j, c, label='T={}K'.format(temperature[counter]))
    counter+=1

plt.ylabel('Intensity (J m$^{-2}$ sr$^{-1}$ Hz$^{-1}$)')
plt.xlabel('$\lambda$ (nm)')
plt.legend()
plt.show()