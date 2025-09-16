import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Function number 1
def f1(x : int) -> int:
    # Define the output for the function
    return x ** 2

# Function number 2
def f2(x : int) -> int:
    # Define the output for the function
    return (x - 2) ** 2

# Create the domains for each funcion
dominio_f1 = np.linspace(-10, 10, 100)
dominio_f2 = np.linspace(-10, 10, 100)

# Create elements for the plot
fig, ax = plt.subplots()

# Total of points
N = 100

# Generate all the points for the convex combination
W = np.linspace(0, 1, N)

# For a given w, get the domain value that minimizes the convex combination 
X = np.zeros(N)

i = 0
for w in W:

    # Make the convex combination for the function
    def convex_combination(x):
        return w*f1(x)+(1-w)*f2(x)
    
    X[i] = float(minimize(convex_combination, x0=0).x[0])
    #ax.plot(dominio_f1, w*f1(dominio_f1) + (1-w)*f2(dominio_f1), color = (1 * w, 1 * (1 - w), 0, 0.3))

    i += 1

print(X)
image_f1_with_minimums = f1(X)
image_f2_with_minimums = f2(X)

ax.plot(image_f1_with_minimums, image_f2_with_minimums)

plt.xlim(-5, 5)
plt.ylim(-1, 15)
plt.show()
