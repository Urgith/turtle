from time import perf_counter
from scipy import linalg
import numpy as np
import pylab


def calculating(size_of_matrix):
    ''' Calculate time to solve a linear equation system in form A*X=B
    Arguments:
      size_of_matrix - vertical and horizontal size of matrix (int>0)
    return:
      average time of calculating solution
    '''
    start = perf_counter()
    times = []

    # A - coefficients of the equation system
    # B - constant terms
    iterations = 0
    while perf_counter() - start < 0.05 or iterations <= 2:
        iterations += 1

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
    ''' Create chart of execution time for linear equation solver
    Arguments:
      size - maximum size of tested system (number of unknowns, int>=11)
      order - order of approximated polynomial, nominal=3
    return: polynomial as string
    '''
    if type(size) != int:
        raise TypeError('size must be integer')
    elif size <= 1:
        raise ValueError('size must be greater than 11')

    if type(order) != int:
        raise TypeError('order must be integer')
    elif order < 0:
        raise ValueError('order can not be negative')

    sizes = np.arange(1, size)
    execut_t = np.asarray([calculating(siz) for siz in np.nditer(sizes)])
    pylab.plot(sizes, execut_t, 'o', markersize=1, label='execution time')

    coefs = np.polyfit(sizes, execut_t, 3)
    polynomial = np.poly1d(coefs)

    sizes = np.arange(1, size)
    y_approx = np.asarray([polynomial(siz) for siz in np.nditer(sizes)])

    pylab.plot(sizes, y_approx, label='approximated function')
    pylab.title('solving linear equation system')
    pylab.ylabel('time of execution [s]')
    pylab.xlabel('size of matrix [n]')
    pylab.legend()
    pylab.grid()

    pylab.show()

    return polynomial


if __name__ == '__main__':
    function = creating_chart(501)
    print(function)
