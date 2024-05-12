# write a function to print elements of a list in single line

vehicle = ["car", "bike", "bus", "train", "ship"]

def print_el(li):
    for el in li:
        print(el, end=" ")
        
print_el(vehicle)
