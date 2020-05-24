"""Creating NumPy arrays."""
import numpy as np


def test_run():
    # np.empty() -> elements of array read in whatever values were present at the corresponding memory location

    # Empty array: 1D array
    print(np.empty(5))

    # Empty array: 2D array with 5 rows, 4 cols
    print(np.empty((5, 4)))

    # Empty array: 3D array with 5 rows, 4 cols, depth of 3
    # print(np.empty((5, 4, 3)))

    # Array of 1s: float type by default
    print(np.ones((5, 4)))

    # Array of 1s: specifying data type as integer
    print(np.ones((5, 4), dtype=np.int_))


if __name__ == "__main__":
    test_run()
