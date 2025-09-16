import numpy as np

# B : bias
# D : random movement

def f(x) -> float:
    D = len(x)
    res = 0
    for i in range(D):
        res += (x[i]**4 - 16*x[i]**2 + 5*x[i])
    return res / D

def inside(x):
    l1 = -8
    l2 = 8

    res = True
    for e in x:
        res = res and e <= l2 and e >= l1

    return res

def busquda_aleatoria_simple(x, K, mu, sigma, B):

    D = len(x)
    minimum = f(x)
    
    for e in range(K):

        fx = f(x)

        # Try moving in the bias direction
        movement = [np.random.normal(mu, sigma) for _ in range(D)]
        new = [movement[e] + x[e] + B[e] for e in range(D)]
        new_eval = f(new) 

        # Verify if is less than the actual position
        if inside(new) and new_eval < fx:
            x = new
            B = [0.2*B[e] + 0.4*movement[e] for e in range(D)]
            minimum = new_eval
            continue

        # Try moving to the other side
        new = [-movement[e] + x[e] + B[e] for e in range(D)]
        new_eval = f(new)

        # Verify if is less than the actual position
        if inside(new) and new_eval < fx:
            x = new
            B = [B[e] - 0.4*movement[e] for e in range(D)]
            minimum = new_eval
            continue

        B = [0.5 * B[e] for e in range(D)]   

    return x, minimum

if __name__ == '__main__':

    # Define the amount of iterations and the dimension
    sigma = 1.8
    mu = 0
    B = [0, 0]
    K = 10000
    print(busquda_aleatoria_simple([4, 6.4], K, mu, sigma, B))
