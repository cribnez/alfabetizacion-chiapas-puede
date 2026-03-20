# 📊 Libro de Datos y Cálculos: Proyecto "Chiapas Puede"
**Ubicación:** Micro-región Tuxtla Gutiérrez Oriente
**Modalidad:** Células de Alfabetización (Desescolarizada / Domiciliaria)

Este documento detalla los datos crudos y las fórmulas utilizadas para obtener las métricas de eficiencia, impacto económico y significancia estadística presentadas en la investigación.

---

## 1. Datos de la Muestra y Eficiencia (El origen del 68.4%)
Se midió la eficiencia terminal de la Célula de Alfabetización y se realizó un desglose por sexo para contrastar la hipótesis de la "brecha cognitiva".

* **Población Total (N):** 19 educandos inscritos.
* **Total de Egresados (Certificados):** 13 educandos.
* **Eficiencia General:** 13 ÷ 19 = `0.6842` (**68.4%**)

### Desglose por Género
* **Mujeres inscritas:** 11 mujeres
  * *Mujeres que aprobaron:* 7 mujeres
  * *Tasa de éxito femenino:* 7 ÷ 11 = **63.6%**
* **Hombres inscritos:** 8 hombres
  * *Hombres que aprobaron:* 6 hombres
  * *Tasa de éxito masculino:* 6 ÷ 8 = **75.0%**

*(Nota metodológica: Las tasas se consideran equiparables debido al tamaño de la muestra; no existe evidencia estadística de una brecha cognitiva cuando se eliminan las barreras de tiempo).*

---

## 2. Prueba de Significancia Estadística (Prueba Z)
Para demostrar que el 68.4% de retención representa una mejora real frente a los modelos tradicionales, se aplicó una Prueba Z para una proporción poblacional.

**Variables del Modelo:**
* `n` (Tamaño de muestra): 19
* `x` (Casos de éxito): 13
* `p` (Proporción obtenida): 0.684
* `P_0` (Media histórica de contraste en zonas marginadas): 0.45 (45%)
* `α` (Nivel de significancia): 0.05 (Confianza del 95%)

**Cálculo (Fórmula Z):**
* Diferencia de proporciones (Numerador): `0.684 - 0.45 = 0.234`
* Error estándar (Denominador): `√((0.45 * 0.55) / 19) = 0.1141`
* Resultado (Z): `0.234 / 0.1141 = 2.0508`

**Resultado Final:** **Z = 2.05** (Dado que 2.05 > 1.96 y p < 0.05, se rechaza la hipótesis nula. El modelo domiciliario mejora significativamente la retención escolar).

---

## 3. Datos Económicos (El origen de los $144.00 MXN)
Cálculo del ahorro directo o "costo de oportunidad" para los educandos al transitar de un modelo de Plaza Comunitaria al modelo domiciliario.

* **Costo de transporte por sesión:** **$48.00 MXN** *(Basado en 2 pasajes de ida y 2 de vuelta por transbordos/acompañante en zonas periféricas).*
* **Frecuencia de estudio:** 3 sesiones por semana.
* **Ahorro Semanal Total:** $48.00 × 3 = **$144.00 MXN**

---

## 4. Pobreza de Tiempo (El origen de las 4.5 horas)
Medición del tiempo recuperado que las mujeres pudieron reinvertir en la economía de cuidado, descanso o estudio autónomo.

* **Tiempo de traslado evitado:** 90 minutos promedio por sesión *(45 min de ida a la plaza comunitaria + 45 min de regreso).*
* **Frecuencia de estudio:** 3 sesiones por semana.
* **Cálculo en minutos:** 90 mins × 3 = 270 minutos semanales.
* **Ahorro Semanal en Horas:** 270 ÷ 60 = **4.5 horas recuperadas**.
