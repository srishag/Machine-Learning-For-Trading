"""Minimize an objective function, using SciPy."""

import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo


def error_poly(C, data):  # error function
    """Ciompute error between given polynomial and observed data.

    Parameters:
        C: numpy.poly1d object or equivalent array representing polynomial coefficients
        data: 2D array where each row is a point (x, y)

    Returns error as a single real value.
    """
    # Metric: sum of squared Y-axis differences
    err = np.sum((data[:, 1] - np.polyval(C, data[:, 0]))**2)
    return err


def fit_poly(data, error_func, degree=3):
    """Fit a polynomial to given data, using a supplied error function.

    Parameters:
        data: 2D array where each row is a point (X0, Y)
        error_func: function that computes the error between a polynomial and observed data

    Returns polynomial that minimizes the error function.
    """
    # Generate initial guess for polynomial model (all coefficients = 1)
    Cguess = np.poly1d(np.ones(degree + 1, dtype=np.float32))

    # Plot initial guess (optional)
    x = np.linspace(-5, 5, 21)
    plt.plot(x, np.polyval(Cguess, x), 'm--', linewidth=2.0, label="Initial guess")

    # Call optimizer to minimize error function
    result = spo.minimize(error_func, Cguess, args=(data,), method='SLSQP', options={'disp': True})
    return np.poly1d(result.x)


def test_run():
    # Define original polynomial
    poly_orig = np.poly1d(np.array([1, -5, 5, 10, -2], dtype=np.float32))
    Xorig = np.linspace(-5, 5, 21)
    Yorig = np.polyval(poly_orig, Xorig)
    plt.plot(Xorig, Yorig, 'b--', linewidth=2.0, label="Original polynomial")

    # Generate noisy data points
    noise_sigma = 3.0
    noise = np.random.normal(0, noise_sigma, Yorig.shape)
    data = np.asarray([Xorig, Yorig + noise]).T
    plt.plot(data[:, 0], data[:, 1], 'go', label="Data points")

    # Try to fit a polynomial to this data
    poly_fit = fit_poly(data, error_poly)
    plt.plot(data[:, 0], np.polyval(poly_fit, data[:, 0]), 'r--', linewidth=2.0, label="Fitted polynomial")
    plt.legend(loc="upper right")
    plt.show()


if __name__ == "__main__":
    test_run()
