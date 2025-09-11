import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def main(w : int):
    # Definir la función objetivo
    def f1(x1, x2):
        return w*(4 * x1**2 + 4 * x2**2) + (1-w)*((x1-5)**2 + (x2-5)**2) 

    # Definir las funciones de las restricciones
    def g1(x1, x2):
        return (x1 - 5)**2 + x2**2

    def g2(x1, x2):
        return (x1 - 8)**2 + (x2 + 3)**2


    # Crear una cuadrícula de valores para x1 y x2
    x1 = np.linspace(-10, 10, 400)
    x2 = np.linspace(-10, 10, 400)
    X1, X2 = np.meshgrid(x1, x2)

    # Evaluar la función objetivo en la cuadrícula
    Z_f1 = f1(X1, X2)

    # Evaluar las restricciones en la cuadrícula
    Z_g1 = g1(X1, X2)
    Z_g2 = g2(X1, X2)

    # Dibujar el gráfico de la función objetivo
    plt.figure(figsize=(8, 6))
    contour_f1 = plt.contour(X1, X2, Z_f1, levels=30, cmap=cm.Blues)
    plt.clabel(contour_f1, inline=1, fontsize=10)

    # Añadir la restricción g1 como una línea de contorno
    contour_g1 = plt.contour(X1, X2, Z_g1, levels=[25], colors='red')
    plt.clabel(contour_g1, inline=1, fontsize=10, fmt="g1 ≤ 25")

    # Añadir la restricción g2 como una línea de contorno
    contour_g2 = plt.contour(X1, X2, Z_g2, levels=[7.7], colors='green')
    plt.clabel(contour_g2, inline=1, fontsize=10, fmt="g2 ≥ 7.7")

    # ➕ Añadir líneas para las restricciones x1 <= 5 y x2 <= 3
    plt.axvline(x=5, color='purple')
    plt.axhline(y=3, color='orange')

    # Limitar los ejes a las restricciones 0 <= x1 <= 5 y 0 <= x2 <= 3
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    # Etiquetas de los ejes y título
    plt.xlabel(r'$x_1$')
    plt.ylabel(r'$x_2$')
    #plt.title(r'$f_1(x_1, x_2) = 4x_1^2 + 4x_2^2$')

    # Mostrar el gráfico
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    W = np.linspace(0, 1, 10)
    for w in W:
        main(w)