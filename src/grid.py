import numpy as np
def create_grid(N=1024, x_min=-7, x_max=7):
    """
    Create the spatial grid and its corresponding Fourier-space grid
    used by the Split-Step method.
    """
    # Real Space Grid
    x = np.linspace(x_min, x_max, N)
    dx = x[1]-x[0]
    #Fourier Space Grid
    k = 2*np.pi * np.fft.fftfreq(N, d=dx)
    return x,dx,k