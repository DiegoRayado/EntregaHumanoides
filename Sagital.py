#!/usr/bin/env python
"""Simulador 2D del LIPM con múltiples gráficos y animación mejorada"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# Configuración inicial
MAX_X = 24
HEIGHT = 1.2
G = 9.8
TIME_DELTA = 0.02

# Configuración de la figura con 3 subgráficos
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8), gridspec_kw={'height_ratios': [2, 1, 1]})
plt.subplots_adjust(hspace=0.4)

# Elementos gráficos
pendulum_line, = ax1.plot([], [], 'o-', lw=2)
traj_line, = ax2.plot([], [], lw=1)
vel_line, = ax3.plot([], [], lw=1, color='orange')

class Simulator():
    def __init__(self):
        self.zmp_x = [0, 4, 8, 12, 16, 20, 24]
        self.zmp_x_change = [2, 6, 10, 14, 18, 22]
        self.zmp_idx = 0
        self.T_c = math.sqrt(HEIGHT / G)
        self.t_abs = 0
        self.t_rel = 0
        self.x_dot_0 = 0.3
        self.x_0_rel = 0
        self.time_history = []
        self.position_history = []
        self.velocity_history = []

    def __call__(self):
        self.t_rel += TIME_DELTA
        self.t_abs += TIME_DELTA

        self.x_t_rel = (self.x_0_rel * math.cosh(self.t_rel / self.T_c)) + \
                       self.T_c * self.x_dot_0 * math.sinh(self.t_rel / self.T_c)
        self.x_dot_t = (self.x_0_rel * math.sinh(self.t_rel / self.T_c) / self.T_c) + \
                       self.x_dot_0 * math.cosh(self.t_rel / self.T_c)

        # Almacenamiento de datos
        current_position = self.zmp_x[self.zmp_idx] + self.x_t_rel
        self.time_history.append(self.t_abs)
        self.position_history.append(current_position)
        self.velocity_history.append(self.x_dot_t)

        # Lógica de cambio de ZMP
        if self.zmp_idx < len(self.zmp_x_change) and current_position > self.zmp_x_change[self.zmp_idx]:
            self.zmp_idx += 1
            if self.zmp_idx >= len(self.zmp_x):
                # Detener la animación si se sale del rango
                plt.close(fig)
                return pendulum_line, traj_line, vel_line
            self.t_rel = 0
            self.x_dot_0 = self.x_dot_t
            self.x_t_rel -= (self.zmp_x[self.zmp_idx] - self.zmp_x[self.zmp_idx-1])
            self.x_0_rel = self.x_t_rel

        # Actualización de elementos gráficos
        pendulum_line.set_data(
            [self.zmp_x[self.zmp_idx], current_position],
            [0, HEIGHT]
        )
        traj_line.set_data(self.time_history, self.position_history)
        vel_line.set_data(self.time_history, self.velocity_history)

        # Ajuste automático de los ejes de los subgráficos 2 y 3
        if self.time_history:
            last_time = self.time_history[-1]
            window = 10
            ax2.set_xlim(max(0, last_time - window), max(window, last_time))
            ax3.set_xlim(max(0, last_time - window), max(window, last_time))
            ax2.set_ylim(min(self.position_history[-window:]), max(self.position_history[-window:]) + 1)
            ax3.set_ylim(min(self.velocity_history[-window:]), max(self.velocity_history[-window:]) + 1)

        return pendulum_line, traj_line, vel_line

def init():
    ax1.set_xlim(0, MAX_X)
    ax1.set_ylim(-0.1, HEIGHT + 0.1)
    ax1.set_title('Simulación del Péndulo Invertido')
    ax1.grid(True)

    ax2.set_title('Evolución de la Posición')
    ax2.grid(True)

    ax3.set_title('Evolución de la Velocidad')
    ax1.set_ylim(-0.1, HEIGHT + 0.1)
    ax3.grid(True)

    return pendulum_line, traj_line, vel_line

def animate(frame):
    artists = simulator()
    return list(artists)  # Solución al error de concatenación

# Configuración de animación
simulator = Simulator()
ani = FuncAnimation(fig, animate, init_func=init,
                    interval=int(TIME_DELTA*1000), blit=True, cache_frame_data=False)

plt.show()
