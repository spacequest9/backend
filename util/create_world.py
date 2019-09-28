from django.contrib.auth.models import User
from adventure.models import Player, Room

import random

print("Create world called...")
roomDict= {}
i = 1
with open("util/data") as f:
    for line in f:
        x = line.split(":")
        print (x)
        title = x[0]
        description = x[1]
        room = Room(title=title, description= description)
        roomDict[i] = room
        i += 1

roomIds = roomDict.keys()
random.shuffle(roomIds)
for i in range(1, len(roomIds)//2):
    room1 = roomDict[i]
    room2 = roomDict[i+1]
    room1.e_to = room2
    room2.w_to = room1

random.shuffle(roomIds)
for i in range(1, len(roomIds)//2):
    room1 = roomDict[i]
    room2 = roomDict[i+1]
    room1.n_to = room2
    room2.s_to = room1

# for i, room in roomDict.items():
#     room.save()

Room.objects.all().delete()

r_outside = Room(title="Outside Cave Entrance",
               description="North of you, the cave mount beckons")

r_foyer = Room(title="Foyer", description="""Dim light filters in from the south. Dusty
passages run north and east.""")

r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

r_narrow = Room(title="Narrow Passage", description="""The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_addNewRoom = Room(title="New Room", description="""This is new room...""")

r_outside.save()
r_foyer.save()
r_overlook.save()
r_narrow.save()
r_treasure.save()
r_addNewRoom.save()

# Link rooms together
r_outside.connectRooms(r_foyer, "n")
r_foyer.connectRooms(r_outside, "s")

r_foyer.connectRooms(r_overlook, "n")
r_overlook.connectRooms(r_foyer, "s")

r_foyer.connectRooms(r_narrow, "e")
r_narrow.connectRooms(r_foyer, "w")

r_narrow.connectRooms(r_treasure, "n")
r_treasure.connectRooms(r_narrow, "s")

r_outside.connectRooms(r_addNewRoom, 'e')

players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()

