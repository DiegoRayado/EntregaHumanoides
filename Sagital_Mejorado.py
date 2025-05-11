#!/usr/bin/env python
"""
Simulador 2D Avanzado del Modelo de Péndulo Invertido Lineal (LIPM)
Con múltiples gráficos, animación mejorada, controles interactivos y análisis de estabilidad.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button, Slider
import math
from enum import Enum
import time


class EstadoSimulacion(Enum):
    """Enumeración para los posibles estados de la simulación."""
    EJECUTANDO = 1
    PAUSADO = 2
    DETENIDO = 3


class ModeloLIPM:
    """
    Modelo matemático del Péndulo Invertido Lineal (LIPM).
    Implementa las ecuaciones de movimiento y propiedades físicas del sistema.
    """

    def __init__(self, altura=1.2, gravedad=9.8):
        """
        Inicializa el modelo LIPM con parámetros físicos.

        Args:
            altura (float): Altura del centro de masa (en metros)
            gravedad (float): Aceleración de la gravedad (en m/s²)
        """
        self.altura = altura
        self.gravedad = gravedad
        # Constante de tiempo del péndulo invertido
        self.T_c = math.sqrt(self.altura / self.gravedad)

    def actualizar_parametros(self, altura=None, gravedad=None):
        """Actualiza los parámetros físicos del modelo."""
        if altura is not None:
            self.altura = altura
        if gravedad is not None:
            self.gravedad = gravedad
        self.T_c = math.sqrt(self.altura / self.gravedad)

    def calcular_posicion(self, x_0, x_dot_0, t):
        """
        Calcula la posición del péndulo en el tiempo t.

        Args:
            x_0 (float): Posición inicial relativa al ZMP
            x_dot_0 (float): Velocidad inicial
            t (float): Tiempo transcurrido

        Returns:
            float: Posición relativa en el tiempo t
        """
        return (x_0 * math.cosh(t / self.T_c)) + \
            self.T_c * x_dot_0 * math.sinh(t / self.T_c)

    def calcular_velocidad(self, x_0, x_dot_0, t):
        """
        Calcula la velocidad del péndulo en el tiempo t.

        Args:
            x_0 (float): Posición inicial relativa al ZMP
            x_dot_0 (float): Velocidad inicial
            t (float): Tiempo transcurrido

        Returns:
            float: Velocidad en el tiempo t
        """
        return (x_0 * math.sinh(t / self.T_c) / self.T_c) + \
            x_dot_0 * math.cosh(t / self.T_c)

    def calcular_energia(self, x, x_dot):
        """
        Calcula la energía total del sistema.

        Args:
            x (float): Posición relativa al ZMP
            x_dot (float): Velocidad actual

        Returns:
            tuple: (Energía potencial, Energía cinética, Energía total)
        """
        # Suponemos una masa unitaria para simplificar
        energia_potencial = self.gravedad * self.altura
        energia_cinetica = 0.5 * x_dot ** 2
        energia_total = energia_potencial + energia_cinetica
        return energia_potencial, energia_cinetica, energia_total


class SimuladorLIPM:
    """
    Simulador del LIPM que gestiona la evolución temporal, los cambios de ZMP,
    y almacena el historial de estados.
    """

    def __init__(self, modelo, dt=0.02):
        """
        Inicializa el simulador.

        Args:
            modelo (ModeloLIPM): Modelo físico a utilizar
            dt (float): Incremento de tiempo por paso (en segundos)
        """
        self.modelo = modelo
        self.dt = dt

        # Puntos de momento cero (ZMP)
        self.zmp_x = [0, 4, 8, 12, 16, 20, 24]  # Posiciones de los ZMP
        self.zmp_x_change = [2, 6, 10, 14, 18, 22]  # Puntos de cambio de ZMP
        self.zmp_idx = 0  # Índice del ZMP actual

        # Estado actual
        self.t_abs = 0  # Tiempo absoluto
        self.t_rel = 0  # Tiempo relativo al último cambio de ZMP
        self.x_dot_0 = 0.3  # Velocidad inicial
        self.x_0_rel = 0  # Posición inicial relativa al ZMP actual
        self.estado = EstadoSimulacion.EJECUTANDO

        # Historiales
        self.historial_tiempo = []
        self.historial_posicion = []
        self.historial_velocidad = []
        self.historial_energia = []
        self.historial_zmp = []

        # Estados adicionales para cálculos
        self.x_t_rel = 0  # Posición relativa actual
        self.x_dot_t = 0  # Velocidad actual

        # Tiempo de la última actualización (para pausas)
        self.ultimo_tiempo_real = time.time()
        self.tiempo_pausado = 0

    def reiniciar(self):
        """Reinicia la simulación a su estado inicial."""
        self.__init__(self.modelo, self.dt)

    def pausar_reanudar(self):
        """Alterna entre pausa y ejecución."""
        tiempo_actual = time.time()

        if self.estado == EstadoSimulacion.EJECUTANDO:
            self.estado = EstadoSimulacion.PAUSADO
            self.tiempo_pausado = tiempo_actual
        else:
            self.estado = EstadoSimulacion.EJECUTANDO
            # Ajustar el tiempo absoluto para compensar la pausa
            delta_pausa = tiempo_actual - self.tiempo_pausado
            self.ultimo_tiempo_real += delta_pausa

    def paso(self):
        """
        Ejecuta un paso de simulación.

        Returns:
            tuple: (posición_actual, zmp_actual)
        """
        if self.estado != EstadoSimulacion.EJECUTANDO:
            return self.zmp_x[self.zmp_idx] + self.x_t_rel, self.zmp_x[self.zmp_idx]

        # Actualizar tiempos
        self.t_rel += self.dt
        self.t_abs += self.dt

        # Calcular nuevo estado
        self.x_t_rel = self.modelo.calcular_posicion(self.x_0_rel, self.x_dot_0, self.t_rel)
        self.x_dot_t = self.modelo.calcular_velocidad(self.x_0_rel, self.x_dot_0, self.t_rel)

        # Calcular posición absoluta
        posicion_actual = self.zmp_x[self.zmp_idx] + self.x_t_rel

        # Calcular energías
        energia_pot, energia_cin, energia_total = self.modelo.calcular_energia(self.x_t_rel, self.x_dot_t)

        # Almacenar historiales
        self.historial_tiempo.append(self.t_abs)
        self.historial_posicion.append(posicion_actual)
        self.historial_velocidad.append(self.x_dot_t)
        self.historial_energia.append(energia_total)
        self.historial_zmp.append(self.zmp_x[self.zmp_idx])

        # Lógica de cambio de ZMP
        if self.zmp_idx < len(self.zmp_x_change) and posicion_actual > self.zmp_x_change[self.zmp_idx]:
            self.zmp_idx += 1
            if self.zmp_idx >= len(self.zmp_x):
                # Límite alcanzado
                self.estado = EstadoSimulacion.DETENIDO
                return posicion_actual, self.zmp_x[self.zmp_idx - 1]

            # Actualizar estado para el nuevo ZMP
            self.t_rel = 0
            self.x_dot_0 = self.x_dot_t
            # La posición relativa se ajusta con respecto al nuevo ZMP
            self.x_t_rel -= (self.zmp_x[self.zmp_idx] - self.zmp_x[self.zmp_idx - 1])
            self.x_0_rel = self.x_t_rel

        return posicion_actual, self.zmp_x[self.zmp_idx]


class VisualizadorLIPM:
    """
    Gestiona la visualización gráfica y la animación del simulador LIPM.
    """

    def __init__(self, simulador):
        """
        Inicializa el visualizador.

        Args:
            simulador (SimuladorLIPM): Simulador a visualizar
        """
        self.simulador = simulador
        self.creando_widgets = True
        self.configurar_figura()
        self.creando_widgets = False

    def configurar_figura(self):
        """Configura la figura de matplotlib con todos los subgráficos y controles."""
        # Crear figura con 4 subgráficos
        self.fig = plt.figure(figsize=(12, 10))
        gs = self.fig.add_gridspec(4, 1, height_ratios=[2, 1, 1, 1], hspace=0.3)
        

        # Subgráfico para la animación del péndulo
        self.ax_pendulo = self.fig.add_subplot(gs[0])
        self.ax_pendulo.set_xlim(0, max(self.simulador.zmp_x) + 2)
        self.ax_pendulo.set_ylim(-0.2, self.simulador.modelo.altura + 0.5)
        self.ax_pendulo.set_title('Simulación del Péndulo Invertido Lineal', fontweight='bold')
        self.ax_pendulo.set_xlabel('Posición (m)')
        self.ax_pendulo.set_ylabel('Altura (m)')
        self.ax_pendulo.grid(True, linestyle='--', alpha=0.7)

        # Dibujar los puntos ZMP fijos
        for zmp in self.simulador.zmp_x:
            self.ax_pendulo.plot(zmp, 0, 'ro', markersize=5)

        # Dibujar líneas verticales para los puntos de cambio de ZMP
        for cambio in self.simulador.zmp_x_change:
            self.ax_pendulo.axvline(x=cambio, color='r', linestyle='--', alpha=0.3)

        # Elementos gráficos del péndulo
        self.linea_pendulo, = self.ax_pendulo.plot([], [], 'o-', lw=2, color='blue',
                                                   label='Péndulo')
        self.punto_zmp, = self.ax_pendulo.plot([], [], 'gD', markersize=8,
                                               label='ZMP Activo')
        self.ax_pendulo.legend(loc='upper right')

        # Subgráfico para la evolución de la posición
        self.ax_posicion = self.fig.add_subplot(gs[1], sharex=self.ax_pendulo)
        self.ax_posicion.set_title('Evolución de la Posición', fontweight='bold')
        self.ax_posicion.set_ylabel('Posición (m)')
        self.ax_posicion.grid(True, linestyle='--', alpha=0.7)
        self.linea_posicion, = self.ax_posicion.plot([], [], lw=1.5, color='green')
        self.linea_zmp, = self.ax_posicion.plot([], [], 'r--', lw=1, alpha=0.7,
                                                label='ZMP')
        self.ax_posicion.legend(loc='upper right')

        # Subgráfico para la evolución de la velocidad
        self.ax_velocidad = self.fig.add_subplot(gs[2], sharex=self.ax_pendulo)
        self.ax_velocidad.set_title('Evolución de la Velocidad', fontweight='bold')
        self.ax_velocidad.set_ylabel('Velocidad (m/s)')
        self.ax_velocidad.grid(True, linestyle='--', alpha=0.7)
        self.linea_velocidad, = self.ax_velocidad.plot([], [], lw=1.5, color='orange')

        # Subgráfico para la evolución de la energía
        self.ax_energia = self.fig.add_subplot(gs[3], sharex=self.ax_pendulo)
        self.ax_energia.set_title('Evolución de la Energía', fontweight='bold')
        self.ax_energia.set_xlabel('Tiempo (s)')
        self.ax_energia.set_ylabel('Energía (J)')
        self.ax_energia.grid(True, linestyle='--', alpha=0.7)
        self.linea_energia, = self.ax_energia.plot([], [], lw=1.5, color='purple')

        # Botones de control
        self.ax_boton_pausa = plt.axes([0.81, 0.02, 0.1, 0.04])
        self.boton_pausa = Button(self.ax_boton_pausa, 'Pausar')
        self.boton_pausa.on_clicked(self.accion_pausar)

        self.ax_boton_reiniciar = plt.axes([0.7, 0.02, 0.1, 0.04])
        self.boton_reiniciar = Button(self.ax_boton_reiniciar, 'Reiniciar')
        self.boton_reiniciar.on_clicked(self.accion_reiniciar)

        # Sliders para parámetros
        self.ax_slider_altura = plt.axes([0.25, 0.02, 0.3, 0.03])
        self.slider_altura = Slider(
            self.ax_slider_altura, 'Altura (m)',
            0.5, 2.0, valinit=self.simulador.modelo.altura
        )
        self.slider_altura.on_changed(self.accion_cambiar_altura)

        # Etiqueta para mostrar información durante la simulación
        self.texto_info = self.ax_pendulo.text(
            0.02, 0.95, '', transform=self.ax_pendulo.transAxes,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        )

    def accion_pausar(self, event):
        """Acción para el botón de pausar/reanudar."""
        if not self.creando_widgets:
            self.simulador.pausar_reanudar()
            texto = 'Reanudar' if self.simulador.estado == EstadoSimulacion.PAUSADO else 'Pausar'
            self.boton_pausa.label.set_text(texto)

    def accion_reiniciar(self, event):
        """Acción para el botón de reiniciar."""
        if not self.creando_widgets:
            self.simulador.reiniciar()
            self.boton_pausa.label.set_text('Pausar')

    def accion_cambiar_altura(self, val):
        """Acción para el slider de altura."""
        if not self.creando_widgets:
            self.simulador.modelo.actualizar_parametros(altura=val)

    def inicializar_animacion(self):
        """
        Inicializa los elementos de la animación.

        Returns:
            list: Lista de artistas gráficos a animar
        """
        self.linea_pendulo.set_data([], [])
        self.punto_zmp.set_data([], [])
        self.linea_posicion.set_data([], [])
        self.linea_velocidad.set_data([], [])
        self.linea_energia.set_data([], [])
        self.linea_zmp.set_data([], [])
        self.texto_info.set_text('')
        return [self.linea_pendulo, self.punto_zmp, self.linea_posicion,
                self.linea_velocidad, self.linea_energia, self.linea_zmp,
                self.texto_info]

    def animar(self, i):
        """
        Función de animación que actualiza los gráficos en cada frame.

        Args:
            i (int): Número de frame

        Returns:
            list: Lista de artistas gráficos actualizados
        """
        # Actualizar el simulador
        posicion_actual, zmp_actual = self.simulador.paso()

        # Actualizar elementos gráficos
        self.linea_pendulo.set_data(
            [zmp_actual, posicion_actual],
            [0, self.simulador.modelo.altura]
        )
        self.punto_zmp.set_data([zmp_actual], [0])

        # Actualizar gráficos de historial
        self.linea_posicion.set_data(
            self.simulador.historial_tiempo,
            self.simulador.historial_posicion
        )
        self.linea_zmp.set_data(
            self.simulador.historial_tiempo,
            self.simulador.historial_zmp
        )
        self.linea_velocidad.set_data(
            self.simulador.historial_tiempo,
            self.simulador.historial_velocidad
        )
        self.linea_energia.set_data(
            self.simulador.historial_tiempo,
            self.simulador.historial_energia
        )

        # Ajustar los límites de los ejes automáticamente
        if self.simulador.historial_tiempo:
            ultimo_tiempo = self.simulador.historial_tiempo[-1]
            ventana = 10  # Mostrar los últimos 10 segundos

            # Limitar la ventana de visualización al rango de tiempo relevante
            tiempo_min = max(0, ultimo_tiempo - ventana)
            tiempo_max = max(ventana, ultimo_tiempo)

            # Actualizar límites de los ejes
            for ax in [self.ax_posicion, self.ax_velocidad, self.ax_energia]:
                ax.set_xlim(tiempo_min, tiempo_max)

            # Ajustar límites verticales para los datos visibles
            indices_visibles = [i for i, t in enumerate(self.simulador.historial_tiempo)
                                if tiempo_min <= t <= tiempo_max]

            if indices_visibles:
                # Posición
                posiciones_visibles = [self.simulador.historial_posicion[i] for i in indices_visibles]
                min_pos = min(posiciones_visibles) - 0.5
                max_pos = max(posiciones_visibles) + 0.5
                self.ax_posicion.set_ylim(min_pos, max_pos)

                # Velocidad
                velocidades_visibles = [self.simulador.historial_velocidad[i] for i in indices_visibles]
                min_vel = min(velocidades_visibles) - 0.2
                max_vel = max(velocidades_visibles) + 0.2
                self.ax_velocidad.set_ylim(min_vel, max_vel)

                # Energía
                energias_visibles = [self.simulador.historial_energia[i] for i in indices_visibles]
                min_ener = min(energias_visibles) * 0.9
                max_ener = max(energias_visibles) * 1.1
                self.ax_energia.set_ylim(min_ener, max_ener)

        # Actualizar texto informativo
        texto = (
            f"Tiempo: {self.simulador.t_abs:.2f}s\n"
            f"Posición: {posicion_actual:.2f}m\n"
            f"Velocidad: {self.simulador.x_dot_t:.2f}m/s\n"
            f"ZMP Actual: {zmp_actual:.1f}m\n"
            f"Estado: {'PAUSADO' if self.simulador.estado == EstadoSimulacion.PAUSADO else 'EJECUTANDO'}"
        )
        self.texto_info.set_text(texto)

        return [self.linea_pendulo, self.punto_zmp, self.linea_posicion,
                self.linea_velocidad, self.linea_energia, self.linea_zmp,
                self.texto_info]

    def iniciar_animacion(self):
        """Inicia la animación y muestra la figura."""
        self.animacion = FuncAnimation(
            self.fig, self.animar, init_func=self.inicializar_animacion,
            interval=int(self.simulador.dt * 1000), blit=True, cache_frame_data=False
        )
        plt.show()


def ejecutar_simulacion():
    """Función principal para ejecutar la simulación."""
    # Crear modelo LIPM
    modelo = ModeloLIPM(altura=1.2, gravedad=9.8)

    # Crear simulador
    simulador = SimuladorLIPM(modelo, dt=0.02)

    # Crear visualizador y iniciar animación
    visualizador = VisualizadorLIPM(simulador)
    visualizador.iniciar_animacion()


if __name__ == "__main__":
    ejecutar_simulacion()
