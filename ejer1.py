import numpy as np
import matplotlib.pyplot as plt

# Definir la función a evaluar
def f(x):
    return x**3 - 4*x - 9

# Implementación del método de bisección con errores absoluto, relativo y cuadrático
def biseccion(a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        print("El método de bisección no es aplicable en el intervalo dado.")
        return None
    
    iteraciones = []
    errores_abs = []
    errores_rel = []
    errores_cuad = []
    datos_tabla = []
    c_old = a  # Para calcular errores

    print("\nIteraciones del Método de Bisección:")
    print("Iter |       a       |       b       |       c       |      f(c)      |  Error Abs  |  Error Rel  |  Error Cuad")
    print("-" * 120)

    for i in range(max_iter):
        c = (a + b) / 2
        iteraciones.append(c)

        error_abs = abs(c - c_old)
        error_rel = error_abs / abs(c) if c != 0 else 0
        error_cuad = error_abs ** 2

        errores_abs.append(error_abs)
        errores_rel.append(error_rel)
        errores_cuad.append(error_cuad)

        print(f"{i+1:4d} | {a:.8f} | {b:.8f} | {c:.8f} | {f(c):.8f} | {error_abs:.8e} | {error_rel:.8e} | {error_cuad:.8e}")
        
        # Guardar datos para la tabla
        datos_tabla.append([i+1, a, b, c, f(c), error_abs, error_rel, error_cuad])

        if abs(f(c)) < tol or error_abs < tol:
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        c_old = c

    return iteraciones, errores_abs, errores_rel, errores_cuad, datos_tabla

# Parámetros iniciales
a, b = 2, 3
tolerancia = 1e-5

# Ejecutar el método de bisección
iteraciones, errores_abs, errores_rel, errores_cuad, datos_tabla = biseccion(a, b, tolerancia)

# Crear figura para la tabla
fig, ax = plt.subplots(figsize=(12, 6))
ax.axis('tight')
ax.axis('off')
columnas = ["Iteración", "a", "b", "c", "f(c)", "Error Abs", "Error Rel", "Error Cuad"]
tabla = ax.table(cellText=datos_tabla, colLabels=columnas, cellLoc='center', loc='center')
tabla.auto_set_font_size(False)
tabla.set_fontsize(9)
tabla.scale(1.2, 1.2)

plt.title("Iteraciones del Método de Bisección")
plt.show()

# Gráficas de convergencia de errores
fig, ax = plt.subplots(1, 2, figsize=(14, 5))

# Gráfica de convergencia del error absoluto
ax[0].plot(range(1, len(errores_abs)+1), errores_abs, marker='o', linestyle='-', color='b', label="Error Absoluto")
ax[0].set_yscale("log")  # Escala logarítmica
ax[0].set_xlabel("Iteración")
ax[0].set_ylabel("Error Absoluto")
ax[0].set_title("Convergencia del Error Absoluto")
ax[0].grid()
ax[0].legend()

# Gráfica de convergencia del error relativo y cuadrático
ax[1].plot(range(1, len(errores_rel)+1), errores_rel, marker='s', linestyle='-', color='r', label="Error Relativo")
ax[1].plot(range(1, len(errores_cuad)+1), errores_cuad, marker='^', linestyle='-', color='g', label="Error Cuadrático")
ax[1].set_yscale("log")  # Escala logarítmica
ax[1].set_xlabel("Iteración")
ax[1].set_ylabel("Errores")
ax[1].set_title("Convergencia de Errores Relativo y Cuadrático")
ax[1].grid()
ax[1].legend()

# Mostrar gráficas
plt.show()
