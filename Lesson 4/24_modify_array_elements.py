"""Modifying NumPy arrays."""
import numpy as np


def test_run():
    a = np.random.rand(5, 4)
    print("Array:\n", a)

    # Assigning a value to a particular location
    a[0, 0] = 1
    print("Modified (replaced one element):\n", a)

    # Assigning a single value to an entire row
    a[0, :] = 2
    print("Modified (replaced a row with a single value):\n", a)

    # Assigning a list to a column in an array
    a[:, 3] = [1, 2, 3, 4, 5]
    print("Modified (replaced a column with a list):\n", a)


if __name__ == "__main__":
    test_run()
