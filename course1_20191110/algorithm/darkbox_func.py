import numpy as np

def func1(x):
    # return 5 * x ** 2 + 3 * x + 2
    return np.sin(x * 10) + np.cos(np.sqrt(x * 5 + 2))

def get_samples(count = 10000):
    samples = []
    for _ in range(count):
        x = np.random.rand() * 10
        y = func1(x)
        samples.append([x, y])
    return samples