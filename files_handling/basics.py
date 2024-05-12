# read

f = open("files_handling/demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()


# write

# f = open("files_handling/demo.txt", "w")
# f.write("\nI am learning python")
# f.close()


# append

# f = open("files_handling/demo.txt", "a")
# f.write("\nI am learning file I/O")
# f.close()


# r+ -> read, overwrite, no truncate, (ptr - start)
# w+ -> read, overwrite, truncate
# a+ -> read, append, no truncate, (ptr -end)


# with syntax

# with open("files_handling/demo.txt", "r") as f:
#     data = f.read()
#     print(data)
    
# with open("files_handling/demo.txt", "w") as f:
#     f.write("Enter new data")
    
    
# delete

import os
# - create
f = open("files_handling/sample.txt", "w")
f.write("Sample.txt")
# - delete
# os.remove("files_handling/sample.txt") 