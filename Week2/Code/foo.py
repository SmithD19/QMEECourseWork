import easygui

path = easygui.fileopenbox

f = open("seq.txt", "r")

# for each line assign it to an element in list
seq_total = []
for lines in f:
    print(lines)
    seq_total.append(lines)

# first seq assigned
seq1 = seq_total[0]

# second seq assigned
seq2 = seq_total[1]

# Assign the longer sequence s1, and the shorter to s2
# l1 is length of the longest, l2 that of the shortest

l1 = len(seq1)
l2 = len(seq2)
if l1 >= l2:
    s1 = seq1
    s2 = seq2
else:
    s1 = seq2
    s2 = seq1
    l1, l2 = l2, l1 # swap the two lengths

