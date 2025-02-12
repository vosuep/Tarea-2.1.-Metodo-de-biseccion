import numpy as np
import matplotlib.pyplot as plt

# Definir la función f(x) = cos(x) - x
def f(x):
    return np.cos(x) - x

# Método de Bisección
def biseccion(a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        print("El método de bisección no es aplicable en el intervalo dado.")
        return None
    
    iteraciones = []
    a_vals = []
    b_vals = []
    c_vals = []
    fc_vals = []
    errores_abs = []
    errores_rel = []
    errores_cuad = []
    
    c_old = a  # Para calcular errores
    
    for i in range(max_iter):
        c = (a + b) / 2
        iteraciones.append(i + 1)
        a_vals.append(a)
        b_vals.append(b)
        c_vals.append(c)
        fc_vals.append(f(c))
        
        error_abs = abs(c - c_old)
        errores_abs.append(error_abs)
        
        error_rel = error_abs / abs(c) if c != 0 else 0
        errores_rel.append(error_rel)
        
        error_cuad = error_abs ** 2
        errores_cuad.append(error_cuad)
        
        if abs(f(c)) < tol or error_abs < tol:
            break
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        c_old = c
    
    return iteraciones, a_vals, b_vals, c_vals, fc_vals, errores_abs, errores_rel, errores_cuad

# Parámetros iniciales
a, b = 0, 1
resultados = biseccion(a, b)

# Extraer resultados
iteraciones, a_vals, b_vals, c_vals, fc_vals, errores_abs, errores_rel, errores_cuad = resultados

# Crear figura con gráficos
fig, ax = plt.subplots(1, 2, figsize=(14, 5))

# Gráfica de la función y convergencia de iteraciones
x = np.linspace(a, b, 400)
y = f(x)
ax[0].plot(x, y, label=r'$f(x) = \cos(x) - x$', color='b')
ax[0].axhline(0, color='k', linestyle='--', linewidth=1)
ax[0].scatter(c_vals, [f(c) for c in c_vals], color='red', label='Iteraciones')
ax[0].set_xlabel('x')
ax[0].set_ylabel('f(x)')
ax[0].set_title("Convergencia del Método de Bisección")
ax[0].legend()
ax[0].grid()

# Gráfica del error absoluto
ax[1].plot(range(1, len(errores_abs) + 1), errores_abs, marker='o', linestyle='-', color='r')
ax[1].set_yscale("log")
ax[1].set_xlabel("Iteración")
ax[1].set_ylabel("Error Absoluto")
ax[1].set_title("Error Absoluto en cada Iteración")
ax[1].grid()

plt.show()

# Crear tabla con Matplotlib
fig, ax = plt.subplots(figsize=(8, 6))
ax.axis('tight')
ax.axis('off')

tabla_data = list(zip(iteraciones, a_vals, b_vals, c_vals, fc_vals, errores_abs, errores_rel, errores_cuad))
columnas = ["Iter", "a", "b", "c", "f(c)", "Error Abs", "Error Rel", "Error Cuad"]

tabla = ax.table(cellText=tabla_data, colLabels=columnas, cellLoc='center', loc='center')
tabla.auto_set_font_size(False)
tabla.set_fontsize(8)
tabla.auto_set_column_width([0,1,2,3,4,5,6,7])

plt.show()
