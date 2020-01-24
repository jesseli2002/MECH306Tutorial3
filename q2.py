import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
from uncertainties import ufloat

# part a) --------------------------
L = ufloat(0.7, 0.014)
h = ufloat(0.03, 0.003)
b = ufloat(0.04, 0.0004)
F = ufloat(80, 0.8)
delta = ufloat(0.008, 0.00008)

I = b * h ** 3 / 12
E = F * L ** 3 / (3 * delta * I)
E /= 1E9 #present in GPa
print("E analytic: ", E)


# part b) ----------------------------------
L_base = 0.7
h_base = 0.03
b_base = 0.04
F_base = 80
delta_base = 0.008


E_x = np.linspace(E.n - 4 * E.s, E.n + 4 * E.s, num=200)
E_y = scipy.stats.norm.pdf(E_x, E.n, E.s)
plt.plot(E_x, E_y, color='orange')


N = 10000
E_results = np.zeros(N)
for i in range(N):
    rand_nums = np.random.standard_normal(5)

    L = L_base + rand_nums[0] * 0.014
    h = h_base + rand_nums[1] * 0.003
    b = b_base + rand_nums[2] * 0.0004
    F = F_base + rand_nums[3] * 0.8
    delta = delta_base + rand_nums[4] * 0.00008

    I = b * h ** 3 / 12
    E_results[i] = F * L ** 3 / (3 * delta * I)

E_results /= 1E9 #present in GPA
plt.hist(E_results, bins=30, density=True)

plt.xlabel("E (GPa)")
plt.ylabel(r"Probability density (GPa$ ^{-1}$)")
plt.title("PDF for E, determined analytically and by Monte Carlo simulation")

plt.savefig(f'Q2.png', bbox_inches='tight')
plt.show()
