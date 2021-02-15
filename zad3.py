import turtle


def setup():
    ''' function which prepare our turtle to work,
        it set him to left down corner and speed him up
        Arguments: none of them
        return: None
    '''
    turtle.hideturtle()
    turtle.speed(0)
    turtle.up()
    turtle.setposition(-turtle.window_width() / 2 + 20,
                       -turtle.window_height() / 2 + 20)
    turtle.down()


def hilbert(iterations, size, version='A'):
    ''' function which draw hilbert curve
        Arguments:
          iterations - number of iterations of hilbert curve
          size - length of single line
          version - version of algorithm ('to left' or 'to right')
        return: None
    '''
    if size is None:
        if iterations >= 3:
            size = min(turtle.window_width() - 40,
                       turtle.window_height() - 40) / (2**iterations)
        elif iterations == 2:
            size = min(turtle.window_width() - 40,
                       turtle.window_height() - 40) / 3
        elif iterations == 1:
            size = min(turtle.window_width() - 40, turtle.window_height() - 40)

    if iterations == 0:
        return

    if version == 'A':
        turtle.left(90)
        hilbert(iterations - 1, size, 'B')
        turtle.forward(size)
        turtle.right(90)
        hilbert(iterations - 1, size, 'A')
        turtle.forward(size)
        hilbert(iterations - 1, size, 'A')
        turtle.right(90)
        turtle.forward(size)
        hilbert(iterations - 1, size, 'B')
        turtle.left(90)

    elif version == 'B':
        turtle.right(90)
        hilbert(iterations - 1, size, 'A')
        turtle.forward(size)
        turtle.left(90)
        hilbert(iterations - 1, size, 'B')
        turtle.forward(size)
        hilbert(iterations - 1, size, 'B')
        turtle.left(90)
        turtle.forward(size)
        hilbert(iterations - 1, size, 'A')
        turtle.right(90)


def draw_hilbert(iterations, size=None):
    ''' function which draw hilbert curve with preparation
        Arguments:
          iterations - number of iterations of hilbert curve
          size - length of single line
        return: None
    '''
    if type(iterations) != int:
        raise TypeError('iterations must be integer')
    elif iterations <= 0:
        raise ValueError('iterations must be positive')

    if size is None:
        pass
    elif type(size) != int and type(size) != float:
        raise TypeError('size must be integer or float')
    elif size <= 0:
        raise ValueError('size must be positive')

    setup()
    hilbert(iterations, size)

draw_hilbert(4)
