import os

def count_num():
    with open("files_handling/Questions/numbers.txt", "w") as f:
        f.write("1, 22, 35, 16, 71, 3, 17, 50, 90, 63")
        
    with open("files_handling/Questions/numbers.txt", "r") as f:
        data = f.read()
    
        nums = data.split(",")
        count = 0
        for val in nums:
            if((int)(val) % 2 == 0):
                count += 1
                
    os.remove("files_handling/Questions/numbers.txt")
    return count

# print(count_num())

def count_word():
    with open("files_handling/Questions/practice.txt", "r") as f:
        data = f.read()
        words = data.split()
    return len(words)
        
print(count_word())

