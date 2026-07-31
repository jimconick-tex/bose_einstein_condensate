import numpy as np

from src.grid import create_grid
from src.physics import initial_condition, normalize, potential


def split_step(g, dtau=1e-3, iterations=50_000):
    """
    Compute the ground-state wave function by evolving
    the Gross-Pitaevskii equation in imaginary time
    using the Split-Step Fourier method.
    """
    x, dx, k = create_grid()

    V = potential(x)
    psi = initial_condition(x)

    for _ in range(iterations):
        psi *= np.exp(
            -0.5 * dtau * (V + g * np.abs(psi)**2)
        )

        psi_fourier = np.fft.fft(psi)

        psi_fourier *= np.exp(
            -0.5 * dtau * k**2
        )

        psi = np.fft.ifft(psi_fourier)

        psi *= np.exp(
            -0.5 * dtau * (V + g * np.abs(psi)**2)
        )

        psi = normalize(psi, x)

    return x, psi