import item as item
class room:
    allRooms = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]         #Static attributes (not specific to each room)

    def __init__(self, roomId) :         #defining the class (constructor)
        self.roomId = roomId                #attributes of the class specific to each room
        self.possibleRooms = []
        if id == 1 : items = []
        if id == 2 : items = []
        if id == 3 : items = []
        if id == 4 : items = []
        if id == 5 : items = []
        if id == 6 : items = []
        if id == 7 : items = []
        if id == 8 : items = []
        if id == 9 : items = []
        if id == 10 : items = []
        if id == 11 : items = []
        if id == 12 : items = []
        if id == 13 : items = []

    def open(self,allRooms):                #will run when player enters the room using room.get(id).open() method
        allRooms[self.roomId].room_graphics(self.roomId)        #will run graphics method
        allRooms[self.roomId].room_ambience(self.roomId)        #will run ambience method
        print("you have entered room {0}".format(self.roomId))        
        allRooms[self.roomId].room_narrator(self.roomId)             #runs the story engine
        allRooms[self.roomId].room_options(self.roomId)         #shows options of where to go
    
    def set_possible_rooms(self, rooms) :
        self.possibleRooms = []
    
    def add_possible_rooms(self, room) :
        self.possibleRooms.append(room)

    def rem_possible_rooms(self, room) :
        self.possibleRooms.remove(room)

    def show_options(self, listOfOptions):
        print("press: ")
        for option in listOfOptions :
            print("a. {0}".format(option))
    
    def exit(self,allRooms):
        if () :
            allRooms[self.roomId].move_to(14)

    def move_to(self, allRooms):
        allRooms[self.roomId].close(self.roomId)
        open(id)

    def narrator(self,items):
        if () :
            items[0].glow()
       
    def room_ambience(self):
        print()

    def room_graphics(self):
        print()
        return

    def close(self):
        print()
