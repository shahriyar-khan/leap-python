current_movies = {"The Grinch":"11L00am",
                  "Rudolp":"1:00pm",
                  "Frosty the Snowman":"3:00pm",
                  "Christmas Vacation":"5:00pm"}

print("We're currently showing the following movies:")
for key in current_movies:
    print(key)
print()
movie = input("What movie would you like the showtime for: ")

showtime = current_movies.get(movie)
if showtime == None:
    print("Requested showtime isn't playing")
else:
    print("{} is playing at {}".format(movie, showtime))