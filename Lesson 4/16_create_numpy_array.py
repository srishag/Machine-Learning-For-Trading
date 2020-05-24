"""Creating NumPy arrays."""
import numpy as np


def test_run():
    # List to 1D array
    print(np.array([2, 3, 4]))

    # 2D array using sequence of sequences: 2 rows, 3 cols
    print(np.array([(2, 3, 4), (5, 6, 7)]))


if __name__ == "__main__":
    test_run()
