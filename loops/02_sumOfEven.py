n = 6
even_sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
print("Sum of even numbers till", n, " is ", even_sum)