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