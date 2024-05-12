color = ["red", "black", "green", "white", "yellow"]
# print(len(color)) - built-in function

def len_list(li):
    count = 0
    for el in li:
        count += 1
    return count

colors = len_list(color)  # number of color
print(colors)  
    