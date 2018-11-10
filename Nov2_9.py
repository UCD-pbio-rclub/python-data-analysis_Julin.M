# intro

import numpy as np

my_arr = np.arange(1000000)

my_list = list(range(1000000))

%time for _ in range(10): my_arr2 = my_arr*2

%time for _ in range(10): my_list2 = my_list*2

# 4.1 ndaarrays

data = np.random.randn(2, 3)

data

data * 10
data + data


# ndarrays are for a single data type

data.shape

data.dtype

# np.meshgrid

points = np.array(range(5))

points

xs, ys = np.meshgrid(points, points)

xs

ys

points2 = np.array(range(7,9))

xs, ys = np.meshgrid(points,points2)

xs

ys




