# combining conditionals and loops
for j in range(12):
    if j % 3 == 0:
        print('There\'s always a bigger fish')

for j in range(15):
    if j % 5 == 3: # if remainder = 3
        print('General Kenobi')
    elif j % 4 == 3: # if remainder = 4
        print('Hello there')

z = 0
while z != 15:
    print('I have the high ground')
    z = z + 3

z = 12
while z < 100:
    if z == 31:
        for k in range(7):
            print('It\'s over Anakin')
    elif z == 18:
        print('Hello')
    z = z + 1



