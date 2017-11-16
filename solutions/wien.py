def Wien(T):
    return 2.8977729e-3/T #m/K

lambda_max= []
for i in temperature:
    j = Wien(i)
    lambda_max.append(j)
    print('{:.2f} nm'.format(j*1e9))
#print('{}'.format(lambda_max*1e6))