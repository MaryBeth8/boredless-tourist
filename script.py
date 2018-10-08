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

test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)