# define list of desintations 
destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

# define test traveler 
test_traveler = ['Erin Wikles', 'Shanghai, China', ['hisotrical site', 'art']]

# write function to get an index 
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

# test function 
# print(get_destination_index('Hyderabad, India'
# ))

# define traveler location function 
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

# create testing vars 
test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

# define a list of attactions 
attractions = [[], [], [], [], []]
print(attractions)

# create add attraction variable 
def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)

# try function 
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
# print(attractions)

# add more attractions
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# print list 
# print(attractions)

# define find attraction function
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]

  # initiate empty list 
  attractions_with_interest = []

  # loop over attractions and append anything that matches
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = possible_attraction[1]
    for interest in interests:
      if attraction_tags.count(interest) > 0:
        attractions_with_interest.append(possible_attraction[0])
        
  return attractions_with_interest

# test function 
la_arts = find_attractions('Los Angeles, USA', ['art'])
print(la_arts)

# define a new functio 
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = ("Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": ")
  for attraction in traveler_attractions:
    interests_string += (attraction)
  return interests_string

# test function 
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)






