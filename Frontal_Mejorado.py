#!/usr/bin/env python

"""\
lipm2d.py: Una simulación mejorada del modelo de péndulo invertido lineal 2D con animación matplotlib.

Este programa simula un modelo de péndulo invertido lineal (LIPM) en 2D, comúnmente utilizado para
la planificación y control de la marcha de robots bípedos. La simulación incluye visualización avanzada,
cálculos de energía orbital, trazado de trayectorias y más.

- Inspirado parcialmente en: <https://github.com/AtsushiSakai/PythonRobotics>
- Frontal = YZ
- Y representado como eje x en matplotlib
- Z representado como eje y en matplotlib
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches
import matplotlib.gridspec as gridspec
import numpy as np
from time import sleep
import math
import argparse

# Constantes físicas y de simulación
MAX_TIME = 50  # Tiempo máximo de simulación (s)
HEIGHT = 1.2  # Altura del péndulo (m)
G = 9.8  # Aceleración de la gravedad (m/s²)
TIME_DELTA = 0.02  # Incremento de tiempo (s)
MASS = 1.0  # Masa del péndulo (kg)


class LIPMSimulator:
    """Simulador del modelo de péndulo invertido lineal (LIPM) en 2D."""

    def __init__(self, height=HEIGHT, g=G, max_time=MAX_TIME):
        """
        Inicializa el simulador LIPM.

        Args:
            height: Altura del péndulo (m)
            g: Aceleración de la gravedad (m/s²)
            max_time: Tiempo máximo de simulación (s)
        """
        # Configuración ZMP (Zero Moment Point)
        self.zmp_y = [0.4, 0.8, 0.4, 0.8, 0.4, 0.8, 0.4]  # Posiciones ZMP
        self.zmp_time_change = [0.4, 1, 2, 3.5, 4, 7.4, 10.0]  # Tiempos de cambio ZMP

        # Estado inicial
        self.zmp_idx = 0
        self.height = height
        self.g = g
        self.T_c = math.sqrt(height / g)  # Constante de tiempo del LIPM
        self.t_abs = self.t_rel = 0
        self.foot = "LF"  # Left foot (pie izquierdo)

        # Condiciones iniciales
        self.y_dot_0 = 0.3  # Velocidad inicial en Y
        self.y_0_rel = 0.0  # Posición inicial relativa en Y

        # Historiales para visualización
        self.history_t = []
        self.history_y = []
        self.history_y_dot = []
        self.history_zmp = []
        self.foot_positions = []
        self.energy_history = []

        print(f"Simulador LIPM inicializado. T_c={self.T_c:.2f}s")
        print(f"ZMP inicial: {self.zmp_idx}, Pie: {self.foot}")

    def calculate_position(self):
        """Calcula la posición del péndulo en el tiempo actual."""
        # Ecuación del LIPM para la posición
        y_rel = (self.y_0_rel * math.cosh(self.t_rel / self.T_c)) + \
                (self.T_c * self.y_dot_0 * math.sinh(self.t_rel / self.T_c))
        return y_rel

    def calculate_velocity(self):
        """Calcula la velocidad del péndulo en el tiempo actual."""
        # Ecuación del LIPM para la velocidad
        y_dot = (self.y_0_rel * math.sinh(self.t_rel / self.T_c) / self.T_c) + \
                (self.y_dot_0 * math.cosh(self.t_rel / self.T_c))
        return y_dot

    def calculate_acceleration(self):
        """Calcula la aceleración del péndulo en el tiempo actual."""
        # Ecuación del LIPM para la aceleración
        y_ddot = (self.y_0_rel / (self.T_c ** 2) * math.cosh(self.t_rel / self.T_c)) + \
                 (self.y_dot_0 / self.T_c * math.sinh(self.t_rel / self.T_c))
        return y_ddot

    def calculate_orbital_energy(self, y, y_dot):
        """
        Calcula la energía orbital del péndulo.

        La energía orbital es una constante de movimiento para el LIPM:
        E = (1/2) * y_dot² - (g/2h) * y²
        """
        return 0.5 * y_dot ** 2 - (self.g / (2 * self.height)) * y ** 2

    def update(self):
        """Actualiza el estado del simulador para el siguiente paso de tiempo."""
        # Incrementar tiempo
        self.t_rel += TIME_DELTA
        self.t_abs += TIME_DELTA

        # Calcular el nuevo estado
        self.y_t_rel = self.calculate_position()
        self.y_dot_t = self.calculate_velocity()
        self.y_ddot_t = self.calculate_acceleration()

        # Calcular posición y velocidad absolutas
        self.y_abs = self.zmp_y[self.zmp_idx] + self.y_t_rel

        # Calcular energía orbital
        self.orbital_energy = self.calculate_orbital_energy(self.y_t_rel, self.y_dot_t)

        # Guardar historiales para visualización
        self.history_t.append(self.t_abs)
        self.history_y.append(self.y_abs)
        self.history_y_dot.append(self.y_dot_t)
        self.history_zmp.append(self.zmp_y[self.zmp_idx])
        self.energy_history.append(self.orbital_energy)

        # Verificar cambio de ZMP
        if self.t_abs > self.zmp_time_change[self.zmp_idx] and self.zmp_idx < len(self.zmp_time_change) - 1:
            # Registrar posición del pie
            self.foot_positions.append((self.t_abs, self.zmp_y[self.zmp_idx], self.foot))

            # Cambiar índice ZMP
            self.zmp_idx += 1

            # Alternar pie
            self.foot = "RF" if self.foot == "LF" else "LF"

            print(f"Cambio ZMP: {self.zmp_idx}, Pie: {self.foot}")

            # Reiniciar tiempo relativo
            self.t_rel = 0

            # Conservar velocidad
            self.y_dot_0 = self.y_dot_t

            # Calcular nueva posición inicial relativa
            self.y_t_rel -= (self.zmp_y[self.zmp_idx] - self.zmp_y[self.zmp_idx - 1])
            self.y_0_rel = self.y_t_rel

        # Verificar fin de simulación
        if self.t_abs > MAX_TIME:
            return False

        return True

    def get_display_data(self):
        """Retorna los datos para visualización."""
        return {
            't': self.t_abs,
            'y': self.y_abs,
            'y_dot': self.y_dot_t,
            'y_ddot': self.y_ddot_t,
            'zmp': self.zmp_y[self.zmp_idx],
            'foot': self.foot,
            'orbital_energy': self.orbital_energy,
            'history_t': self.history_t,
            'history_y': self.history_y,
            'history_y_dot': self.history_y_dot,
            'history_zmp': self.history_zmp,
            'foot_positions': self.foot_positions,
            'energy_history': self.energy_history
        }


class LIPMVisualizer:
    """Visualizador para el simulador LIPM."""

    def __init__(self, simulator, save_animation=False, interval=50):
        """
        Inicializa el visualizador.

        Args:
            simulator: Instancia del simulador LIPMSimulator
            save_animation: Si es True, guarda la animación como un archivo GIF
            interval: Intervalo de tiempo entre cuadros de animación (ms)
        """
        self.simulator = simulator
        self.save_animation = save_animation
        self.interval = interval

        # Configurar figura y subplots
        self.fig = plt.figure(figsize=(14, 10))
        self.gs = gridspec.GridSpec(3, 2, height_ratios=[3, 1, 1])

        # Subplot principal: Visualización del péndulo
        self.ax_pendulum = plt.subplot(self.gs[0, :])
        self.ax_pendulum.set_xlim(0, 1.2)
        self.ax_pendulum.set_ylim(-0.2, self.simulator.height + 0.2)
        self.ax_pendulum.set_xlabel('Posición Y (m)')
        self.ax_pendulum.set_ylabel('Altura Z (m)')
        self.ax_pendulum.set_title('Simulación de Péndulo Invertido Lineal 2D')
        self.ax_pendulum.grid(True)

        # Line objects
        self.ln_pendulum, = self.ax_pendulum.plot([], [], 'r-', linewidth=2)
        self.ln_mass, = self.ax_pendulum.plot([], [], 'ro', markersize=10, label='Masa')
        self.ln_com_trajectory, = self.ax_pendulum.plot([], [], 'b--', linewidth=1, label='Trayectoria CoM')
        self.ln_zmp, = self.ax_pendulum.plot([], [], 'gx', markersize=8, label='ZMP')

        # Pies (representados como rectángulos)
        self.left_foot = patches.Rectangle((0, -0.05), 0.1, 0.05, fc='blue', alpha=0.7)
        self.right_foot = patches.Rectangle((0, -0.05), 0.1, 0.05, fc='red', alpha=0.7)
        self.ax_pendulum.add_patch(self.left_foot)
        self.ax_pendulum.add_patch(self.right_foot)

        # Texto para mostrar información
        self.text_info = self.ax_pendulum.text(0.02, self.simulator.height * 0.9, '',
                                               fontsize=10, transform=self.ax_pendulum.transAxes)

        # Subplot: Trayectoria de posición y ZMP
        self.ax_position = plt.subplot(self.gs[1, 0])
        self.ax_position.set_xlabel('Tiempo (s)')
        self.ax_position.set_ylabel('Posición (m)')
        self.ax_position.set_title('Posición vs Tiempo')
        self.ax_position.grid(True)
        self.ln_pos_y, = self.ax_position.plot([], [], 'b-', label='Posición Y')
        self.ln_pos_zmp, = self.ax_position.plot([], [], 'g-', label='ZMP')
        self.ax_position.legend()

        # Subplot: Velocidad
        self.ax_velocity = plt.subplot(self.gs[1, 1])
        self.ax_velocity.set_xlabel('Tiempo (s)')
        self.ax_velocity.set_ylabel('Velocidad (m/s)')
        self.ax_velocity.set_title('Velocidad vs Tiempo')
        self.ax_velocity.grid(True)
        self.ln_vel_y, = self.ax_velocity.plot([], [], 'r-', label='Velocidad Y')
        self.ax_velocity.legend()

        # Subplot: Retrato de fase (Phase Portrait)
        self.ax_phase = plt.subplot(self.gs[2, 0])
        self.ax_phase.set_xlabel('Posición Y (m)')
        self.ax_phase.set_ylabel('Velocidad Y (m/s)')
        self.ax_phase.set_title('Retrato de Fase')
        self.ax_phase.grid(True)
        self.ln_phase, = self.ax_phase.plot([], [], 'g-', label='Trayectoria')
        self.ax_phase.legend()

        # Subplot: Energía orbital
        self.ax_energy = plt.subplot(self.gs[2, 1])
        self.ax_energy.set_xlabel('Tiempo (s)')
        self.ax_energy.set_ylabel('Energía Orbital')
        self.ax_energy.set_title('Energía Orbital vs Tiempo')
        self.ax_energy.grid(True)
        self.ln_energy, = self.ax_energy.plot([], [], 'm-', label='Energía')
        self.ax_energy.legend()

        # Ajustar diseño
        plt.tight_layout()

        # Crear animación
        self.ani = FuncAnimation(
            self.fig, self.update, frames=self.frames_generator,
            interval=self.interval, init_func=self.init_animation,
            blit=False, save_count=MAX_TIME * 50
        )

    def init_animation(self):
        """Inicializa la animación."""
        self.ln_pendulum.set_data([], [])
        self.ln_mass.set_data([], [])
        self.ln_com_trajectory.set_data([], [])
        self.ln_zmp.set_data([], [])
        self.left_foot.set_xy((0, -0.05))
        self.right_foot.set_xy((0, -0.05))
        self.text_info.set_text('')
        self.ln_pos_y.set_data([], [])
        self.ln_pos_zmp.set_data([], [])
        self.ln_vel_y.set_data([], [])
        self.ln_phase.set_data([], [])
        self.ln_energy.set_data([], [])
        return (self.ln_pendulum, self.ln_mass, self.ln_com_trajectory, self.ln_zmp,
                self.text_info, self.ln_pos_y, self.ln_pos_zmp, self.ln_vel_y,
                self.ln_phase, self.ln_energy)

    def update(self, i):
        """Actualiza la animación para el frame i."""
        # Obtener datos actuales
        data = self.simulator.get_display_data()

        # Actualizar péndulo
        self.ln_pendulum.set_data([data['zmp'], data['y']], [0, self.simulator.height])
        self.ln_mass.set_data([data['y']], [self.simulator.height])

        # Actualizar trayectoria de CoM
        self.ln_com_trajectory.set_data(data['history_y'], [self.simulator.height] * len(data['history_y']))

        # Actualizar ZMP
        self.ln_zmp.set_data([data['zmp']], [0])

        # Actualizar pies
        if data['foot'] == "LF":
            self.left_foot.set_xy((data['zmp'] - 0.05, -0.05))
            self.left_foot.set_alpha(1.0)
            self.right_foot.set_alpha(0.3)
        else:
            self.right_foot.set_xy((data['zmp'] - 0.05, -0.05))
            self.right_foot.set_alpha(1.0)
            self.left_foot.set_alpha(0.3)

        # Actualizar texto de información
        info_text = (
            f"Tiempo: {data['t']:.2f}s\n"
            f"Posición Y: {data['y']:.2f}m\n"
            f"Velocidad: {data['y_dot']:.2f}m/s\n"
            f"Aceleración: {data['y_ddot']:.2f}m/s²\n"
            f"ZMP: {data['zmp']:.2f}m\n"
            f"Pie: {data['foot']}\n"
            f"Energía Orbital: {data['orbital_energy']:.4f}"
        )
        self.text_info.set_text(info_text)

        # Actualizar gráficas de posición y ZMP
        self.ln_pos_y.set_data(data['history_t'], data['history_y'])
        self.ln_pos_zmp.set_data(data['history_t'], data['history_zmp'])
        self.ax_position.relim()
        self.ax_position.autoscale_view()

        # Actualizar gráfica de velocidad
        self.ln_vel_y.set_data(data['history_t'], data['history_y_dot'])
        self.ax_velocity.relim()
        self.ax_velocity.autoscale_view()

        # Actualizar retrato de fase
        self.ln_phase.set_data(data['history_y'], data['history_y_dot'])
        self.ax_phase.relim()
        self.ax_phase.autoscale_view()

        # Actualizar gráfica de energía orbital
        self.ln_energy.set_data(data['history_t'], data['energy_history'])
        self.ax_energy.relim()
        self.ax_energy.autoscale_view()

        return (self.ln_pendulum, self.ln_mass, self.ln_com_trajectory, self.ln_zmp,
                self.text_info, self.ln_pos_y, self.ln_pos_zmp, self.ln_vel_y,
                self.ln_phase, self.ln_energy)

    def frames_generator(self):
        """Generador de frames para la animación."""
        while True:
            # Actualizar simulador
            if not self.simulator.update():
                break
            yield 1

    def show(self):
        """Muestra la animación."""
        plt.show()

    def save(self, filename='lipm_animation.gif'):
        """Guarda la animación como un archivo GIF."""
        if self.save_animation:
            print(f"Guardando animación como {filename}...")
            self.ani.save(filename, writer='pillow', fps=30)
            print(f"Animación guardada correctamente.")


def parse_arguments():
    """Parsea argumentos de línea de comando."""
    parser = argparse.ArgumentParser(description='Simulador de Péndulo Invertido Lineal en 2D')
    parser.add_argument('--height', type=float, default=HEIGHT,
                        help='Altura del péndulo (m)')
    parser.add_argument('--g', type=float, default=G,
                        help='Aceleración de la gravedad (m/s²)')
    parser.add_argument('--max_time', type=float, default=MAX_TIME,
                        help='Tiempo máximo de simulación (s)')
    parser.add_argument('--save', action='store_true',
                        help='Guardar animación como GIF')
    parser.add_argument('--interval', type=int, default=50,
                        help='Intervalo entre frames de animación (ms)')
    return parser.parse_args()


def main():
    """Función principal."""
    # Parsear argumentos
    args = parse_arguments()

    # Crear simulador
    simulator = LIPMSimulator(
        height=args.height,
        g=args.g,
        max_time=args.max_time
    )

    # Crear visualizador
    visualizer = LIPMVisualizer(
        simulator=simulator,
        save_animation=args.save,
        interval=args.interval
    )

    # Mostrar animación
    visualizer.show()

    # Guardar animación si se especificó
    if args.save:
        visualizer.save()


if __name__ == "__main__":
    main()
