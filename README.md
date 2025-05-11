# EntregaHumanoides
## Tabla de Contenidos
1. [Introducción](#Introduccion)
2. [Plano Sagital: lipm2d_sagital.py](#S)
5. [Mejoras: Sagital_Mejorado.py](#MS)
3. [Plano Frontal: lipm2d_frontal.py](#F)
4. [Mejoras: lipm2d_frontal.py](#MF)
6. [Robot Bipedo: BOBY (#BOB)}
7. [Conclusión](#i4)

## Introducción <a name="Introduccion"></a>
Tal y como se meciona en el guión con esta practica se pretende estudiar la locomocion bipeda. Dado que mi apellido es "rayado" y contiene 6 letras, la variable HEIGHT sera igual a 1.2m en toda la práctica.  

## Plano Sagital <a name="S"></a>
No se ha requerido ninguna modificación.

### Video
[Enlace](https://youtu.be/kf7UdsoY8r0)
![Archivo](lipm2d_sagital.py)

## Plano Sagital Mejorado <a name="MS"></a>
![Archivo](Sagital_Mejorado.py)
![Captura](Imagenes/Sagital.png)
### Características Principales
Se ha mejorado significativamente el código original añadiendo mayor estructura, visualización avanzada, controles interactivos y análisis adicional.
###Mejoras:
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
<pre> self.zmp_y = [0.4, 0.8, 0.4, 0.8, 0.4, 0.8, 0.4]
        self.zmp_time_change = [0.4, 1, 1.8, 8, 10.0] </code></pre>

## SigueParedes con GPS <a name="Sigueparedes"></a>
### Video
[Enlace](https://youtu.be/G5IKbE7ssrU)
### Descripcion
Este controlador tiene como finalidad localizar una pelota verde y mandar la posición de la misma. 
### Uso del turretSlot
El e-puck no tiene incorporado un GPS por lo que se le añade uno. 

![Captura](Images/Uso_turretSlot.png)

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

## Conclusion <a name="i4"></a>
Ambos algoritmos logran alcanzar la meta, pero presentan ciertas limitaciones:
### 
A*: Al depender de la odometría, tiende a acumular errores a lo largo del recorrido, a pesar de los esfuerzos por minimizar este efecto. ¿Funcionaría mejor con GPS? En teoría, sí, pero solo en esta simulación, donde el GPS no introduce error (aunque en Webots se puede añadir). En un entorno real, los GPS suelen tener un margen de error superior a un metro, lo que los haría poco útiles para este propósito.
### 
Algoritmo de seguimiento de paredes: Su lógica es más sencilla y se puede mejorar fácilmente para reducir colisiones innecesarias contra las paredes. Sin embargo, este tipo de enfoques presentan el riesgo de quedar atrapados en bucles, girando alrededor de "islas" dentro del laberinto sin encontrar la solución.
