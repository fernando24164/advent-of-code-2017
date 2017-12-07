# part 1
with open("data.txt", "r") as input_data:
    for lines in input_data:
        array_values = [int(number) for index, number in enumerate(lines)
                        if int(number) == int(lines[int(index + 1) % len(lines)])]

print("Answer: ", sum(array_values))

# part 2
with open("data.txt", "r") as input_data:
    for lines in input_data:
        array_values = [int(number) for index, number in enumerate(lines)
                        if int(number) == int(lines[int(index + (len(lines) / 2)) % len(lines)])]

print("Answer: ", sum(array_values))
