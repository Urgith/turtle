from time import perf_counter  # time measurement module
import numpy as np  # module to work with matrixes
import pylab  # module which draw charts


def calculating_matrix(size_of_matrix):
    ''' function which calculate time to solve a linear equation system
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
    while perf_counter() - start < 1:
        A = np.random.rand(size_of_matrix, size_of_matrix)
        B = np.random.rand(size_of_matrix, 1)

        if np.linalg.det(A) == 0:
            continue

        start_of_calculating = perf_counter()
        np.linalg.solve(A, B)
        times.append(perf_counter() - start_of_calculating)

    return sum(times) / len(times)


def creating_chart(size):
    ''' function which create chart of execution time of finding solutions
        in linear equation system
        Arguments:
          size - maximum size of tested system (number of unknown)
                 it should pe integer >=11
        return: None
    '''
    if type(size) != int:
        raise TypeError('size must be integer')
    if size <= 10:
        raise ValueError('size must be greater than 11')

    x1 = np.arange(10, size, 10)
    y1 = np.asarray([calculating_matrix(siz) for siz in np.nditer(x1)])
    pylab.plot(x1, y1, 'o', label='measured execution time of execution')

    coefs = np.polyfit(x1, y1, 3)
    polynomial = np.poly1d(coefs)

    x2 = np.arange(1, 201)
    y2 = np.asarray([polynomial(siz) for siz in np.nditer(x2)])

    pylab.plot(x2, y2, label='approximated function')

    pylab.legend()
    pylab.grid(True)
    pylab.show()

    return polynomial

function = creating_chart(201)
print(function)
