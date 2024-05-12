# write a python program to input a number and print "odd" or "even" depending on the number

n = (int)(input("Enter a number: "))

def check_even_odd(num):
    if(num % 2 == 0):
        return "even"
    else:
        return "odd"
print(check_even_odd(n))