"""Accessing NumPy arrays."""
import numpy as np


def test_run():
    a = np.random.rand(5, 4)
    print("Array:\n", a)

    # Accessing element at position (3, 2)
    element = a[3, 2]
    print(element)

    # Elements in defined range
    print(a[0, 1:3])

    # Top left corner of array
    print(a[0:2, 0:2])

    print(a[:, 0:3:2])  # will select columns 0, 2 for every row


if __name__ == "__main__":
    test_run()
