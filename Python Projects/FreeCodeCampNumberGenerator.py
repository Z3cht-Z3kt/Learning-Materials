def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    elif n < 1:
        return 'Argument must be an integer greater than 0.'
    else:
        for numbers in list(range(1, n + 1)):
            return ' '.join(str(numbers) for numbers in range(1, n + 1))

print(number_pattern(6))