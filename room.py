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

        def open():                #will run when player enters the room using room.get(id).open() method
            room_graphics()        #will run graphics method
            room_ambience(roomId)        #will run ambience method
            print("you have entered room {0}".format(id))        
            room.narrator(roomId)             #runs the story engine
            room.show_options(roomId)         #shows options of where to go
    
        def set_possible_rooms(rooms) :
            self.possibleRooms = []
    
        def add_possible_rooms(room) :
            self.possibleRooms.append(room)

        def rem_possible_rooms(room) :
            self.possibleRooms.remover(room)

        def show_options(listOfOptions):
            print("press: ")
            for option in listOfOptions :
                print("a. {0}".format(option))
    
        def exit():
            if () :
                move_to(14)

        def move_to(id):
            close(self.id)
            open(id)

        def narrator():
            if () :
                items[0].glow()
       
        def room_ambience():
            print()

        def room_graphics():
            print()
            return

        def close():
            print()

