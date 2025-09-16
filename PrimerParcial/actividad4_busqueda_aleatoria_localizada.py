import numpy as np

def f(x) -> float:
    D = len(x)
    res = 0
    for i in range(D):
        res += (x[i]**4 - 16*x[i]**2 + 5*x[i])
    return res / D

def busquda_aleatoria_simple(x, K, mu, sigma):

    D = len(x)
    minimum = f(x)
    
    for e in range(K):
        # new = [x[_] + np.random.normal(mu, sigma) for _ in range(D)]
        new = [x[_] + np.random.normal(mu, sigma) for _ in range(D)]
        new_eval = f(new) 

        if new_eval < minimum:
            minimum = new_eval
            x = new

    return x, minimum

if __name__ == '__main__':

    # Define the amount of iterations and the dimension
    sigma = 1.8
    mu = 0
    K = 10000
    print(busquda_aleatoria_simple([4, 6.4], K, mu, sigma))
