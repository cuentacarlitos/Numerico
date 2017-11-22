import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
from scipy.stats import multivariate_normal
from scipy.stats import multivariate_normal
import file as f
class MidpointNormalize(colors.Normalize):
    def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
        self.midpoint = midpoint
        colors.Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        # I'm ignoring masked values and all kinds of edge cases to make a
        # simple example...
        x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
        return np.ma.masked_array(np.interp(value, x, y))
datos = f.read_archive()
array = np.asarray(datos[0].info[0].dias)
dt = np.dtype([('R','u1'), ('G','u1'), ('B','u1'), ('A','u1')])
for x in array:
	x.astype(dt)
fig, ax = plt.subplots(1, 1)
pcm = ax.pcolor(C=array, norm=MidpointNormalize(midpoint=0.), cmap='RdBu_r')
fig.colorbar(pcm, ax=ax, extend='both')