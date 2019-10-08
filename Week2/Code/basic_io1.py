######
# FILE INPUT
######
# Open a file for reading

import pickle
f = open('../Sandbox/test.txt', 'r')

# use an implicit for loop
for line in f:
    print(line)

# close the file
f.close()

# Now do the same example but skip the blank lines

f = open('../Sandbox/test.txt', 'r')

# use an implicit for loop
for line in f:
    if len(line.strip()) > 0:
        print(line)

# close the file
f.close()

