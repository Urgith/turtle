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
    turtle.setposition(-turtle.window_width() / 2, 0)
    turtle.down()


def koch_curve(iterations, size, angle, moves='f'):
    ''' function which draw koch curve
        Arguments:
          iterations - number of iterations of koch curve
          size - length of single line
          moves - moves to do
        return: None
    '''
    if size is None:
        size = turtle.window_width() / (3**iterations)

    for move in moves:
        if move == 'f':
            if iterations == 0:
                turtle.forward(size)
            else:
                koch_curve(iterations - 1, size, angle, 'flfrflf')
        if move == 'l':
            turtle.left(angle)
        if move == 'r':
            turtle.right(2*angle)


def draw_koch_curve(iterations, size=None, angle=60):
    ''' function which draw koch curve with preparation
        Arguments:
          iterations - number of iterations of koch curve
          size - length of single line
          angle - angle of curve, nominal=60
        return: None
    '''
    if type(iterations) != int:
        raise TypeError('iterations must be integer')
    elif iterations < 0:
        raise ValueError('iterations can not be negative')

    if size is None:
        pass
    elif type(size) != int and type(size) != float:
        raise TypeError('size must be integer or float')
    elif size < 0:
        raise ValueError('size can not be negative')

    setup()
    koch_curve(iterations, size, angle)
    turtle.mainloop()

draw_koch_curve(4)
