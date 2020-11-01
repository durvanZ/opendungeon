import room as room

class Player:
    room_ID = 0
    def __init__(self, name, age, health, items, currentRoom):
        self.name = name
        self.age = age
        self.health = health
        self.items = []
        self.currentRoom = 0

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health

    def get_current_room(self):
        return self.currentRoom

    def set_current_room(self, room):
        self.currentRoom = room

    
