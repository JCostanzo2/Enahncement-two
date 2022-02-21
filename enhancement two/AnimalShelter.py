from pymongo import MongoClient


class AnimalShelter(object):
    def __init__(self):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongod://%s:%s@localhost:46008' % (aacuser, password))
        self.database = self.client['project']

    # method for C in CRUD
    def create(self, data):
        if data is not None:
            print("Entering new animal.")
            self.database.animals.insert(data)  # data should be dictionary
        else:
            raise Exception("Nothing to save, because data parameter is empy")

    # method for R in CRUD
    def read(self, value=None):
        # if value isn't none then return all data that matches value
        if value:
            data = self.database.animals.find(value, {"_id": False})
        # if there is no value then return all data
        else:
            raise Exception("nothing to read, hint is empty")

        return data

    # this method is used to delete animal from the db
    def delete(self, _animal):
        if _animal is not None:
            data = self.read(_animal)  # finds the animal first
            if data is None:
                print("Animal does not exist")
                return
            self.database.animals.delete_many(_animal)
        else:
            raise Exception("nothing to delete, animal data is empty")

    # used for updating animal
    def update(self, _criteria, _newData):
        if _criteria is not None and _newData is not None:
            self.database.animals.update_many(_criteria, {'$set': _newData})
            self.read(_newData)

        else:
            raise Exception("Nothing to save, because data parameter is empy")
