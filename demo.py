from numpy import *
import matplotlib.pyplot as plt


random.rand(2, 4)
N = 1000
M = 100

Z = zeros(N)

for i in range(N):
    Xj = (random.rand(M) > 0.5) * 2 - 1
    Z[i] = sum(Xj)

n_bins = 20
plt.hist(Z, n_bins, density=True)
plt.show()
