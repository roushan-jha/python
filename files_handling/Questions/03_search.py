def check_word(word):
    with open("files_handling/Questions/practice.txt", "r") as f:
        data = f.read()
        
        data = data.lower() # ignore case
        
        if(word in data):
            print("Found")
        else:
            print("Not found")
            
check_word("file")

def check_for_line(word):
    with open("files_handling/Questions/practice.txt", "r") as f:
        data = True
        line_no = 1
        while data:
            data = f.readline()
            if(word in data):
                return line_no
            line_no += 1
    return -1
            
print(check_for_line("File"))
    