import random


def is_divisible_by_seven(x):
    return x % 7 == 0


def test():
    test_data_count = 22
    test_data = {random.randint(-100, 100) for _ in range(test_data_count)}

    print("|  x  | divisible by 7")
    print("|-----|---------------")
    for x in test_data:
        result = is_divisible_by_seven(x)
        print("|{:^5d}| {}".format(x, result))


if __name__ == "__main__":
    test()
