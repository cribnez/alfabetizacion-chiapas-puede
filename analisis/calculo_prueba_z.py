import math

# --- DATOS DEL PROYECTO CHIAPAS PUEDE ---
n = 19          # Tamaño de la muestra
x = 13          # Éxitos (Certificados)
p = x / n       # Proporción observada (0.684)
p0 = 0.45       # Media histórica (45%)

print(f"Eficiencia Terminal: {p:.2%}")

# --- CÁLCULO DE LA PRUEBA Z ---
# Numerador: Diferencia de proporciones
numerador = p - p0

# Denominador: Error Estándar
error_estandar = math.sqrt((p0 * (1 - p0)) / n)

# Resultado Z
valor_z = numerador / error_estandar

print(f"Valor Z calculado: {valor_z:.2f}")

# --- CONCLUSIÓN ---
if valor_z > 1.96:
    print("Resultado: SIGNIFICATIVO (Se rechaza la hipótesis nula)")
else:
    print("Resultado: No significativo")
