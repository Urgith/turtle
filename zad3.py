import turtle


def setup():
    ''' function which prepare our turtle to work,
        it set him to left down corner and speeds him up
    Arguments: none of them
    return: None
    '''
    turtle.hideturtle()
    turtle.speed(0)
    turtle.up()

    turtle.setposition(
        -(turtle.window_width() / 2) + 20,
        -(turtle.window_height() / 2) + 20
    )

    turtle.down()


def hilbert(iterations, length, version='left'):
    ''' function which draw hilbert curve
    Arguments:
      iterations - number of iterations of hilbert curve
      length - length of single line
      version - version of algorithm ('to left' or 'to right')
    return: None
    '''
    if length is None:
        if iterations >= 3:
            length = min(turtle.window_width() - 40, turtle.window_height() - 40) / (2**iterations)

        elif iterations == 2:
            length = min(turtle.window_width() - 40, turtle.window_height() - 40) / 3

        elif iterations == 1:
            length = min(turtle.window_width() - 40, turtle.window_height() - 40)

    if iterations == 0:
        return

    if version == 'left':
        turtle.left(90)
        hilbert(iterations - 1, length, 'right')
        turtle.forward(length)
        turtle.right(90)
        hilbert(iterations - 1, length, 'left')
        turtle.forward(length)
        hilbert(iterations - 1, length, 'left')
        turtle.right(90)
        turtle.forward(length)
        hilbert(iterations - 1, length, 'right')
        turtle.left(90)

    elif version == 'right':
        turtle.right(90)
        hilbert(iterations - 1, length, 'left')
        turtle.forward(length)
        turtle.left(90)
        hilbert(iterations - 1, length, 'right')
        turtle.forward(length)
        hilbert(iterations - 1, length, 'right')
        turtle.left(90)
        turtle.forward(length)
        hilbert(iterations - 1, length, 'left')
        turtle.right(90)


def draw_hilbert(iterations, length=None):
    ''' function which draw hilbert curve with preparation
    Arguments:
      iterations - number of iterations of hilbert curve
      length - length of single line
    return: None
    '''
    if type(iterations) != int:
        raise TypeError('iterations must be integer')

    elif iterations <= 0:
        raise ValueError('iterations must be positive')

    if length is None:
        pass
    elif type(length) != int and type(length) != float:
        raise TypeError('length must be integer or float')

    elif length <= 0:
        raise ValueError('length must be positive')

    setup()
    hilbert(iterations, length)
    turtle.mainloop()


if __name__ == '__main__':
    draw_hilbert(4)
