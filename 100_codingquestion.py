# What is the expected result of the following code?

result = [x for i, x in enumerate(range(10)) if i % 3 == 0]

print(result)

# OUTPUT
# [0, 3, 6, 9]
