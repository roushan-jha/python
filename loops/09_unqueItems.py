items = ["red", "blue", "orange", "white", "green", "white", "magenta"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate:", item)
        break
    else:
        unique_item.add(item)