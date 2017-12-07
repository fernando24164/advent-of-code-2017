input_data = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]
expect_value = 18

result_per_line = []
for element in input_data:
    min_value = min(element)
    max_value = max(element)
    result_per_line.append(max_value-min_value)

try:
    assert expect_value == sum(result_per_line)
except AssertionError:
    print "Error in your code"
