import numpy as np

#fit all data with quadratic function and save output as c2, c1, c0
c2, c1, c0 = np.polyfit(z, d, deg=2) #degree=1 is linear; 2 is quadratic
print(c2, c1, c0)