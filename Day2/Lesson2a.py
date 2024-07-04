# In this Lesson we will Do Dta Types List, Tuples and Dictionary
# Define a List
# NB: ALways remind students that we count List items from Zero, Lists uses []
cars = ['Honda',67,'["blue,"red"]', 'Nissan', 'Surf', 'Mazda', 'Volkswagon']

# Print
# print(cars)

# Accessing List items by index
# print(cars[4])

# Slicing
# Print from index 1 to 5, There is a minus one
# print(cars[1:4])

# Print from index 3 and above
# print(cars[3:])

# Print upto index 4 and below, There is a minus one
# print(cars[:5])

# List are mutable, Can be updated
# Lets Understand List Mutability
# Lets Update our List by Appending BMW into our List
# cars.append("BMW") 
cars[0] = 'hondar'
# print(cars)

# Now Print Your List
# print(cars)  # Notice from output BMW is at Last

# Insert Toyota at a Given Position, Below we Insert Cars at Position 2
# cars.insert(2, "Toyota")
# cars.append("BMW")
# print(cars)

# Now Print Your List, Notice Toyota at Position 2
# print(cars)
cars.pop()
print(cars)

# Next, What are Tuples? How do they Differ from Lists?