import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple


############# Define functions and restrictions #############
# Function number 1
def f1(x : int, y : int) -> int:
    # Define the output for the funciton
    return 4*x**2 + 4*y**2

# Function number 2
def f2(x : int, y : int) -> int:
    # Define the output for the funciton
    return (x-5)**2 + (y-5)**2

# Restriction number 1
def g1(x : int, y : int) -> bool:
    # Return if the point is inside the restriction
    return (x-5)**2 + y**2 <= 25

# Restriction number 2
def g2(x : int, y : int) -> bool:
    # Return if the point is inside the restriction
    return (x-8)**2 + (y+3)**2 >= 7.7

# Restiction number 3
def g3(x : int, y : int) -> bool:
    # REturn if the point is inside the restiction
    return (x >= 0 and x <= 5)

# Restiction number 4
def g4(x : int, y : int) -> bool:
    # REturn if the point is inside the restiction
    return (y >= 0 and y <= 3)

def is_inside(x : int, y : int) -> bool:
    return (g1(x, y) and g2(x, y) and g3(x, y) and g4(x, y))

def convex_combination(x : int, y : int, w : int) -> int:
    # Return the convex combination of the funcitons
    return w * f1(x, y) + (1 - w) * f2(x, y) 

############# UMDA #############

############# Variables #############
"""
l1 : limit inferior to the original search
l2 : limit superior to the original search
pop : number of populations
n : size of population
m : size of best population
"""
l1 = -20
l2 = 20
pop = 100
n = 100
m = n // 2

############# Procedure #############
def UMDA(w : int) -> Tuple[int, int, int]:

    x = 1000000
    y = 1000000
    min = 1000000

    # Initial position
    population = [[0, 0, 0] for _ in range(n)]
    for e in population:
        while True:
            e[1] = np.random.uniform(l1, l2)
            e[2] = np.random.uniform(l1, l2)

            if is_inside(e[1], e[2]):
                break
        e[0] = convex_combination(e[1], e[2], w)

    population = sorted(population)
    if min > population[0][0]:
        min, x, y = population[0]
    
    # Create new populations
    for _ in range(pop):

        # Calculate the current mean 
        meanx = 0
        meany = 0

        for i in range(m):
            e = population[i]
            meanx += e[1]
            meany += e[2]

        meanx /= m
        meany /= m

        # Calculate the current mean deviation
        sigmax = 0
        sigmay = 0

        for i in range(m):
            e = population[i]
            sigmax += (meanx - e[1])**2
            sigmay += (meany - e[2])**2

        sigmax /= (m-1)
        sigmay /= (m-1)

        sigmax = np.sqrt(sigmax)
        sigmay = np.sqrt(sigmay)

        # Calculate the new generation
        for e in population:
            while True:
                e[1] = np.random.normal(meanx, sigmax)
                e[2] = np.random.normal(meany, sigmay)

                if is_inside(e[1], e[2]):
                    break
                    
            e[0] = convex_combination(e[1], e[2], w)

        # Sort the population
        population = sorted(population)

        # Compare with the minimum
        if e[0] < min:
            min = e[0]
            x = e[1]
            y = e[2]

    return min, x, y


############# Program #############
W = np.linspace(0, 1, 10)

X = []
Y = []
for w in W:

    min = 1000000
    x = 0
    y = 0
    
    for _ in range(10):
        MIN, xx, yy = UMDA(w)
        if(MIN < min):
            x = xx
            y = yy
            min = MIN
            
    X.append(x)
    Y.append(y)

# Create elements for the plot
fig, ax = plt.subplots()

ax.plot(X, Y)

plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.show()

