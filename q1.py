import numpy as np
import scipy.stats
import matplotlib.pyplot as plt


# --------------------------------
# PART 1 -------------------------
# --------------------------------

s = 1

M_choices = [1, 4, 16, 32]
large_N = 10000

for M in M_choices:
    vals = np.zeros(large_N)
    for i in range(large_N):
        delta = ((np.random.rand(M) > 0.5) * 2 - 1) * s / np.sqrt(M)
        epsilon = sum(delta)
        vals[i] = epsilon

    smallest_possible = -M * s / np.sqrt(M)
    largest_possible = M * s / np.sqrt(M)
    bins = np.linspace(smallest_possible, largest_possible, M + 2)


    ideal_x = np.linspace(smallest_possible * (1 + 1 / M), largest_possible * (1 + 1 / M), 200)
    ideal_y = scipy.stats.norm.pdf(ideal_x, 0, 1)

    plt.clf()
    plt.hist(vals, bins=bins, density=True)
    plt.plot(ideal_x, ideal_y, color='orange')

    plt.xlabel(r"$\epsilon$")
    plt.ylabel("Probability Density")

    plt.legend("Simulated values", "Normal distribution")
    plt.title(f"Simulated errors, M = {M}")

    plt.savefig(f'Q1_M{M}.png', bbox_inches='tight')



