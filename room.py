import item.py 
class Room:
    allRooms = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]         #Static attributes (not specific to each room)

    def __init__(self, id)     #defining the class (constructor)
        self.id = id                #attributes of the class specific to each room
        self.possibleRooms = []
        if room.id == 1 : items = []
        if room.id == 2 : items = []
        if room.id == 3 : items = []
        if room.id == 4 : items = []
        if room.id == 5 : items = []
        if room.id == 6 : items = []
        if room.id == 7 : items = []
        if room.id == 8 : items = []
        if room.id == 9 : items = []
        if room.id == 10 : items = []
        if room.id == 11 : items = []
        if room.id == 12 : items = []
        if room.id == 13 : items = []

    def open():                #will run when player enters the room using room.get(id).open() method
        room_graphics()        #will run graphics method
        room_ambience()        #will run ambience method
        print("you have entered room {0}".format(id))        
        narrator()             #runs the story engine
        show_options()         #shows options of where to go
    
    def set_possible_rooms() :
    
    def add_possible_rooms() :
    
    def rem_possible_rooms() :

    def show_options(listOfOptions):
        print("press: ")
        for option in listOfOptions :
            print("a. {0}".format(option))
    
    def exit()
        if :
            move_to(14)

    def move_to(id)

    def narrator()
    if :
    items[0].glow()
    if :
    if :
    else :

    def room_ambience()

    def room_graphics()

