#!/usr/bin/env python
"""
Enhanced 2D LIPM Simulator with oscillating Z position and detailed visualization.
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import math

# ======== Configuration ========
MAX_TIME = 60  # seconds
HEIGHT = 1.2  # [m] Base COM height
G = 9.8  # [m/s^2]
TIME_DELTA = 0.08  # [s] (50 Hz)
PLOT_HISTORY = 60.0  # [s] How much history to display

# ======== Visualization Setup ========
plt.style.use('dark_background')
fig = plt.figure(figsize=(14, 9))
gs = fig.add_gridspec(3, 2)

# Main animation plot
ax1 = fig.add_subplot(gs[:2, :])
ax1.set_title('2D LIPM Simulation', fontsize=16)
ax1.set_xlabel('Y Position [m]')
ax1.set_ylabel('Z Position [m]')
ax1.set_xlim(0, 3)
ax1.set_ylim(-0.1, HEIGHT + 0.4)

# Trajectory plot
ax2 = fig.add_subplot(gs[2, 0])
ax2.set_title('COM Trajectory')
ax2.set_xlabel('Time [s]')
ax2.set_ylabel('Y Position [m]')

# Velocity/Acceleration plot
ax3 = fig.add_subplot(gs[2, 1])
ax3.set_title('Dynamics')
ax3.set_xlabel('Time [s]')

# ======== Visualization Objects ========
com_line, = ax1.plot([], [], 'b-', lw=2, alpha=0.6)
zmp_line, = ax1.plot([], [], 'g--', lw=1)
com_marker, = ax1.plot([], [], 'bo', ms=8)
zmp_marker, = ax1.plot([], [], 'gX', ms=14, mew=2)
foot_marker, = ax1.plot([], [], 'rs', ms=15, alpha=0.5)

traj_line, = ax2.plot([], [], 'b-', lw=1)
vel_line, = ax3.plot([], [], 'r-', label='Velocity')
acc_line, = ax3.plot([], [], 'g-', label='Acceleration')
ax3.legend()


# ======== Physics Engine ========
class EnhancedSimulatorZ:
    def __init__(self):
        self.Tc = math.sqrt(HEIGHT / G)
        self.reset()
        # ZMP pattern (time, position, foot)
        self.zmp_sequence = [
            (0.7, 1.0, "LF"),
            (2.1, 2.0, "RF"),
            (2.8, 1.0, "LF"),
            (3.2, 2.0, "RF"),
            (10.0, 1.0, "LF")
        ]

    def reset(self):
        self.time = []
        self.com_history = []
        self.com_z_history = []
        self.zmp_history = []
        self.vel_history = []
        self.acc_history = []
        self.foot_positions = []
        self.current_zmp = 1.0
        self.current_foot = "LF"
        self.step_counter = 0
        self.last_switch = 0.0
        self.y = 0.0
        self.y_dot = 0.3

    def compute_dynamics(self, t):
        cosh = math.cosh(t / self.Tc)
        sinh = math.sinh(t / self.Tc)
        y = self.y * cosh + self.Tc * self.y_dot * sinh
        y_dot = (self.y / self.Tc) * sinh + self.y_dot * cosh
        y_acc = (y / HEIGHT) * G
        return y, y_dot, y_acc

    def z_position(self, t):
        amplitude = 0.05  # Oscillation amplitude in meters
        frequency = 1.0  # Oscillation frequency in Hz
        z = HEIGHT + amplitude * math.sin(2 * math.pi * frequency * t)
        return z

    def update(self, frame):
        t = len(self.time) * TIME_DELTA
        self.time.append(t)
        if self.step_counter < len(self.zmp_sequence):
            next_time, next_zmp, next_foot = self.zmp_sequence[self.step_counter]
            if t >= next_time:
                self._switch_zmp(next_zmp, next_foot, t)
        elapsed = t - self.last_switch
        y_rel, y_dot, y_acc = self.compute_dynamics(elapsed)
        com_y = self.current_zmp + y_rel
        com_z = self.z_position(t)
        self.com_history.append(com_y)
        self.com_z_history.append(com_z)
        self.zmp_history.append(self.current_zmp)
        self.vel_history.append(y_dot)
        self.acc_history.append(y_acc)
        self._update_plots()
        if t >= MAX_TIME:
            self.reset()
            return []
        return [com_line, zmp_line, com_marker, zmp_marker, foot_marker,
                traj_line, vel_line, acc_line]

    def _switch_zmp(self, new_zmp, new_foot, t):
        self.y = (self.com_history[-1] - new_zmp)
        self.y_dot = self.vel_history[-1]
        self.current_zmp = new_zmp
        self.current_foot = new_foot
        self.step_counter += 1
        self.last_switch = t
        self.foot_positions.append((new_foot, new_zmp, t))

    def _update_plots(self):
        N = int(PLOT_HISTORY / TIME_DELTA)
        com_line.set_data(self.com_history[-N:], self.com_z_history[-N:])
        zmp_line.set_data(self.zmp_history[-N:], [0] * len(self.zmp_history[-N:]))
        com_marker.set_data([self.com_history[-1]], [self.com_z_history[-1]])
        zmp_marker.set_data([self.current_zmp], [0])
        feet_x = [pos[1] for pos in self.foot_positions]
        feet_y = [0] * len(feet_x)
        foot_marker.set_data(feet_x, feet_y)
        traj_line.set_data(self.time, self.com_history)
        ax2.relim()
        ax2.autoscale_view()
        vel_line.set_data(self.time, self.vel_history)
        acc_line.set_data(self.time, self.acc_history)
        ax3.relim()
        ax3.autoscale_view()


# ======== Run Simulation ========
sim = EnhancedSimulatorZ()
ani = FuncAnimation(fig, sim.update,
                    interval=TIME_DELTA * 1000,
                    blit=True,
                    cache_frame_data=False)

plt.tight_layout()
plt.show()
