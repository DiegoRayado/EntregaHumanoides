#include <Servo.h>

Servo piernaIzquierda;
Servo piernaDerecha;

const int CENTRO_IZQ = 95;
const int CENTRO_DER = 95;
const int AMPLITUD = 15; // Mayor amplitud

// Duración total de un ciclo completo (ida y vuelta de ambas piernas)
int DURACION_PASO = 1000; // Más rápido, 1 segundo por ciclo
int pasos = 100;          // Menos pasos para mantener suavidad

void setup() {
  piernaIzquierda.attach(10);
  piernaDerecha.attach(11);
  piernaIzquierda.write(CENTRO_IZQ);
  piernaDerecha.write(CENTRO_DER);
  delay(1000);
}

void loop() {
  for (int i = 0; i <= pasos; i++) {
    float fase = 2 * PI * i / pasos;  // Avanza en un ciclo seno
    float movIzq = sin(fase);         // -1 a +1
    float movDer = sin(fase + PI);    // Desfase de 180°, pierna opuesta

    int anguloIzq = constrain(CENTRO_IZQ + AMPLITUD * movIzq, 0, 180);
    int anguloDer = constrain(CENTRO_DER - AMPLITUD * movDer, 0, 180);

    piernaIzquierda.write(anguloIzq);
    piernaDerecha.write(anguloDer);

    delay(DURACION_PASO / pasos);
  }
}
