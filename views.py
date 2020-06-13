from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from ipywidgets import widgets
from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib nbagg


def update_plot(request):
                amp = widgets.FloatSlider(min=1, max=1000, value=1, description='AMPLITUDE')
                phase = widgets.FloatSlider(min=0, max=5, value=0, description='PHASE')
                fre = widgets.FloatSlider(min=1, max=10, value=1, description='FREQUENCY')
                widgets.interactive(amp=amp, phase=phase, fre=fre)
                x = np.linspace(0, 2, 1000)
                fig, ax = plt.subplots(1, figsize=(10, 4))
                plt.suptitle('SINE WAVE')
                ax.clear()
                units = 'amp={} $(psi)$\nphase={} $(s)$\nfre={} $(Hz)$'
                y = amp * np.sin(2 * np.pi * (fre * x + phase))
                ax.plot(x, y, label=units.format(amp, phase, fre))
                ax.legend(loc=1)
                ax.set_xlabel('S')
                ax.set_ylabel('psi')
                w=plt.show()
                return render(request,'DEMOAPP/projecT.html',{'result':w})