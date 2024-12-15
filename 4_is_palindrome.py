def is_palindrome(x):
    # негативные числа не могут быть палиндромом
    if x < 0:
        return False

    # числа оканчивающиеся на 0 (но не сам 0) - не могут быть палиндромом
    if x != 0 and x % 10 == 0:
        return False

    # половину разрядов с конца переносим в x_reversed
    # примеры результатов выполнения:
    # | x исходный |    x    | x_reversed |
    # |   12345    | 12      | 543        |
    # |   12321    | 12      | 321        |
    # |   4444     | 44      | 44         |
    x_reversed = 0
    while x_reversed < x:
        x_reversed = x_reversed * 10 + x % 10
        x //= 10

    # при нечетном кол-ве цифр в числе цифра посередине не важна
    return x == x_reversed or x == x_reversed // 10


def test():
    test_data = (
        (12321, True),
        (12152, False),
        (34653, False),
        (363464363, True),
        (12345, False),
        (4444, True),
        (444, True),
        (44, True),
        (4, True),
        (4445, False),
        (445, False),
        (45, False),
    )

    for x, expected in test_data:
        result = is_palindrome(x)
        print(x, "-", result)
        assert result == expected


if __name__ == "__main__":
    test()
