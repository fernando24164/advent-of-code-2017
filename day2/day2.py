from itertools import permutations

# part 1
with open("data.txt", "r") as input_data:
    result_part_one = []
    for line in input_data:
        elements = map(int, line.split())
        try:
            min_value = min(elements)
            max_value = max(elements)
            result_part_one.append(max_value - min_value)
        except ValueError:
            pass

print('Answer', sum(result_part_one))

def check_number(line):
    answer = []
    for a,b in permutations(line, 2):
        if (a % b == 0):
            if (a < b):
                answer.append(b/a)
            else:
                answer.append(a/b)
    return sum(answer)


result_part_two = []

with open("data.txt", "r") as input_data:
    result_part_one = []
    for line in input_data:
        elements = map(int, line.split())
        try:
            result_part_two.append(check_number(elements))
        except ValueError:
            pass

print("Answer", sum(result_part_two))