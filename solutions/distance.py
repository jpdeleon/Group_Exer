#import trigo functions from math library and abbreviate as m
import math as m

print("Input coordinates of two points:")
slat = m.radians(float(input("Starting latitude: ")))
slon = m.radians(float(input("Ending longitude: ")))
elat = m.radians(float(input("Starting latitude: ")))
elon = m.radians(float(input("Ending longitude: ")))

#calculate distance using variable `dist`
dist = 6371.01 * m.acos(sin(slat)*m.sin(elat) + m.cos(slat)*m.cos(elat)*m.cos(slon - elon))
print("The distance is %.2fkm." % dist)