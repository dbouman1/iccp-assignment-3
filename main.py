# ICCP assignment 3
from QD.dynamics import CrankNicolson

# Parameters
a = 0.5        # Spatial resolution
L = 50        # Square box size
sigma_x = 2.5   # Wavefunction shape x-direction
sigma_y = 2.5   # Wavefunction shape y-direction
mu_x = 25        # Wavefunction position x-direction
mu_y = 5       # Wavefunction position y-direction
k_x = 0     # Wave vector x-direction
k_y = 500     # Wave vector y-direction

# Time evolution
tau = 1
duration = 100

particle = CrankNicolson(a,L,sigma_x,sigma_y,k_x,k_y,mu_x,mu_y)     # Initialize particle
particle.normalize_wavefunction()      # normalize wavefunction so that probability sums up to unity
particle.potential("double slit",25,100,1,5)          # Initialize potential
particle.timeEvolution(tau,duration)             # Start time evolution of particle
particle.plot2D("animate")
# particle1.plot()
