from AnimalShelter import AnimalShelter

# instantiates an AnimalShelter
shelter = AnimalShelter()

# Creates a list of dogs and a cat
animals = [
    {"name": "Spike",
     "type": "dog"},
    {"name": "Arrow",
     "type": "dog"},
    {"name": "Earl",
     "type": "cat"},
    ]

# Cycles through list and puts them in the shelter using the create method
for i in animals:
    shelter.create(i)

# Uses read method to list the logs in the shelter
dogs = shelter.read({"type": "dog"})
for dog in dogs:
    print(dog)
