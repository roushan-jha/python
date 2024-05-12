# write a recursive function to calculate the sum of first n natural numbers

def calc_sum(num):
    if(num == 0):
        return 0
    return (calc_sum(num - 1) + num)

print(calc_sum(5))