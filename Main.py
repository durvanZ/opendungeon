import time
from Player import Player
from room import room

print("==========Welcome to Open Dungeon!==========")

name_ = input("Please enter your name: ")
age_ = input("Please enter your age: ")
items_ = []

my_player = Player(name_, age_, 100, items_, 0)
print(my_player.get_name())