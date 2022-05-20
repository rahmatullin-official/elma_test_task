def check_number(i):
    if i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    elif i % 12 == 0:
        return "FizzBuzz"
    else:
        return i


print(*[check_number(i) for i in range(1, 101)])
