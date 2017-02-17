from __future__ import print_function
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

h = 6.626e-34
c = 3.0e+8
k = 1.38e-23

def Wien(T):
    return 2.8977729e-3/T #m/K

def plotBB(temp):
    fig, ax = pl.subplots(1,1)#1, figsize=(10,5))
    ax.set_xlabel('$\lambda$ (nm)')
    ax.set_ylabel('Intensity (J . m$^{-2}$ sr$^{-1}$ Hz$^{-1}$)')
    ax.set_xlim(0,3000)
    ax.set_ylim(0,8e13)
    ax.set_title('Blackbody curve of a star')
    ax.plot(wavelengths*1e9, planck(wavelengths, temp), label='T={}K'.format(temp))
    wav_peak=Wien(temp)
    I_peak=planck(Wien(temp), temp)
    ax.vlines(x=wav_peak*1e9, ymin=0, ymax=I_peak, color='k', linestyles='dotted')
    ax.text(wav_peak, I_peak, r'$\lambda$={:.0f} nm'.format(wav_peak*1e9), fontsize=10, horizontalalignment='left')
    pl.legend()
    pl.show()
interact(plotBB, temp=(5000,7000,100)); #f corresponds to the temperature