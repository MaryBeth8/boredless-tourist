"""This is the Boredless Tourist project from Codecademy's Computer Science path.
This project contains a recommendation engine designed to give tourists the power to 
find the parts of the city that fit the pace of their life.
This engine first evaluate a person's interests, then gives recommendations in the area 
to venues, restaurants, and historical destinations that they are likely to be enjoyable. 
"""

# list of possible destinations
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "So Paulo, Brazil", "Cairo, Egypt"]

# define a test traveler to see how the engine's functionality is working
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# return index of a destination
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

# return the index of a specific traveler's destination
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

# testing get_traveler_location()
#test_destination_index = get_traveler_location(test_traveler)
#print(test_destination_index)

# create attractions list
attractions = [[] for d in destinations]

# enable adding attractions to attractions list
def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
  except SyntaxError:
    return

# add attractions to attractions list  
add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
print(attractions)
