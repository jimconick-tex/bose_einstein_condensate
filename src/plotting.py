import numpy as np
import matplotlib.pyplot as plt


def plot_bec_density(x, psi, g, save=False):
    """
    Plot the particle density of the Bose-Einstein condensate.
    """
    fig, ax = plt.subplots(figsize=(7, 4))

    ax.plot(x, np.abs(psi)**2, lw=2)

    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$|\psi(x)|^2$")
    ax.set_title(fr"Ground-state density ($g={g:g}$)")

    # Nice style
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.tick_params(direction="out", length=5, width=1)
    ax.margins(x=0)

    plt.tight_layout()

    if save:
        plt.savefig(
            f"bec_density_g{g:g}.png",
            dpi=300,
            bbox_inches="tight"
        )

    plt.show()