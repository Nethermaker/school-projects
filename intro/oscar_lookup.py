with open('oscars.txt', 'rb') as infile:
    #print infile.read()
    movies = {}
    for line in infile:
        line = line.strip()
        movie, year = line.split('\t')
        year = int(year[1:5])
        movies[year] = movie

#UPDATE THE INFORMATION
movies[2015] = 'Spotlight'
movies[2016] = 'La La Land'


#Let's write a new file!
with open('newoscars.txt', 'w') as outfile:
    years = sorted(movies.keys()) #get the years in order
    for year in years:
        outfile.write('{}: {}\n'.format(year, movies[year]))





#infile = open('oscars.txt', 'rb')
