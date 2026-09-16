import numpy as np
import matplotlib.pyplot as plt

# Initial conditions
N0 = 1000000
half_life = 10

# Decay constant
lam = np.log(2) / half_life

# Time
t = np.linspace(0, 50, 500)

# Radioactive decay
N = N0 * np.exp(-lam * t)

# Display
plt.plot(t, N)
plt.xlabel("Time")
plt.ylabel("Number of Nuclei")
plt.title("Radioactive Decay Simulation")
plt.grid(True)
plt.show()
