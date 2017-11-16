#plot with error bars usng plt.errorbar
plt.errorbar(x=z, y=d, yerr=err, marker='o', linestyle='none')
#add labels, take note of the units
plt.ylabel('Distance (Mpc)')
plt.xlabel('Redshift')
plt.title('Supernova measurements')