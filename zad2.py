class Stack:
    ''' class of stack, top of stack is on end of list
    Defined methods:
      __init__ - constructor of this class, it initialize empty stack
      __str__ - method which returns string representation of stack
      push - method which add element on top of stack
      pull - method which pull element from top of stack
      peek - method which check element from top of stack
      isEmpty - method which check if stack is empty
      size - method which calculate size of stack
    '''
    def __init__(self):
        ''' constructor of the class, initialize empty stack as python list'''
        self.items = []

    def __str__(self):
        ''' return stack in string representation'''
        string = '#'

        for item in self.items:
            string += str(item) + '>'

        return string

    def isEmpty(self):
        ''' function which check if stack is empty
        return: True, if stack is empty
        return: False, if stack is not empty
        '''
        return self.items == []

    def push(self, item):
        ''' function which add element on stack
        Arguments:
          item - element added on top of Stack
        return: None
        '''
        self.items.append(item)

    def pop(self):
        ''' function which remove top of stack
        return: element on top of stack
        '''
        return self.items.pop()

    def peek(self):
        ''' function which return top of stack
        return: item on top of stack
        '''
        return self.items[-1]

    def size(self):
        ''' function which calculate size of stack
        return: size of stack
        '''
        return len(self.items)


def hanoi_tower(size):
    ''' function which show how to solve hanoi tower problem
    Arguments:
      size - size (height) of solved tower
    return: None
    '''
    if type(size) != int:
        raise TypeError('size must be integer')
    if size < 0:
        raise ValueError('size can not be negetive')

    start_pole = Stack()
    middle_pole = Stack()
    final_pole = Stack()

    for roller in range(size, 0, -1):
        start_pole.push(roller)
    poles = [start_pole, middle_pole, final_pole]

    show_poles(poles)
    move_tower(size, start_pole, middle_pole, final_pole, poles)


def move_tower(size, start, middle, final, poles):
    ''' recursive function which is solving hanoi tower problem
    Arguments:
      size - size (height) of solved tower
      start - starting pole as Queue()
      middle - middle (helping) pole as Queue()
      final - final pole as Queue()
      poles - list of all 3 poles
    '''
    if size >= 1:
        move_tower(size - 1, start, final, middle, poles)
        move_roller(start, final)
        show_poles(poles)
        move_tower(size - 1, middle, start, final, poles)


def move_roller(old_pole, new_pole):
    ''' function which change position of two rollers
    Arguments:
      old_pole - current pole of roller
      new_pole - new pole of roller
    return: None
    '''
    new_pole.push(old_pole.pop())


def show_poles(poles):
    ''' function which show content of stacks
    Arguments:
      poles - list of stacks
    return: None
    '''
    print(poles[0])
    print(poles[1])
    print(poles[2], '\n')


if __name__ == '__main__':
  hanoi_tower(4)
