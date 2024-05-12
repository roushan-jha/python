# write a recursive function to print numbers from 1 to n

def show(num):
    if num == 0:
        return
    print(num)
    show(num - 1)
    
show(10)
