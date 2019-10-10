birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
         )

#(1) Write three separate list comprehensions that create three different
# lists containing the latin names, common names and mean body masses for
# each species in birds, respectively. 

latin_lc = [i[0] for i in birds]
name_lc = [i[1] for i in birds]
mass_lc = [i[2] for i in birds]



# (2) Now do the same using conventional loops (you can choose to do this 
# before 1 !). 

latin_loop = []
name_loop = []
mass_loop = []

attributes = [latin_loop, name_loop, mass_loop]

for i in birds:
    latin_loop.append(i[0])
    name_loop.append(i[1])
    mass_loop.append(i[2])
print(attributes)


