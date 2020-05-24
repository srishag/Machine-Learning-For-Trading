"""Array attributes."""
import numpy as np


def test_run():
    a = np.random.random((5, 4, 3))  # 5x4x3 array of random numbers
    print(a)

    print(a.shape)

    print(a.shape[0])  # returns number of rows
    print(a.shape[1])  # returns number of columns

    print(len(a.shape))  # returns the dimension of the array

    print(a.size)  # returns number of elements in array

    print(a.dtype)  # returns data type of elements


if __name__ == "__main__":
    test_run()
