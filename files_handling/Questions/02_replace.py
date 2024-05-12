f = open("files_handling/Questions/practice.txt", "r")
data = f.read()

new_data = data.replace("Java", "Python")
print(new_data) 

with open("files_handling/Questions/practice.txt", "w") as f:
    f.write(new_data)
       