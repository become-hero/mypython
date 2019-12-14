def factorial_func(num):
    if num>1:
        return num*factorial_func(num-1)
    else:
        return num

print(factorial_func(6))
