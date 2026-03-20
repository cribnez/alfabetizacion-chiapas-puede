import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# --- DATOS DEL PROYECTO CHIAPAS PUEDE ---
n = 19          # Tamaño de la muestra
x = 13          # Éxitos (Certificados)
p_obs = x / n   # Proporción observada (0.684)
p0 = 0.45       # Media histórica de contraste (45%)
alfa = 0.05     # Nivel de significancia (95% confianza)

print(f"Eficiencia Terminal Observada: {p_obs:.2%}")

# --- CÁLCULO DE LA PRUEBA Z ---
numerador = p_obs - p0
error_estandar = math.sqrt((p0 * (1 - p0)) / n)
valor_z_calc = numerador / error_estandar

print(f"Valor Z calculado: {valor_z_calc:.2f}")

# --- GENERACIÓN DE LA GRÁFICA DE DISTRIBUCIÓN NORMAL ---
# 1. Definir el rango del eje X (de -4 a 4 desviaciones estándar)
x_axis = np.arange(-4, 4, 0.001)

# 2. Calcular la distribución normal estándar (media=0, sd=1)
y_axis = norm.pdf(x_axis, 0, 1)

# 3. Configurar la gráfica
plt.figure(figsize=(10, 6))
plt.plot(x_axis, y_axis, label='Distribución Normal Estándar', color='blue', lw=2)

# 4. Sombrear la zona de rechazo (alfa = 0.05, dos colas)
z_critico = norm.ppf(1 - alfa/2) # Aproximadamente 1.96
plt.fill_between(x_axis, y_axis, where=(x_axis >= z_critico), color='red', alpha=0.3, label='Zona de Rechazo (alfa=0.05)')
plt.fill_between(x_axis, y_axis, where=(x_axis <= -z_critico), color='red', alpha=0.3)

# 5. Marcar tu Valor Z Calculado (2.05)
plt.axvline(x=valor_z_calc, color='green', linestyle='--', lw=2, label=f'Z Calculado = {valor_z_calc:.2f}')
plt.scatter(valor_z_calc, norm.pdf(valor_z_calc, 0, 1), color='green', s=100, zorder=5)

# 6. Anotaciones y etiquetas
plt.title('Prueba Z: Eficiencia Terminal - Proyecto Chiapas Puede', fontsize=14, fontweight='bold')
plt.xlabel('Desviaciones Estándar (Z-Score)', fontsize=12)
plt.ylabel('Densidad de Probabilidad', fontsize=12)
plt.axhline(0, color='black',lw=1)
plt.legend(loc='upper left')
plt.grid(axis='x', linestyle='--', alpha=0.5)

# 7. Guardar la imagen
# Nota: En GitHub esto no mostrará la gráfica, pero si corres el script localmente, guardará el archivo.
plt.savefig('grafica_prueba_z_chiapas.png', dpi=300)
print("Gráfica generada y guardada como 'grafica_prueba_z_chiapas.png'")

# plt.show() # Descomenta esta línea si lo corres en tu computadora para verla.
