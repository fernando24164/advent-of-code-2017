from itertools import cycle, product
from collections import defaultdict


def move_right(x, y): return x + 1, y


def move_down(x, y):  return x, y - 1


def move_left(x, y):  return x - 1, y


def move_up(x, y):    return x, y + 1


def spiral(end):
    m = cycle([move_right, move_up, move_left, move_down])
    n = 1
    pos = 0, 0
    times_to_move = 1

    yield n, pos

    while True:
        for _ in range(2):
            move = next(m)
            for _ in range(times_to_move):
                if n >= end:
                    return
                pos = move(*pos)
                n += 1
                yield n, pos

        times_to_move += 1


# Part One
data_input = 289326
sp = spiral(data_input)
try:
    while True:
        n, pos = next(sp)
except StopIteration:
    pass

print(abs(pos[0]) + abs(pos[1]))

# Part Two
move_right = lambda x, y: (x + 1, y)
move_up = lambda x, y: (x, y + 1)
move_left = lambda x, y: (x - 1, y)
move_down = lambda x, y: (x, y - 1)


def spiral(end_number):
    direction = cycle([move_right, move_up, move_left, move_down])
    times_to_move = 1
    current_number = 1
    coordinates = (0, 0)
    values = defaultdict(lambda: 0)
    values['0,0'] = 1

    def get_current_coordinates():
        return "{0},{1}".format(coordinates[0], coordinates[1])

    def get_coordinates(x, y):
        coordinates_aux = (coordinates[0] + x, coordinates[1] + y)
        return "{0},{1}".format(coordinates_aux[0], coordinates_aux[1])

    def sum_of_neighbors():
        posible_values = [-1, 0, 1]
        set_of_coordinates = product(posible_values, repeat=2)
        answer_array = []
        for surroundings in set_of_coordinates:
            answer_array.append(values.get(get_coordinates(surroundings[0], surroundings[1])))
        return sum(filter(None, answer_array))

    while True:
        # every two direction the time to repeat the movement increase one
        for _ in range(2):
            movement = next(direction)
            for _ in range(times_to_move):
                if current_number >= end_number:
                    return
                coordinates = movement(coordinates[0], coordinates[1])
                current_number = sum_of_neighbors()
                values[get_current_coordinates()] = current_number
                yield current_number

        times_to_move += 1


data_input = 289326
sp = spiral(data_input)
number = 0
try:
    while True:
        number = next(sp)
except StopIteration:
    pass

print(number)
