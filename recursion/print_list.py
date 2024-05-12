# write a recursive function to print element of a list

fruits = ["mango", "grapes", "apple", "pear"]

def print_list(li, idx=0):
    if(idx == len(li)):
        return
    print(li[idx])
    print_list(li, idx + 1)
    
print_list(fruits)