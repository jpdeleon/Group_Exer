R = 1.097e-2
for m in range(1,4):
    print("Series for m =",m)
    for n in range(m+1,m+6):
        invlambda = R*(1.0/m**2-1.0/n**2)
        print("  ",1.0/invlambda," nm")
