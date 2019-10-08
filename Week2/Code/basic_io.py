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

######
# FILE OUTPUT
######
# save the elements of a lsit to a file
list_to_save = range(100)

f = open('../Sandbox/testout.txt', 'w')
for i in list_to_save:
    f.write(str(i) + '\n')  # add a new line at the end


# close the file
f.close()

######
# STORING OBJECTS
######
# save an object for later use

my_dictionary = {'a key': 10, 'another key': 11}


f = open('../Sandbox/testp.p', 'wb')  # note the b: accept binary files
pickle.dump(my_dictionary, f)
f.close()

# Load the data again
f = open('../Sandbox/testp.p', 'rb')
another_dictionary = pickle.load(f)
f.close()

print(another_dictionary)
