import numpy as np
import matplotlib.pyplot as plt

# plate size, mm
w = h = 10.0
# intervals in x-, y- directions, mm
dx = dy = 0.1
# Thermal diffusivity of steel, mm2.s-1
D = 110.0

Tcool, Thot = 300, 700

nx, ny = int(w / dx), int(h / dy)

dx2, dy2 = dx * dx, dy * dy
dt = dx2 * dy2 / (2 * D * (dx2 + dy2))

u0 = Tcool * np.ones((nx, ny))
u = u0.copy()

u0[-1, :] = Thot

"""
Testing
"""


def do_timestep(u0, u):
    # Propagate with forward-difference in time, central-difference in space
    u[1:-1, 1:-1] = u0[1:-1, 1:-1] + D * dt * (
        (u0[2:, 1:-1] - 2 * u0[1:-1, 1:-1] + u0[:-2, 1:-1]) / dx2
        + (u0[1:-1, 2:] - 2 * u0[1:-1, 1:-1] + u0[1:-1, :-2]) / dy2
    )
    u[-1, :] = Thot
    u0 = u.copy()
    return u0, u


# Number of timesteps
nsteps = 10000
for m in range(nsteps):
    u0, u = do_timestep(u0, u)

np.save("diffusion.npy", u)
