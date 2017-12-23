from itertools import cycle
from copy import deepcopy


def read_data_input():
    with open('data.txt', 'r') as file:
        for lines in file:
            lines = lines.replace('\n', '').split('\t')
        lines = [int(number) for number in lines]
        return lines

def get_redistribution(arr_block):
    times_to_move = max(arr_block)

    index = arr_block.index(times_to_move)

    arr_block[index] = 0

    for i in range(times_to_move):
        if index + 1 >= len(arr_block):
            index = 0
        else:
            index += 1
        arr_block[index] += 1

    return deepcopy(arr_block)


def cycle_around_blocks(arr_block):

    cache_block = [deepcopy(arr_block)]

    for _ in cycle(arr_block):

        result = get_redistribution(arr_block)

        if result in cache_block:
            return len(cache_block)

        cache_block.append(result)

if __name__ == '__main__':
    data_input = read_data_input()
    result = cycle_around_blocks(data_input)
    print('Answer 1: ', result)