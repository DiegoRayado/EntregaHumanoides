#!/usr/bin/env python

"""\
lipm2d.py: A tiny 2d LIPM simulation with matplotlib animation.

- Partial inspiration (beware some bugs atow): <https://github.com/AtsushiSakai/PythonRobotics/blob/808e98133d57426b1e6fbbc2bdc897a196278d7d/Bipedal/bipedal_planner/bipedal_planner.py>
- Sagital = XZ
- X plotted as matplotlib_x
- Z plotted as matplotlib_y
"""

__author__      = "Juan G Victores"
__copyright__   = "Copyright 2024-present, Planet Earth"

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from time import sleep
import math

MAX_X = 24
HEIGHT = 1.2
G = 9.8
TIME_DELTA = 0.04 # s

fig, ax = plt.subplots()
ln, = ax.plot([], [], marker = 'o')

def init():
    ax.set_xlim(0, MAX_X)
    ax.set_ylim(-0.1, 1.5)
    return ln,

def animate(args):
    return ln,

class Simulator():
    def __init__(self):
        self.zmp_x = [0, 4, 8, 12, 16, 20, 24]
        self.zmp_x_change = [2, 6, 10, 14, 18, 22]
        self.zmp_idx = 0
        self.T_c = math.sqrt(HEIGHT / G)
        self.t_abs = self.t_rel = 0
        # Establecer alguno de estos dos para que arranque:
        self.x_dot_0 = 0.3
        self.x_0_rel = 0

    def __call__(self):
        self.t_rel += TIME_DELTA
        self.t_abs += TIME_DELTA
        
        self.x_t_rel = (self.x_0_rel * math.cosh(self.t_rel / self.T_c)) + self.T_c * self.x_dot_0 * math.sinh(self.t_rel / self.T_c)

        self.x_dot_t = (self.x_0_rel * math.sinh(self.t_rel / self.T_c) / self.T_c) + self.x_dot_0 * math.cosh(self.t_rel / self.T_c) # para conservar tras cambio

        print("t_rel: %1.2f (zmp_x[self.zmp_idx]: %5f), x_t_rel: %5.2f, x_dot_t: %5.2f" % (self.t_rel, self.zmp_x[self.zmp_idx], self.x_t_rel, self.x_dot_t))
        
        ln.set_data([self.zmp_x[self.zmp_idx], self.zmp_x[self.zmp_idx] + self.x_t_rel], [0, HEIGHT])
        # ln.set_data([180, self.currentTimeStep, 0, self.currentTimeStep], [0, HEIGHT, 0, HEIGHT])

        if self.zmp_x[self.zmp_idx] + self.x_t_rel > self.zmp_x_change[self.zmp_idx]:
            self.zmp_idx += 1
            print("zmp_idx", self.zmp_idx)
            self.t_rel = 0 # reseteamos tiempo
            self.x_dot_0 = self.x_dot_t # conservamos velocidad
            self.x_t_rel -= (self.zmp_x[self.zmp_idx] - self.zmp_x[self.zmp_idx-1]) # restamos lo avanzado
            self.x_0_rel = self.x_t_rel

        if self.zmp_x[self.zmp_idx] + self.x_t_rel > MAX_X:
            quit()

        return 1

simulator = Simulator()

def frames():
    while True:
        yield simulator()

ani = FuncAnimation(fig, animate, frames=frames,
                    interval=100, init_func=init,
                    blit=True, save_count=MAX_X)
plt.show()