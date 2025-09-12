# Example of using a dictionary to manage movie showtimes
current_movies = {'The Grinch': '11:00am',
                  'The Matrix': '12:00pm',
                  'The Green Mile': '4:00pm',
                  'The Godfather': '2:00pm'}

print("Current movies showing:")
for key in current_movies:
    print(key)
# Prompt user for a movie
movie = input("Enter the movie you want to see: ")
# Look up the movie in the dictionary
showtime = current_movies.get(movie)
print(showtime)

if showtime == None:
    print("Movie not found")
else:
    print("Movie found, it starts at " + showtime)