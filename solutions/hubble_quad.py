#plot all data points with error
plt.errorbar(x=z, y=d, yerr=err, marker='o', linestyle='none',label='measurements')
plt.ylabel('Distance (Mpc)')
plt.xlabel('Redshift')

#superpose best fit line earlier
n=60
plt.plot(z[:n], best_fit_line, label='best fit: deg=1', color='r', lw=3)

#superpose best fit curve 
best_fit_curve= c2*z**2 + c1*z + c0
plt.plot(z, best_fit_curve, label='best fit: deg=2', color='g', lw=3)
plt.legend(loc='best')