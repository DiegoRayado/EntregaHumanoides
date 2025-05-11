# EntregaHumanoides
## Tabla de Contenidos
1. [Introducción](#Introduccion)
2. [Plano Sagital: lipm2d_sagital.py](#S)
5. [Mejoras: Sagital_Mejorado.py](#MS)
3. [Plano Frontal: lipm2d_frontal.py](#F)
4. [Mejoras: Frontal_Mejorado.py](#MF)
6. [Robot Bipedo: BOBY ](#BOB)

## Introducción <a name="Introduccion"></a>
Tal y como se meciona en el guión con esta practica se pretende estudiar la locomocion bipeda. Dado que mi apellido es "rayado" y contiene 6 letras, la variable HEIGHT sera igual a 1.2m en toda la práctica.  

## Plano Sagital <a name="S"></a>
No se ha requerido ninguna modificación.
[Video](https://youtu.be/t9dBL4-J16M)
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
[Video](https://youtu.be/FZKNNdqZmL8)

## Plano Frontal Mejorado <a name="MF"></a>
![Archivo](Frontal_Mejorado.py)
![Captura](Imagenes/Frontal.png)

### Mejoras realizadas:
<ol class="marker:text-textOff list-decimal">
<li>
<p class="my-0"><strong>Vista principal mejorada</strong>: Visualización completa del péndulo con línea de conexión y masa, representación de los puntos ZMP (Zero Moment Point), trazado de la trayectoria del Centro de Masa (CoM) y visualización de los pies (izquierdo/derecho) usando rectángulos de colores diferenciados.</p>
</li>
<li>
<p class="my-0"><strong>Panel de información en tiempo real</strong>: Muestra el tiempo actual, posición, velocidad, aceleración, ZMP actual, pie activo y energía orbital.</p>
</li>
<li>
<p class="my-0"><strong>Múltiples gráficas de análisis</strong>: Incluye gráfica de posición vs. tiempo (del CoM y del ZMP), gráfica de velocidad vs. tiempo, retrato de fase (relación entre posición y velocidad) y evolución de la energía orbital a lo largo del tiempo.</p>
</li>
<li>
<p class="my-0"><strong>Cálculos dinámicos</strong>: Se calcula la posición usando las ecuaciones del LIPM: y = y₀·cosh(t/Tc) + Tc·ẏ₀·sinh(t/Tc), la velocidad: ẏ = (y₀·sinh(t/Tc)/Tc) + ẏ₀·cosh(t/Tc), y la aceleración: ÿ = (y₀/(Tc²))·cosh(t/Tc) + (ẏ₀/Tc)·sinh(t/Tc).</p>
</li>
<li>
<p class="my-0"><strong>Energía orbital</strong>: Calculada como E = (1/2)·ẏ² - (g/2h)·y², se representa su evolución temporal y se conserva durante cada fase de apoyo.</p>
</li>
<li>
<p class="my-0"><strong>Transiciones de apoyo</strong>: Se calcula el punto de cambio de ZMP, se conserva la velocidad durante la transición y se ajusta la posición relativa al nuevo punto de apoyo.</p>
</li>
</ol>

## Robot Bipedo: BOBY <a name="BOB"></a>

Para estudiar más en profundidad la locomoción bípeda, he desarrollado un robot al que he llamado Boby. Boby es más bien medio robot, ya que solo consta de dos piernas movidas por un total de dos servomotores 9G, uno por pierna. El diseño de Boby no supuso un gran desafío en términos generales, ya que se basó en conceptos básicos de robots bípedos simplificados, enfocados en replicar el movimiento esencial de caminar con la menor cantidad de componentes posible. Sin embargo, un componente clave presentó una dificultad significativa: los pies. Con solo un servomotor por pierna, el control del equilibrio y la estabilidad se vuelve extremadamente complicado, y los pies juegan un papel crucial para compensar esta limitación. El diseño de los pies necesitaba garantizar un contacto adecuado con el suelo y una base lo suficientemente amplia para soportar el peso del robot, algo que todavia no esta optimizado.

Ficheros 3D y código en la carpeta Boby
### Boby anda!!! [Video](https://youtu.be/WE5tCC_DQgw)

### Boby con sus primeros pies
![Captura](Imagenes/Boby.png)

### Boby version final
![Captura](Imagenes/Boby2.jpg)

### Codigo Boby

<h2 class="mb-2 mt-6 text-lg font-[500] first:mt-0 dark:font-[475]" id="explicacin-general">Explicación General</h2>
<p class="my-0">El código mueve dos servomotores (pierna izquierda y derecha) de manera coordinada, usando funciones seno para simular un movimiento suave y alternado, como si el robot caminara.</p>

<h2 class="mb-2 mt-6 text-lg font-[500] first:mt-0 dark:font-[475]" id="secciones-del-cdigo">Secciones del Código</h2>
<h2 class="mb-xs mt-5 text-base font-[500] first:mt-0 dark:font-[475]">1. <strong>Inclusión de la librería y creación de objetos Servo</strong></h2>
<div class="w-full md:max-w-[90vw]"><pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-textMainDark selection:!text-superDark selection:bg-superDuper/10 bg-offset dark:bg-offsetDark my-md relative flex flex-col rounded font-mono text-sm font-thin"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl sticky top-0 flex h-0 items-start justify-end"><button type="button" class="focus-visible:bg-offsetPlus dark:focus-visible:bg-offsetPlusDark hover:bg-offsetPlus text-textOff dark:text-textOffDark hover:text-textMain dark:hover:bg-offsetPlusDark  dark:hover:text-textMainDark font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-out font-sans  select-none items-center relative group/button  justify-center text-center items-center rounded-full cursor-pointer active:scale-[0.97] active:duration-150 active:ease-outExpo origin-center whitespace-nowrap inline-flex text-sm h-8 aspect-square"><div class="flex items-center min-w-0 font-medium gap-1.5 justify-center"><div class="flex shrink-0 items-center justify-center size-4"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="copy" class="svg-inline--fa fa-copy fa-fw fa-1x " role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M384 336l-192 0c-8.8 0-16-7.2-16-16l0-256c0-8.8 7.2-16 16-16l140.1 0L400 115.9 400 320c0 8.8-7.2 16-16 16zM192 384l192 0c35.3 0 64-28.7 64-64l0-204.1c0-12.7-5.1-24.9-14.1-33.9L366.1 14.1c-9-9-21.2-14.1-33.9-14.1L192 0c-35.3 0-64 28.7-64 64l0 256c0 35.3 28.7 64 64 64zM64 128c-35.3 0-64 28.7-64 64L0 448c0 35.3 28.7 64 64 64l192 0c35.3 0 64-28.7 64-64l0-32-48 0 0 32c0 8.8-7.2 16-16 16L64 464c-8.8 0-16-7.2-16-16l0-256c0-8.8 7.2-16 16-16l32 0 0-48-32 0z"></path></svg></div></div></button></div><div class="-mt-xl"><div><div class="text-text-200 bg-background-300 py-xs px-sm inline-block rounded-br rounded-tl-[3px] font-thin">cpp</div></div><div class="pr-lg"><span style="font-size: inherit; font-family: inherit; background: transparent; color: rgb(77, 77, 76); border-radius: 3px; display: flex; line-height: 1.42857; overflow-x: auto; white-space: pre;"><code style="white-space: pre-wrap; font-size: inherit; font-family: inherit; line-height: 1.66667; padding: 8px;"><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span class="token token macro property directive-hash">#</span><span class="token token macro property directive" style="color: rgb(137, 89, 168); font-weight: bolder;">include</span><span class="token token macro property"> </span><span class="token token macro property" style="color: rgb(113, 140, 0);">&lt;Servo.h&gt;</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;">
</span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span>Servo piernaIzquierda</span><span class="token token punctuation">;</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span>Servo piernaDerecha</span><span class="token token punctuation">;</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"></span></code></span></div></div></div></pre></div>
<ul class="marker:text-textOff list-disc">
<li>
<p class="my-0"><strong>Incluye</strong> la librería necesaria para controlar servos.</p>
</li>
<li>
<p class="my-0"><strong>Crea dos objetos</strong> para controlar cada pierna.</p>
</li>
</ul>

<h2 class="mb-xs mt-5 text-base font-[500] first:mt-0 dark:font-[475]">2. <strong>Definición de constantes y variables</strong></h2>
<div class="w-full md:max-w-[90vw]"><pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-textMainDark selection:!text-superDark selection:bg-superDuper/10 bg-offset dark:bg-offsetDark my-md relative flex flex-col rounded font-mono text-sm font-thin"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl sticky top-0 flex h-0 items-start justify-end"><button type="button" class="focus-visible:bg-offsetPlus dark:focus-visible:bg-offsetPlusDark hover:bg-offsetPlus text-textOff dark:text-textOffDark hover:text-textMain dark:hover:bg-offsetPlusDark  dark:hover:text-textMainDark font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-out font-sans  select-none items-center relative group/button  justify-center text-center items-center rounded-full cursor-pointer active:scale-[0.97] active:duration-150 active:ease-outExpo origin-center whitespace-nowrap inline-flex text-sm h-8 aspect-square"><div class="flex items-center min-w-0 font-medium gap-1.5 justify-center"><div class="flex shrink-0 items-center justify-center size-4"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="copy" class="svg-inline--fa fa-copy fa-fw fa-1x " role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M384 336l-192 0c-8.8 0-16-7.2-16-16l0-256c0-8.8 7.2-16 16-16l140.1 0L400 115.9 400 320c0 8.8-7.2 16-16 16zM192 384l192 0c35.3 0 64-28.7 64-64l0-204.1c0-12.7-5.1-24.9-14.1-33.9L366.1 14.1c-9-9-21.2-14.1-33.9-14.1L192 0c-35.3 0-64 28.7-64 64l0 256c0 35.3 28.7 64 64 64zM64 128c-35.3 0-64 28.7-64 64L0 448c0 35.3 28.7 64 64 64l192 0c35.3 0 64-28.7 64-64l0-32-48 0 0 32c0 8.8-7.2 16-16 16L64 464c-8.8 0-16-7.2-16-16l0-256c0-8.8 7.2-16 16-16l32 0 0-48-32 0z"></path></svg></div></div></button></div><div class="-mt-xl"><div><div class="text-text-200 bg-background-300 py-xs px-sm inline-block rounded-br rounded-tl-[3px] font-thin">cpp</div></div><div class="pr-lg"><span style="font-size: inherit; font-family: inherit; background: transparent; color: rgb(77, 77, 76); border-radius: 3px; display: flex; line-height: 1.42857; overflow-x: auto; white-space: pre;"><code style="white-space: pre-wrap; font-size: inherit; font-family: inherit; line-height: 1.66667; padding: 8px;"><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span class="token token" style="color: rgb(137, 89, 168); font-weight: bolder;">const</span><span> </span><span class="token token" style="color: rgb(137, 89, 168); font-weight: bolder;">int</span><span> CENTRO_IZQ </span><span class="token token operator">=</span><span> </span><span class="token token" style="color: rgb(245, 135, 31);">95</span><span class="token token punctuation">;</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span></span><span class="token token" style="color: rgb(137, 89, 168); font-weight: bolder;">const</span><span> </span><span class="token token" style="color: rgb(137, 89, 168); font-weight: bolder;">int</span><span> CENTRO_DER </span><span class="token token operator">=</span><span> </span><span class="token token" style="color: rgb(245, 135, 31);">95</span><span class="token token punctuation">;</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span></span><span class="token token" style="color: rgb(137, 89, 168); font-weight: bolder;">const</span><span> </span><span class="token token" style="color: rgb(137, 89, 168); font-weight: bolder;">int</span><span> AMPLITUD </span><span class="token token operator">=</span><span> </span><span class="token token" style="color: rgb(245, 135, 31);">15</span><span class="token token punctuation">;</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span></span><span class="token token" style="color: rgb(137, 89, 168); font-weight: bolder;">int</span><span> DURACION_PASO </span><span class="token token operator">=</span><span> </span><span class="token token" style="color: rgb(245, 135, 31);">1000</span><span class="token token punctuation">;</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span></span><span class="token token" style="color: rgb(137, 89, 168); font-weight: bolder;">int</span><span> pasos </span><span class="token token operator">=</span><span> </span><span class="token token" style="color: rgb(245, 135, 31);">100</span><span class="token token punctuation">;</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"></span></code></span></div></div></div></pre></div>
<ul class="marker:text-textOff list-disc">
<li>
<p class="my-0"><code>CENTRO_IZQ</code> y <code>CENTRO_DER</code>: Ángulos centrales de reposo de cada pierna.</p>
</li>
<li>
<p class="my-0"><code>AMPLITUD</code>: Cuánto se moverán los servos desde el centro (más amplitud = paso más largo).</p>
</li>
<li>
<p class="my-0"><code>DURACION_PASO</code>: Tiempo total de un ciclo de paso (ida y vuelta).</p>
</li>
<li>
<p class="my-0"><code>pasos</code>: Cantidad de pasos intermedios para suavizar el movimiento.</p>
</li>
</ul>

<h2 class="mb-xs mt-5 text-base font-[500] first:mt-0 dark:font-[475]">3. <strong>Configuración inicial (<code>setup</code>)</strong></h2>
<div class="w-full md:max-w-[90vw]"><pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-textMainDark selection:!text-superDark selection:bg-superDuper/10 bg-offset dark:bg-offsetDark my-md relative flex flex-col rounded font-mono text-sm font-thin"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl sticky top-0 flex h-0 items-start justify-end"><button type="button" class="focus-visible:bg-offsetPlus dark:focus-visible:bg-offsetPlusDark hover:bg-offsetPlus text-textOff dark:text-textOffDark hover:text-textMain dark:hover:bg-offsetPlusDark  dark:hover:text-textMainDark font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-out font-sans  select-none items-center relative group/button  justify-center text-center items-center rounded-full cursor-pointer active:scale-[0.97] active:duration-150 active:ease-outExpo origin-center whitespace-nowrap inline-flex text-sm h-8 aspect-square"><div class="flex items-center min-w-0 font-medium gap-1.5 justify-center"><div class="flex shrink-0 items-center justify-center size-4"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="copy" class="svg-inline--fa fa-copy fa-fw fa-1x " role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M384 336l-192 0c-8.8 0-16-7.2-16-16l0-256c0-8.8 7.2-16 16-16l140.1 0L400 115.9 400 320c0 8.8-7.2 16-16 16zM192 384l192 0c35.3 0 64-28.7 64-64l0-204.1c0-12.7-5.1-24.9-14.1-33.9L366.1 14.1c-9-9-21.2-14.1-33.9-14.1L192 0c-35.3 0-64 28.7-64 64l0 256c0 35.3 28.7 64 64 64zM64 128c-35.3 0-64 28.7-64 64L0 448c0 35.3 28.7 64 64 64l192 0c35.3 0 64-28.7 64-64l0-32-48 0 0 32c0 8.8-7.2 16-16 16L64 464c-8.8 0-16-7.2-16-16l0-256c0-8.8 7.2-16 16-16l32 0 0-48-32 0z"></path></svg></div></div></button></div><div class="-mt-xl"><div><div class="text-text-200 bg-background-300 py-xs px-sm inline-block rounded-br rounded-tl-[3px] font-thin">cpp</div></div><div class="pr-lg"><span style="font-size: inherit; font-family: inherit; background: transparent; color: rgb(77, 77, 76); border-radius: 3px; display: flex; line-height: 1.42857; overflow-x: auto; white-space: pre;"><code style="white-space: pre-wrap; font-size: inherit; font-family: inherit; line-height: 1.66667; padding: 8px;"><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span class="token token" style="color: rgb(137, 89, 168); font-weight: bolder;">void</span><span> </span><span class="token token" style="color: rgb(77, 77, 76);">setup</span><span class="token token punctuation">(</span><span class="token token punctuation">)</span><span> </span><span class="token token punctuation">{</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span>  piernaIzquierda</span><span class="token token punctuation">.</span><span class="token token" style="color: rgb(77, 77, 76);">attach</span><span class="token token punctuation">(</span><span class="token token" style="color: rgb(245, 135, 31);">10</span><span class="token token punctuation">)</span><span class="token token punctuation">;</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span>  piernaDerecha</span><span class="token token punctuation">.</span><span class="token token" style="color: rgb(77, 77, 76);">attach</span><span class="token token punctuation">(</span><span class="token token" style="color: rgb(245, 135, 31);">11</span><span class="token token punctuation">)</span><span class="token token punctuation">;</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span>  piernaIzquierda</span><span class="token token punctuation">.</span><span class="token token" style="color: rgb(77, 77, 76);">write</span><span class="token token punctuation">(</span><span>CENTRO_IZQ</span><span class="token token punctuation">)</span><span class="token token punctuation">;</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span>  piernaDerecha</span><span class="token token punctuation">.</span><span class="token token" style="color: rgb(77, 77, 76);">write</span><span class="token token punctuation">(</span><span>CENTRO_DER</span><span class="token token punctuation">)</span><span class="token token punctuation">;</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span>  </span><span class="token token" style="color: rgb(77, 77, 76);">delay</span><span class="token token punctuation">(</span><span class="token token" style="color: rgb(245, 135, 31);">1000</span><span class="token token punctuation">)</span><span class="token token punctuation">;</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span></span><span class="token token punctuation">}</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"></span></code></span></div></div></div></pre></div>
<ul class="marker:text-textOff list-disc">
<li>
<p class="my-0"><strong>Conecta</strong> los servos a los pines 10 y 11.</p>
</li>
<li>
<p class="my-0"><strong>Coloca</strong> ambos servos en la posición central.</p>
</li>
<li>
<p class="my-0"><strong>Espera</strong> 1 segundo antes de comenzar.</p>
</li>
</ul>

<h2 class="mb-xs mt-5 text-base font-[500] first:mt-0 dark:font-[475]">4. <strong>Bucle principal (<code>loop</code>)</strong></h2>
<div class="w-full md:max-w-[90vw]"><pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-textMainDark selection:!text-superDark selection:bg-superDuper/10 bg-offset dark:bg-offsetDark my-md relative flex flex-col rounded font-mono text-sm font-thin"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl sticky top-0 flex h-0 items-start justify-end"><button type="button" class="focus-visible:bg-offsetPlus dark:focus-visible:bg-offsetPlusDark hover:bg-offsetPlus text-textOff dark:text-textOffDark hover:text-textMain dark:hover:bg-offsetPlusDark  dark:hover:text-textMainDark font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-out font-sans  select-none items-center relative group/button  justify-center text-center items-center rounded-full cursor-pointer active:scale-[0.97] active:duration-150 active:ease-outExpo origin-center whitespace-nowrap inline-flex text-sm h-8 aspect-square"><div class="flex items-center min-w-0 font-medium gap-1.5 justify-center"><div class="flex shrink-0 items-center justify-center size-4"><svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="copy" class="svg-inline--fa fa-copy fa-fw fa-1x " role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M384 336l-192 0c-8.8 0-16-7.2-16-16l0-256c0-8.8 7.2-16 16-16l140.1 0L400 115.9 400 320c0 8.8-7.2 16-16 16zM192 384l192 0c35.3 0 64-28.7 64-64l0-204.1c0-12.7-5.1-24.9-14.1-33.9L366.1 14.1c-9-9-21.2-14.1-33.9-14.1L192 0c-35.3 0-64 28.7-64 64l0 256c0 35.3 28.7 64 64 64zM64 128c-35.3 0-64 28.7-64 64L0 448c0 35.3 28.7 64 64 64l192 0c35.3 0 64-28.7 64-64l0-32-48 0 0 32c0 8.8-7.2 16-16 16L64 464c-8.8 0-16-7.2-16-16l0-256c0-8.8 7.2-16 16-16l32 0 0-48-32 0z"></path></svg></div></div></button></div><div class="-mt-xl"><div><div class="text-text-200 bg-background-300 py-xs px-sm inline-block rounded-br rounded-tl-[3px] font-thin">cpp</div></div><div class="pr-lg"><span style="font-size: inherit; font-family: inherit; background: transparent; color: rgb(77, 77, 76); border-radius: 3px; display: flex; line-height: 1.42857; overflow-x: auto; white-space: pre;"><code style="white-space: pre-wrap; font-size: inherit; font-family: inherit; line-height: 1.66667; padding: 8px;"><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span class="token token" style="color: rgb(137, 89, 168); font-weight: bolder;">void</span><span> </span><span class="token token" style="color: rgb(77, 77, 76);">loop</span><span class="token token punctuation">(</span><span class="token token punctuation">)</span><span> </span><span class="token token punctuation">{</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span>  </span><span class="token token" style="color: rgb(137, 89, 168); font-weight: bolder;">for</span><span> </span><span class="token token punctuation">(</span><span class="token token" style="color: rgb(137, 89, 168); font-weight: bolder;">int</span><span> i </span><span class="token token operator">=</span><span> </span><span class="token token" style="color: rgb(245, 135, 31);">0</span><span class="token token punctuation">;</span><span> i </span><span class="token token operator">&lt;=</span><span> pasos</span><span class="token token punctuation">;</span><span> i</span><span class="token token operator">++</span><span class="token token punctuation">)</span><span> </span><span class="token token punctuation">{</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span>    </span><span class="token token" style="color: rgb(137, 89, 168); font-weight: bolder;">float</span><span> fase </span><span class="token token operator">=</span><span> </span><span class="token token" style="color: rgb(245, 135, 31);">2</span><span> </span><span class="token token operator">*</span><span> PI </span><span class="token token operator">*</span><span> i </span><span class="token token operator">/</span><span> pasos</span><span class="token token punctuation">;</span><span>  </span><span class="token token" style="color: rgb(142, 144, 140); font-family: inherit; font-style: italic;">// Avanza en un ciclo seno</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span>    </span><span class="token token" style="color: rgb(137, 89, 168); font-weight: bolder;">float</span><span> movIzq </span><span class="token token operator">=</span><span> </span><span class="token token" style="color: rgb(77, 77, 76);">sin</span><span class="token token punctuation">(</span><span>fase</span><span class="token token punctuation">)</span><span class="token token punctuation">;</span><span>         </span><span class="token token" style="color: rgb(142, 144, 140); font-family: inherit; font-style: italic;">// -1 a +1</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span>    </span><span class="token token" style="color: rgb(137, 89, 168); font-weight: bolder;">float</span><span> movDer </span><span class="token token operator">=</span><span> </span><span class="token token" style="color: rgb(77, 77, 76);">sin</span><span class="token token punctuation">(</span><span>fase </span><span class="token token operator">+</span><span> PI</span><span class="token token punctuation">)</span><span class="token token punctuation">;</span><span>    </span><span class="token token" style="color: rgb(142, 144, 140); font-family: inherit; font-style: italic;">// Desfase de 180°, pierna opuesta</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;">
</span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span>    </span><span class="token token" style="color: rgb(137, 89, 168); font-weight: bolder;">int</span><span> anguloIzq </span><span class="token token operator">=</span><span> </span><span class="token token" style="color: rgb(77, 77, 76);">constrain</span><span class="token token punctuation">(</span><span>CENTRO_IZQ </span><span class="token token operator">+</span><span> AMPLITUD </span><span class="token token operator">*</span><span> movIzq</span><span class="token token punctuation">,</span><span> </span><span class="token token" style="color: rgb(245, 135, 31);">0</span><span class="token token punctuation">,</span><span> </span><span class="token token" style="color: rgb(245, 135, 31);">180</span><span class="token token punctuation">)</span><span class="token token punctuation">;</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span>    </span><span class="token token" style="color: rgb(137, 89, 168); font-weight: bolder;">int</span><span> anguloDer </span><span class="token token operator">=</span><span> </span><span class="token token" style="color: rgb(77, 77, 76);">constrain</span><span class="token token punctuation">(</span><span>CENTRO_DER </span><span class="token token operator">-</span><span> AMPLITUD </span><span class="token token operator">*</span><span> movDer</span><span class="token token punctuation">,</span><span> </span><span class="token token" style="color: rgb(245, 135, 31);">0</span><span class="token token punctuation">,</span><span> </span><span class="token token" style="color: rgb(245, 135, 31);">180</span><span class="token token punctuation">)</span><span class="token token punctuation">;</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;">
</span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span>    piernaIzquierda</span><span class="token token punctuation">.</span><span class="token token" style="color: rgb(77, 77, 76);">write</span><span class="token token punctuation">(</span><span>anguloIzq</span><span class="token token punctuation">)</span><span class="token token punctuation">;</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span>    piernaDerecha</span><span class="token token punctuation">.</span><span class="token token" style="color: rgb(77, 77, 76);">write</span><span class="token token punctuation">(</span><span>anguloDer</span><span class="token token punctuation">)</span><span class="token token punctuation">;</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;">
</span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span>    </span><span class="token token" style="color: rgb(77, 77, 76);">delay</span><span class="token token punctuation">(</span><span>DURACION_PASO </span><span class="token token operator">/</span><span> pasos</span><span class="token token punctuation">)</span><span class="token token punctuation">;</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span>  </span><span class="token token punctuation">}</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"><span></span><span class="token token punctuation">}</span><span>
</span></span><span style="opacity: 1; font-size: inherit; line-height: 1.42857; color: rgb(77, 77, 76); background-color: transparent; flex-shrink: 0; padding: 8px; text-align: right; user-select: none;"></span></code></span></div></div></div></pre></div>
<h2 class="mb-xs mt-5 text-base font-[500] first:mt-0 dark:font-[475]">¿Qué hace este bucle?</h2>
<ul class="marker:text-textOff list-disc">
<li>
<p class="my-0"><strong>Recorre</strong> desde 0 hasta <code>pasos</code> (100), dividiendo el ciclo en pequeños movimientos suaves.</p>
</li>
<li>
<p class="my-0"><strong>Calcula la fase</strong> para cada paso usando la función seno, que genera un movimiento suave de ida y vuelta.</p>
</li>
<li>
<p class="my-0"><strong><code>movIzq</code></strong>: Movimiento de la pierna izquierda (oscila entre -1 y 1).</p>
</li>
<li>
<p class="my-0"><strong><code>movDer</code></strong>: Movimiento de la pierna derecha, pero desplazado 180° (desfasado, para que cuando una pierna va adelante la otra va atrás).</p>
</li>
<li>
<p class="my-0"><strong>Calcula los ángulos</strong> para cada servo sumando o restando la amplitud al centro, y los limita entre 0 y 180 grados.</p>
</li>
<li>
<p class="my-0"><strong>Mueve los servos</strong> a los ángulos calculados.</p>
</li>
<li>
<p class="my-0"><strong>Espera</strong> un pequeño intervalo antes de pasar al siguiente paso, para que el movimiento sea fluido.</p>
</li>
</ul>

<h2 class="mb-2 mt-6 text-lg font-[500] first:mt-0 dark:font-[475]" id=""><strong>Resumen Visual</strong></h2>
<ul class="marker:text-textOff list-disc">
<li>
<p class="my-0"><strong>Ambas piernas</strong> se mueven alternadamente, simulando el caminar.</p>
</li>
<li>
<p class="my-0"><strong>El movimiento es suave</strong> gracias al uso de la función seno.</p>
</li>
<li>
<p class="my-0"><strong>Puedes ajustar</strong> la velocidad (<code>DURACION_PASO</code>), la amplitud del paso (<code>AMPLITUD</code>), y la suavidad (<code>pasos</code>).</p>
</li>
</ul>

</div></div></div></div></div>
