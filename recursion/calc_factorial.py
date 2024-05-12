# write a recursive python program to caculate factorial of a number

def fact(num):
    if (num == 0 or num == 1):
        return 1
    return num * fact(num - 1)
print(fact(5))