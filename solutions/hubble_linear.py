#n is nth row of data; try any value between n=0 and 100 to get z<0.1 in the plot
n=60

#plot upto nth data point only
plt.errorbar(x=z[:n], y=d[:n], yerr=err[:n], marker='o', linestyle='none')
#add labels
plt.ylabel('Distance (Mpc)')
plt.xlabel('Redshift')