# Comprehensions
# These combine loops, functions and logical tests

# Example 1 - grow a list from an empty vector 1:10
x = [i for i in range(10)]
print(x)

# This is the same as writing the loop:
x = []
for i in range(10):
    x.append(i)
print(x)