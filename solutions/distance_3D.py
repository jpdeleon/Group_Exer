import math
# Input 2 arbitrary points (with 3 components)
x = (1, 2, 3)
y = (3, 2, 1)

#enumerate values of x, y using dummy variables a,b
#first define an empty variable partial_sum
partial_sum = []

#loop for each a, b
for a, b in zip(x, y):
    #compute square of their difference and call it pair
    pair = (a - b) ** 2
    #add the result of pair to partial_sum using .append()
    partial_sum.append(pair)

#partial_sum contains 3 numbers, print them
print(partial_sum)

#finally sum the partial_sum and compute its sqrt; call it distance
distance = math.sqrt(sum(partial_sum))
#print result
print("Euclidean distance from x to y: ",distance)

'''
#Note that the entire program above can be condensed into:
import math
x = (1, 2, 3)
y = (3, 2, 1)

distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
print("Euclidean distance from x to y: ", distance)
'''