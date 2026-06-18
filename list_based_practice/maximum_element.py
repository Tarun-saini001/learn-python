def max_value(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

print(max_value([20, 40, 30, 100, 100, 2]))


def mini_value(numbers):
    smallest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num

    return smallest

print(mini_value([20, 40, 30, 100, 100, 2]))