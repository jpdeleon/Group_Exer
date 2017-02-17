def fit(x,y):
    # Find the average x and y
    avgx = 0.0
    avgy = 0.0
    for i,j in zip(x,y):
        avgx += i/len(x)
        avgy += j/len(y)

    # Find the sums
    totalxx = 0.0
    totalxy = 0.0

    for i,j in zip(x,y):
        totalxx += (i-avgx)**2
        totalxy += (i-avgx)*(j-avgy)

    # Slope/intercept form
    m = totalxy/totalxx
    b = avgy-m*avgx
    
    print("y = "+str(m)+" x + "+str(b))
    
    return m, b