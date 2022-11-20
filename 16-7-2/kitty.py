class Cat:
    def __init__(self, name="", gender="", age=0):
        self.name = name
        self.gender = gender
        self.age = age

    def from_dict(self, some_cat):
        self.name = some_cat.get("name")
        self.gender = some_cat.get("gender")
        self.age = some_cat.get("age")