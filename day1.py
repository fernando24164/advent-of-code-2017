input_data = ["1122", "1111", "1234", "91212129"]
expected_values = [3, 4, 0, 9]
result_array = []

for element in input_data:
    array_values = [int(number) for index, number in enumerate(element)
                    if int(number) == int(element[int(index+1) % len(element)])]
    result = sum(array_values)
    result_array.append(result)

for check in zip(result_array, expected_values):
    try:
        assert check[0] == check[1]
    except AssertionError:
        print "Error in your code"
