# EntregaHumanoides
## Tabla de Contenidos
1. [Introducción](#Introduccion)
2. [Plano Sagital: lipm2d_sagital.py](#S)
5. [Mejoras: Sagital_Mejorado.py](#MS)
3. [Plano Frontal: lipm2d_frontal.py](#F)
4. [Mejoras: Frontal_Mejorado.py](#MF)
6. [Robot Bipedo: BOBY ](#BOB)
7. [Conclusión](#i4)

## Introducción <a name="Introduccion"></a>
Tal y como se meciona en el guión con esta practica se pretende estudiar la locomocion bipeda. Dado que mi apellido es "rayado" y contiene 6 letras, la variable HEIGHT sera igual a 1.2m en toda la práctica.  

## Plano Sagital <a name="S"></a>
No se ha requerido ninguna modificación.
![Video](https://youtu.be/kf7UdsoY8r0)
![Archivo](lipm2d_sagital.py)

## Plano Sagital Mejorado <a name="MS"></a>
![Archivo](Sagital_Mejorado.py)
![Captura](Imagenes/Sagital.png)
### Características Principales
Se ha mejorado significativamente el código original añadiendo mayor estructura, visualización avanzada, controles interactivos y análisis adicional.
### Mejoras:
#### Estructura del Código
- Organización orientada a objetos: Separación clara entre modelo físico, simulación y visualización
- Documentación completa: Docstrings explicativos y comentarios detallados
- Mejor manejo de estados: Control del ciclo de vida de la simulación
#### Visualizacion 
- Panel informativo en tiempo real: Muestra datos de posición, velocidad y estado
- Visualización de ZMP: Puntos y transiciones claramente marcados
- Gráfico de energía: Nuevo gráfico que muestra la evolución energética del sistema
- Mejor estética: Leyendas y cuadrículas mejoradas
### Funcionalidad
- Botones para pausar/reanudar/parar
- Calculo de energía 

## Plano Frontal <a name="F"></a>
Se ha realizado la modificacion de los siguientes parámetros:
<pre> self.zmp_y = [0.4, 0.8, 0.4, 0.8, 0.4, 0.8, 0.4] </code></pre>
<pre> self.zmp_time_change = [0.4, 1, 1.8, 8, 10.0] </code></pre>

Con estas modificaciones se consigue que sea capaz de hacer ida-vuelta-ida
![Video](https://youtu.be/G5IKbE7ssrU)

## Plano Frontal Mejorado <a name="MF"></a>
![Archivo](Frontal_Mejorado.py)
![Captura](Imagenes/Frontal.png)
<ol class="marker:text-textOff list-decimal">
<li>
<p class="my-0"><strong>Vista principal mejorada</strong>:</p>
<ul class="marker:text-textOff list-disc">
<li>
<p class="my-0">Visualización completa del péndulo con línea de conexión y masa</p>
</li>
<li>
<p class="my-0">Representación de los puntos ZMP (Zero Moment Point)</p>
</li>
<li>
<p class="my-0">Trazado de la trayectoria del Centro de Masa (CoM)</p>
</li>
<li>
<p class="my-0">Representación visual de los pies (izquierdo/derecho) utilizando rectángulos con colores diferenciados</p>
</li>
</ul>
</li>
<li>
<p class="my-0"><strong>Panel de información en tiempo real</strong>:</p>
<ul class="marker:text-textOff list-disc">
<li>
<p class="my-0">Tiempo actual</p>
</li>
<li>
<p class="my-0">Posición, velocidad y aceleración</p>
</li>
<li>
<p class="my-0">ZMP actual</p>
</li>
<li>
<p class="my-0">Pie activo</p>
</li>
<li>
<p class="my-0">Energía orbital</p>
</li>
</ul>
</li>
<li>
<p class="my-0"><strong>Múltiples gráficas de análisis</strong><a target="_blank" rel="nofollow noopener" <span class="relative select-none align-middle undefined -top-px font-sans text-base text-textMain dark:text-textMainDark selection:bg-super/50 selection:text-textMain dark:selection:bg-superDuper/10 dark:selection:text-superDark"><span class="hover:bg-super dark:hover:bg-superDark dark:hover:text-backgroundDark min-w-[1rem] rounded-[0.3125rem] px-[0.3rem] text-center align-middle font-mono text-[0.6rem] tabular-nums hover:text-white py-[0.1875rem] border-borderMain/50 ring-borderMain/50 divide-borderMain/50 dark:divide-borderMainDark/50 dark:ring-borderMainDark/50 dark:border-borderMainDark/50 bg-offsetPlus dark:bg-offsetPlusDark">11</span></span></a><a target="_blank" rel="nofollow noopener" class="citation ml-xs inline" data-state="closed" <span class="relative select-none align-middle undefined -top-px font-sans text-base text-textMain dark:text-textMainDark selection:bg-super/50 selection:text-textMain dark:selection:bg-superDuper/10 dark:selection:text-superDark"><span class="hover:bg-super dark:hover:bg-superDark dark:hover:text-backgroundDark min-w-[1rem] rounded-[0.3125rem] px-[0.3rem] text-center align-middle font-mono text-[0.6rem] tabular-nums hover:text-white py-[0.1875rem] border-borderMain/50 ring-borderMain/50 divide-borderMain/50 dark:divide-borderMainDark/50 dark:ring-borderMainDark/50 dark:border-borderMainDark/50 bg-offsetPlus dark:bg-offsetPlusDark">12</span></span></a>:</p>
<ul class="marker:text-textOff list-disc">
<li>
<p class="my-0">Gráfica de posición vs. tiempo (tanto del CoM como del ZMP)</p>
</li>
<li>
<p class="my-0">Gráfica de velocidad vs. tiempo</p>
</li>
<li>
<p class="my-0">Retrato de fase (phase portrait) que muestra la relación entre posición y velocidad</p>
</li>
<li>
<p class="my-0">Evolución de la energía orbital a lo largo del tiempo</p>
</li>
</ul>
</li>
<li>
<p class="my-0"><strong>Cálculos dinámicos</strong>:</p>
<ul class="marker:text-textOff list-disc">
<li>
<p class="my-0">Posición utilizando las ecuaciones del LIPM: <code>y = y₀·cosh(t/Tc) + Tc·ẏ₀·sinh(t/Tc)</code></p>
</li>
<li>
<p class="my-0">Velocidad: <code>ẏ = (y₀·sinh(t/Tc)/Tc) + ẏ₀·cosh(t/Tc)</code></p>
</li>
<li>
<p class="my-0">Aceleración: <code>ÿ = (y₀/(Tc²))·cosh(t/Tc) + (ẏ₀/Tc)·sinh(t/Tc)</code></p>
</li>
</ul>
</li>
<li>
<p class="my-0"><strong>Energía orbital</strong><a target="_blank" rel="nofollow noopener" <span class="relative select-none align-middle undefined -top-px font-sans text-base text-textMain dark:text-textMainDark selection:bg-super/50 selection:text-textMain dark:selection:bg-superDuper/10 dark:selection:text-superDark"><span class="hover:bg-super dark:hover:bg-superDark dark:hover:text-backgroundDark min-w-[1rem] rounded-[0.3125rem] px-[0.3rem] text-center align-middle font-mono text-[0.6rem] tabular-nums hover:text-white py-[0.1875rem] border-borderMain/50 ring-borderMain/50 divide-borderMain/50 dark:divide-borderMainDark/50 dark:ring-borderMainDark/50 dark:border-borderMainDark/50 bg-offsetPlus dark:bg-offsetPlusDark">10</span></span></a>:</p>
<ul class="marker:text-textOff list-disc">
<li>
<p class="my-0">Calculada como <code>E = (1/2)·ẏ² - (g/2h)·y²</code></p>
</li>
<li>
<p class="my-0">Representación de su evolución temporal</p>
</li>
<li>
<p class="my-0">Conservación durante cada fase de apoyo</p>
</li>
</ul>
</li>
<li>
<p class="my-0"><strong>Transiciones de apoyo</strong>:</p>
<ul class="marker:text-textOff list-disc">
<li>
<p class="my-0">Cálculo de puntos de cambio de ZMP</p>
</li>
<li>
<p class="my-0">Conservación de la velocidad durante las transiciones</p>
</li>
<li>
<p class="my-0">Ajuste de la posición relativa al nuevo punto de apoyo</p>
</li>
</ul>
</li>
</ol>



### Lógica del Programa
1. **Inicialización**: Se configuran los dispositivos y sensores del robot.
2. **Detección de objetos verdes**: Se analiza la imagen capturada por la cámara para detectar la presencia de color verde.
3. **Seguimiento del objeto**:
   - Si el objeto verde se encuentra en la izquierda, el robot gira hacia la izquierda.
   - Si el objeto está en la derecha, el robot gira a la derecha.
   - Si el objeto está en el centro, el robot avanza en línea recta.
4. **Seguimiento de pared**:
   - Si el robot no detecta nada verde sigue la pared. 
5. **Detención**: Si el porcentaje de verde en la imagen supera el umbral definido (50%), el robot se detiene completamente.
### Terminal
Va mostrando la posicion del GPS y finaliza avisando de que ha llegado a la pelota.

![Captura](Images/TerminalSigueParedes.png)
## Robot Bipedo: BOBY <a name="BOB"></a>
## Conclusion <a name="i4"></a>
Ambos algoritmos logran alcanzar la meta, pero presentan ciertas limitaciones:
### 
A*: Al depender de la odometría, tiende a acumular errores a lo largo del recorrido, a pesar de los esfuerzos por minimizar este efecto. ¿Funcionaría mejor con GPS? En teoría, sí, pero solo en esta simulación, donde el GPS no introduce error (aunque en Webots se puede añadir). En un entorno real, los GPS suelen tener un margen de error superior a un metro, lo que los haría poco útiles para este propósito.
### 
Algoritmo de seguimiento de paredes: Su lógica es más sencilla y se puede mejorar fácilmente para reducir colisiones innecesarias contra las paredes. Sin embargo, este tipo de enfoques presentan el riesgo de quedar atrapados en bucles, girando alrededor de "islas" dentro del laberinto sin encontrar la solución.
