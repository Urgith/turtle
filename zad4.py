import turtle


def setup():
    ''' function which prepare our turtle to work,
        it set him to left down corner and speeds him up
    Arguments: none of them
    return: None
    '''
    turtle.speed(0)
    turtle.hideturtle()
    turtle.up()
    turtle.setposition(-turtle.window_width() / 2, 0)
    turtle.down()


def koch_curve(iterations, length, angle, moves='f'):
    ''' function which draw koch curve
    Arguments:
      iterations - number of iterations of koch curve
      length - length of single line
      angle - angle of turn
      moves - moves to do f-forward, l-turn left, r-turn right
    return: None
    '''
    if length is None:
        length = turtle.window_width() / (3**iterations)

    for move in moves:
        if move == 'f':
            if iterations == 0:
                turtle.forward(length)

            else:
                koch_curve(iterations - 1, length, angle, 'flfrflf')

        if move == 'l':
            turtle.left(angle)
        if move == 'r':
            turtle.right(2 * angle)


def draw_koch_curve(iterations, length=None, angle=60):
    ''' function which draw koch curve with preparation
    Arguments:
      iterations - number of iterations of koch curve
      length - length of single line
      angle - angle of turn, nominal=60
    return: None
    '''
    if type(iterations) != int:
        raise TypeError('iterations must be integer')
    elif iterations < 0:
        raise ValueError('iterations can not be negative')

    if length is None:
        pass
    elif type(length) != int and type(length) != float:
        raise TypeError('length must be integer or float')

    elif length < 0:
        raise ValueError('length can not be negative')

    setup()
    koch_curve(iterations, length, angle)
    turtle.mainloop()


if __name__ == '__main__':
    draw_koch_curve(4)
