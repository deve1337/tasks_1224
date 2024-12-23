def is_divisible_by_seven(x):
    return x % 7 == 0


input_data = [4, 7, 15, 28, 111, 8687]

for x in input_data:
    print(x, "-", is_divisible_by_seven(x))
