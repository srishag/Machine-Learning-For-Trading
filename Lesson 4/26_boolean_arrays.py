"""Accessing elements."""
import numpy as np


def test_run():
    a = np.array([(20, 25, 10, 23, 26, 32, 10, 5, 0),
                  (0, 2, 50, 20, 0, 1, 28, 5, 0)])
    print(a)

    # calculating mean
    mean = a.mean()
    print(mean)

    # masking: print values less than mean in list
    print(a[a < mean])

    # replace values less than mean with mean
    a[a < mean] = mean
    print(a)


if __name__ == "__main__":
    test_run()
