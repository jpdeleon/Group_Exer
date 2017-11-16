# Define the data
data = set()

count = int(input("Enter the number of data points: "))
for i in range(count):
    x=float(input("X"+str(i+1)+": "))
    y=float(input("Y"+str(i+1)+": "))
    data.add((x,y))

# Find the average x and y
avgx = 0.0
avgy = 0.0
for i in data:
    avgx += i[0]/len(data)
    avgy += i[1]/len(data)

# Find the sums
totalxx = 0
totalxy = 0

for i in data:
    totalxx += (i[0]-avgx)**2
    totalxy += (i[0]-avgx)*(i[1]-avgy)

# Slope/intercept form
m = totalxy/totalxx
b = avgy-m*avgx

print("Best fit line:")
print("y = "+str(m)+"x + "+str(b))

# Prediction by extrapolation
x = float(input("Enter a value to calculate: "))
print("y = "+str(m*x+b))