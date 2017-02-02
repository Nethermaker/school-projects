nominees = ['Moonlight', 'Lion', 'Arrival', 'Manchester by the Sea', 'La La Land',
            'Hell or High Water', 'Hidden Figures', 'Fences']

#1. Print out the movie 'Manchester by the Sea'
#2. Remove the movie 'Lion'
#3. Print out the location of La La Land.
#4. Print out the number of times 'Fences' appears in this list.
#5. Add the movie 'Hacksaw Ridge' to the end of the list.
#6. Print out the new list.

print nominees[3]
nominees.remove('Lion')
print nominees.index('La La Land')
print nominees.count('Fences')
nominees.append('Hacksaw Ridge')
print nominees
