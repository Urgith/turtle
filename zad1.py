from time import perf_counter  # time measurement module
import numpy as np  # module to work with matrixes
import pylab  # module which draw charts
from scipy import linalg


def calculating(size_of_matrix):
    ''' function which calculate time to solve a linear equation system
        in form A*X=B
        Arguments:
          size_of_matrix - vertical and horizontal size of matrix
                           it should be positive integer
        return:
          average time of calculating solution
    '''
    start = perf_counter()
    times = []

    # A - coefficients of the equation system
    # B - constant terms
    while perf_counter() - start < 0.05:
        A = np.random.rand(size_of_matrix, size_of_matrix)
        B = np.random.rand(size_of_matrix, 1)

        if np.linalg.det(A) == 0:
            continue

        start_of_calculating = perf_counter()
        X = linalg.solve(A, B)
        times.append(perf_counter() - start_of_calculating)

    if len(times) > 0:
        times.remove(max(times))

    return sum(times) / len(times)


def creating_chart(size, order=3):
    ''' function which create chart of execution time of finding solutions
        in linear equation system
        Arguments:
          size - maximum size of tested system (number of unknown)
                 it should pe integer >=11
          order - order of approximated polynomial, nominal=3
        return: polynomial as string
    '''
    if type(size) != int:
        raise TypeError('size must be integer')
    elif size <= 10:
        raise ValueError('size must be greater than 11')

    if type(order) != int:
        raise TypeError('order must be integer')
    elif order < 0:
        raise ValueError('order can not be negative')

    x_every_10 = np.arange(1, size)
    y_every_10 = np.asarray([calculating(siz) for siz in np.nditer(x_every_10)])
    pylab.plot(x_every_10, y_every_10, 'o', markersize=1, label='measured execution time')

    coefs = np.polyfit(x_every_10, y_every_10, 3)
    polynomial = np.poly1d(coefs)

    x_every_1 = np.arange(1, size)
    y_approx = np.asarray([polynomial(siz) for siz in np.nditer(x_every_1)])

    pylab.plot(x_every_1, y_approx, label='approximated function')

    pylab.legend()
    pylab.grid(True)
    pylab.title('solving linear equation system')
    pylab.xlabel('size of matrix [n]')
    pylab.ylabel('time of execution [s]')
    pylab.show()

    return polynomial

function = creating_chart(501)
print(function)
