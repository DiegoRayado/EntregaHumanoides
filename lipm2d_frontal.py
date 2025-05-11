  #!/usr/bin/env python

"""\
lipm2d.py: A tiny 2d LIPM simulation with matplotlib animation.

- Partial inspiration (beware some bugs atow): <https://github.com/AtsushiSakai/PythonRobotics/blob/808e98133d57426b1e6fbbc2bdc897a196278d7d/Bipedal/bipedal_planner/bipedal_planner.py>
- Frontal = YZ
- Y plotted as matplotlib_x
- Z plotted as matplotlib_y
"""

__author__      = "Juan G Victores"
__copyright__   = "Copyright 2024-present, Planet Earth"

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from time import sleep
import math

MAX_TIME = 50
HEIGHT = 1.2
G = 9.8
TIME_DELTA = 0.02 # s

fig, ax = plt.subplots()
ln, = ax.plot([], [], marker = 'o')

def init():
    #ax.set_xlim(0, 800)
    ax.set_xlim(0, 1l
                )
    ax.set_ylim(-0.1, 1)
    return ln,

def animate(args):
    return ln,

class Simulator():
    def __init__(self):
        #self.zmp_y = [1.0, 2.0, 1.0, 2.0, 1.0, 2.0, 1.0]
        self.zmp_y = [0.4, 0.8, 0.4, 0.8, 0.4, 0.8, 0.4]
        self.zmp_time_change = [0.4, 1, 1.8, 8, 10.0] # Ultimo solo por ver penultimo
        self.zmp_idx = 0
        self.T_c = math.sqrt(HEIGHT / G)
        self.t_abs = self.t_rel = 0
        self.foot = "LF" # left foot
        print("zmp_idx",self.zmp_idx,self.foot)
        # Establecer alguno de estos dos para que arranque:
        self.y_dot_0 = 0.3
        self.y_0_rel = 0.0

    def __call__(self):

        self.t_rel += TIME_DELTA
        self.t_abs += TIME_DELTA
        
        self.y_t_rel = (self.y_0_rel * math.cosh(self.t_rel / self.T_c)) + self.T_c * self.y_dot_0 * math.sinh(self.t_rel / self.T_c)

        self.y_dot_t = (self.y_0_rel * math.sinh(self.t_rel / self.T_c) / self.T_c) + self.y_dot_0 * math.cosh(self.t_rel / self.T_c) # para conservar tras cambio

        print("t_abs: %1.2f (zmp_y[self.zmp_idx]: %5f), y_t_rel: %5.2f, y_dot_t: %5.2f" % (self.t_abs, self.zmp_y[self.zmp_idx], self.y_t_rel, self.y_dot_t))
        
        ln.set_data([self.zmp_y[self.zmp_idx], self.zmp_y[self.zmp_idx] + self.y_t_rel], [0, HEIGHT])
        # ln.set_data([180, self.currentTimeStep, 0, self.currentTimeStep], [0, HEIGHT, 0, HEIGHT])

        #sleep(0.1)

        if self.t_abs > self.zmp_time_change[self.zmp_idx]:
            self.zmp_idx += 1
            if self.foot == "LF":
                self.foot = "RF"
            else:
                self.foot = "LF"
            print("zmp_idx",self.zmp_idx,self.foot)
            self.t_rel = 0 # reseteamos tiempo
            self.y_dot_0 = self.y_dot_t # conservamos velocidad
            self.y_t_rel -= (self.zmp_y[self.zmp_idx] - self.zmp_y[self.zmp_idx-1]) # restamos lo avanzado
            self.y_0_rel = self.y_t_rel

        if self.t_abs > MAX_TIME:
            quit()

        return 1

simulator = Simulator()

def frames():
    while True:
        yield simulator()

ani = FuncAnimation(fig, animate, frames=frames,
                    interval=100, init_func=init,
                    blit=True, save_count=MAX_TIME)
plt.show()