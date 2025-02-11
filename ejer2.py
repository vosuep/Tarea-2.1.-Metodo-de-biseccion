import numpy as np
import matplotlib.pyplot as plt

# Definir la función

def f(x):
    return np.exp(-x) - x

# Algoritmo del Método de Bisección

def biseccion(a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        print("El método de bisección no es aplicable en el intervalo dado.")
        return None
    
    iteraciones = []
    errores_abs = []
    errores_rel = []
    errores_cuad = []
    c_old = a  # Para calcular errores

    print("\nIteraciones del Método de Bisección:")
    print("Iter |       a       |       b       |       c       |      f(c)      |     Error Abs     |     Error Rel     |    Error Cuadrático")
    print("-" * 130)

    for i in range(max_iter):
        c = (a + b) / 2
        iteraciones.append(c)
        
        error_abs = abs(c - c_old)
        error_rel = error_abs / abs(c) if c != 0 else 0
        error_cuad = error_abs ** 2
        
        errores_abs.append(error_abs)
        errores_rel.append(error_rel)
        errores_cuad.append(error_cuad)

        print(f"{i+1:4d} | {a:.8f} | {b:.8f} | {c:.8f} | {f(c):.8e} | {error_abs:.8e} | {error_rel:.8e} | {error_cuad:.8e}")

        if abs(f(c)) < tol or error_abs < tol:
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        c_old = c

    return iteraciones, errores_abs, errores_rel, errores_cuad

# Intervalo inicial y tolerancia
a, b = 0, 1
iteraciones, errores_abs, errores_rel, errores_cuad = biseccion(a, b)

# Visualización con matplotlib
fig, ax = plt.subplots(1, 2, figsize=(14, 5))

# Gráfica de la función y la convergencia de iteraciones
x = np.linspace(a - 0.5, b + 0.5, 400)
y = f(x)
ax[0].plot(x, y, label=r'$f(x) = e^{-x} - x$', color='b')
ax[0].axhline(0, color='k', linestyle='--', linewidth=1)
ax[0].scatter(iteraciones, [f(c) for c in iteraciones], color='red', label='Iteraciones')
ax[0].set_xlabel('x')
ax[0].set_ylabel('f(x)')
ax[0].set_title("Convergencia del Método de Bisección")
ax[0].legend()
ax[0].grid()

# Gráfica de convergencia del error
ax[1].plot(range(1, len(errores_abs)+1), errores_abs, marker='o', linestyle='-', color='r', label="Error Absoluto")
ax[1].plot(range(1, len(errores_rel)+1), errores_rel, marker='s', linestyle='-', color='g', label="Error Relativo")
ax[1].plot(range(1, len(errores_cuad)+1), errores_cuad, marker='d', linestyle='-', color='b', label="Error Cuadrático")
ax[1].set_yscale("log")
ax[1].set_xlabel("Iteración")
ax[1].set_ylabel("Error")
ax[1].set_title("Errores en cada Iteración")
ax[1].legend()
ax[1].grid()

plt.savefig("biseccion_exp.png", dpi=300)
plt.show()
