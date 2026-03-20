# 📊 Evaluación de Impacto: Proyecto "Chiapas Puede"

![Estado](https://img.shields.io/badge/Estado-Completado-success)
![Enfoque](https://img.shields.io/badge/Enfoque-Desescolarizado-blue)
![Región](https://img.shields.io/badge/Región-Chiapas%2C%20México-orange)

**Ubicación:** Micro-región Tuxtla Gutiérrez Oriente  
**Modalidad:** Células de Alfabetización (Desescolarizada / Domiciliaria / Modelo Matías de Córdova)

Este repositorio contiene el libro de datos crudos, las fórmulas estadísticas y las métricas de impacto socioeconómico que sustentan la investigación: **"Desescolarizar para alfabetizar"**. El objetivo es transparentar la metodología utilizada para evaluar la eficiencia de la educación para adultos en periferias urbanas.

---

## 1. 📈 Datos de la Muestra y Eficiencia Terminal

Se midió la eficiencia terminal de la Célula de Alfabetización y se realizó un desglose por sexo para contrastar la hipótesis de la "brecha cognitiva".

| Métrica | Datos | Porcentaje |
| :--- | :---: | :---: |
| **Población Total (N)** | 19 educandos | 100% |
| **Total de Egresados** | 13 educandos | **68.4%** |

### Desglose por Género
*(Nota metodológica: No existe evidencia estadística de una brecha cognitiva cuando se eliminan las barreras logísticas y de tiempo).*

| Género | Inscritos | Aprobados | Tasa de Éxito |
| :--- | :---: | :---: | :---: |
| **Mujeres** | 11 | 7 | **63.6%** |
| **Hombres** | 8 | 6 | **75.0%** |

*(Aquí te sugiero insertar la imagen: `![Gráfica de Equidad de Género](ruta/de/tu/imagen.png)`)*

---

## 2. 🧮 Prueba de Significancia Estadística (Prueba Z)

Para demostrar que el **68.4%** de retención representa una mejora real frente a los modelos tradicionales, se aplicó una **Prueba Z para una proporción poblacional**.

**Variables del Modelo:**
* `n` (Tamaño de muestra) = 19
* `x` (Casos de éxito) = 13
* `p` (Proporción obtenida) = 0.684
* `P_0` (Media histórica en zonas marginadas) = 0.45 (45%)
* `α` (Nivel de significancia) = 0.05 (Confianza del 95%)

**Desarrollo de la Fórmula (Z):**
1. Diferencia de proporciones (Numerador): `0.684 - 0.45 = 0.234`
2. Error estándar (Denominador): `√((0.45 * 0.55) / 19) = 0.1141`
3. Resultado (Z): `0.234 / 0.1141 = 2.0508`

> **Conclusión Estadística:** **Z = 2.05**. Dado que el valor calculado (2.05) es mayor que el valor crítico (1.96) y $p < 0.05$, se rechaza la hipótesis nula. **El modelo domiciliario mejora significativamente la retención escolar.**

![Comparativa de Eficiencia](instrumentos/grafica_z.png)

---

## 3. 💰 Impacto Socioeconómico: Ahorro y "Pobreza de Tiempo"

La deserción en la alfabetización urbana no es un fenómeno cognitivo, sino logístico. El modelo domiciliario generó ahorros directos (costo de oportunidad) al transitar de un sistema de "Plaza Comunitaria" a uno "Desescolarizado".

### A. Beneficio Económico Directo
* **Costo de transporte evitado:** $48.00 MXN / sesión *(Basado en 2 pasajes de ida y 2 de vuelta por transbordos/acompañante).*
* **Frecuencia:** 3 sesiones semanales.
* 💵 **Ahorro Semanal Total:** **$144.00 MXN** por educando.

### B. Mitigación de la "Pobreza de Tiempo"
Medición del tiempo recuperado, el cual las mujeres (principalmente jefas de familia) pudieron reinvertir en la economía de cuidado, descanso o estudio autónomo.
* **Tiempo de traslado evitado:** 90 minutos por sesión *(45 min ida + 45 min regreso).*
* **Frecuencia:** 3 sesiones semanales.
* **Cálculo:** 90 mins × 3 = 270 minutos semanales.
* ⏱️ **Tiempo Recuperado:** **4.5 horas semanales** por educando.

*(Aquí te sugiero insertar la infografía de impacto: `![Infografía 4.5 horas y 144 MXN](ruta/de/tu/imagen3.png)`)*
