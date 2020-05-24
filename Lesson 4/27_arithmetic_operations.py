"""Accessing elements."""
import numpy as np


def test_run():
    a = np.array([(1, 2, 3, 4, 5),
                  (10, 20, 30, 40, 50)])
    b = np.array([(10, 20, 30, 40, 50),
                  (1, 2, 3, 4, 5)])
    print("Original array: a\n", a)
    print("Original array: b\n", b)

    # multiply a by 2: new array created
    print("Multiply a by 2:\n", 2*a)

    # Divide a by 2: new array created
    print("Divide a by 2:\n", a/2.0)

    # Add the two arrays
    print("Add a + b:\n", a + b)

    # divide the two arrays
    print("Divide a / b:\n", a / b)


if __name__ == "__main__":
    test_run()
