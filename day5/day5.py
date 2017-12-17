def load_array_input():
    with open('input.txt', 'r') as file:
        arr = []
        for line in file:
            line = line.replace('\n', '')
            arr.append(int(line))
        return arr


def complete_array_maze(arr):
    number_of_jumps = 0
    current_index = 0
    while True:
        try:
            next_index = current_index + arr[current_index]
            arr[current_index] += 1
            current_index = next_index
            number_of_jumps += 1
        except IndexError:
            return number_of_jumps


def complete_array_maze_part2(arr):
    current_index = 0
    number_of_jumps = 0
    next_index = 0
    while True:
        try:
            next_index = current_index + arr[current_index]
            if arr[current_index] >= 3:
                arr[current_index] -= 1
            else:
                arr[current_index] += 1
            current_index = next_index
            number_of_jumps += 1
        except IndexError:
            return number_of_jumps


if __name__ == '__main__':
    data_input = load_array_input()
    solution = complete_array_maze(data_input)
    print('Answer ', solution)
    solution_2 = complete_array_maze_part2(data_input)
    print('Answer 2', solution_2)
