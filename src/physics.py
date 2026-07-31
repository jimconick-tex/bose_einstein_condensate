import numpy as np


def potential(x):
    """
    Calculate the external potential.
    """
    return x**4 - 2*x**2


def normalize(psi, x):
    """
    Normalize the wave function so that its total
    probability is equal to one.
    """
    density = np.abs(psi)**2
    norm = np.sqrt(np.trapezoid(density, x))

    return psi / norm


def initial_condition(x):
    """
    Generate an initial guess for the wave function
    used to start the imaginary-time evolution.
    """
    psi = np.exp(-x**2)

    return normalize(psi, x)