import math


def is_coprime(x, y):
    return math.gcd(x, y) == 1


test_data = (
    (56, 15, True),
    (17, 25, True),
    (12, 15, False),
    (20, 100, False),
    (3, 4, True),
    (7, 28, False),
)


def test():
    print("|   x, y   | is_coprime")
    print("|----------|-----------")
    for x, y, expected in test_data:
        print("|{:4d}, {:<4d}| {}".format(x, y, is_coprime(x, y)))
        assert is_coprime(x, y) == expected

    print("Test OK")


if __name__ == "__main__":
    test()
