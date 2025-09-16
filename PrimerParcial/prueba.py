import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Define the function f(x, y)
def f(x, y):
    return (x-5)**2+(y-5)**2

# Create a meshgrid for x and y values
x = np.linspace(-10, 5, 100)
y = np.linspace(-10, 5, 100)
X, Y = np.meshgrid(x, y)

# Calculate Z values based on the function f(x, y)
Z = f(X, Y)

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis') # 'viridis' is a colormap

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis (f(x,y))')
ax.set_title('3D Plot of f(x,y) = sin(sqrt(x^2 + y^2))')
plt.show()
