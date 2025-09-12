import numpy as np
import matplotlib.pyplot as plt

############### Section for functions ###############
# Function to optimize
def f(x):
    return 0.5*((x[0]**4-16*x[0]**2+5*x[0]) + (x[1]**4-16*x[1]**2+5*x[1]))

# Restriction 1
def g1(x):
    return (x[0] >= -8) & (x[0] <= 8)

# Restriction 2
def g2(x):
    return (x[1] >= -8) & (x[1] <= 8)

############### Plot function  ###############
def plot(points):
   
   # Create a grid to evaluate
    x = np.linspace(-8, 8, 200)
    y = np.linspace(-8, 8, 200)
    X, Y = np.meshgrid(x, y)

    # Evaluate the grid
    Z = f(np.array([X, Y]))
    G1 = ((X >= -8) & (X <= 8)).astype(int)
    G2 = ((Y >= -8) & (Y <= 8)).astype(int) 

    # Evalation of the function f
    plt.figure(figsize=(8,8))
    contours = plt.contour(X, Y, Z, levels=30, colors='black')
    plt.clabel(contours, inline=True, fontsize=8)

    # Contour for restrictions
    plt.contourf(X, Y, G1, levels=[0, G1.max()], colors=['red'], alpha=0.2)
    plt.contourf(X, Y, G2, levels=[0, G2.max()], colors=['blue'], alpha=0.2)

    points = np.array(points)
    plt.scatter(points[:,0], points[:,1], color='white', edgecolor='black', s=50, label='Puntos')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Curvas de nivel con restricciones y puntos')
    plt.legend()
    plt.grid(True)
    plt.savefig("grafico.png")

############### Optimization function  ###############
def random_localized_search(K, x):
    
    
    D = 2
    minimum = f(x)
    points = [x]

    for _ in range(K):
        new = [np.random.uniform(-8, 8) for __ in range(D)]
        new_eval = f(new)

        if new_eval < minimum:
            minimum = new_eval
            x = new
            points.append(x)

    return x, minimum, points

############### Main ###############
if __name__ == "__main__":
    
    # Define the amount of iterations and the dimension
    K = 1000

    x, minimum, points = random_localized_search(K, [4, 6.4])
    print(x, minimum)
    plot(points)

