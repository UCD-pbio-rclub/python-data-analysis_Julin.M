print('hello world')

import numpy as np

data = {i: np.random.randn() for i in range()}

data

a = np.random.randn(100, 100)


%timeit np.dot(a, a)

%matplotlib inline

import matplotlib.pyplot as plt

plt.plot(np.random.randn(50).cumsum())

%magic

%debug