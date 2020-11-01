import time
from Player import Player
from room import room
from item import item

print("==========Welcome to Open Dungeon!==========")

name_ = input("Please enter your name: ")
age_ = input("Please enter your age: ")
items_ = []

my_player = Player(name_, age_, 100, items_, 0)
#print(my_player.get_name())

string1 = 'On one fateful Halloween night, you have been captured by a mysterious figure and thrown into a locked room inside a haunted house'
print(string1)

current_room = []
for i in range(13):
    current_room[room(i)]

print("You enter the room")

current_room[my_player.get_current_room()].Open()
