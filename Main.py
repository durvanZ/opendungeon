import time
from Player import Player
from room import room
from item import item
import hangman
import Cipher
import quiz

print("==========Welcome to Open Dungeon!==========")

name_ = input("Please enter your name: ")
age_ = input("Please enter your age: ")
items_ = []

my_player = Player(name_, age_, 100, items_, 0)
#print(my_player.get_name())

string1 = 'It’s a dark, cold, and rainy Halloween night, you dress up as your all time favourite horror character, Pennywise. As you’re walking on the street, proudly looking at your costume on the reflection of the window nearby, you stumble upon an old, spooky haunted house (perfectly fit Halloween style). The house looks even spookier under the stormy weather. Normally, you would be scared to death and run away as fast as you could. However, having this Pennywise costume on gives you extra brevity, plus, it’s Halloween! So you take all of your courage, push the heavy wooden door. The door creaks open as it is pushed inside, a cold wind comes right at you along with a sardonic laugh'
string2 = '\nThe wooden floor makes a loud creak whenever you walk. You light up a lighter you found on the floor. However, since everything is so dark, you can barely see anything. As you take the next step, the floor made out a loud crack. Before you could realize anything, everything went dark ...'
string3 = '\nYou wake up in an underground with a huge hallway full of doors. Chills send through your spine as the cold wind and hysteric laugh again appear. Holding up the lighter, you see a total of 13 doors. You walk towards a door and open it. You choose door ...'
print(string1 + string2)

current_room = []
for i in range(13):
    current_room[room(i)]

current_room = input(string3)
print(f"Room {my_player.get_current_room}")

current_room[my_player.get_current_room()].Open()
