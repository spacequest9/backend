from django.contrib.auth.models import User
from adventure.models import Player, Room

import random

def createWorld():
    #For tesing purpose
    # class Room:
    #     def __init__(self, title, description, locx, locy):
    #         self.id = id
    #         self.title = title
    #         self.description = description
    #         self.n_to = None
    #         self.s_to = None
    #         self.e_to = None
    #         self.w_to = None
    #         self.locx = locx
    #         self.locy = locy
    #     def __repr__(self):
    #         string = self.title + " > " + self.description
    #         if self.n_to:
    #             string += "n:" + self.n_to.title
    #         if self.s_to:
    #             string += "s:" + self.s_to.title
    #         if self.e_to:
    #             string += "e:" + self.e_to.title
    #         if self.w_to:
    #             string += "w:" + self.w_to.title
    #
    #         return string
    #
    #
    #     def connect_rooms(self, connecting_room, direction):
    #         '''
    #         Connect two rooms in the given n/s/e/w direction
    #         '''
    #         reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}
    #         reverse_dir = reverse_dirs[direction]
    #         setattr(self, f"{direction}_to", connecting_room)
    #         setattr(connecting_room, f"{reverse_dir}_to", self)
    #     def get_room_in_direction(self, direction):
    #         '''
    #         Connect two rooms in the given n/s/e/w direction
    #         '''
    #         return getattr(self, f"{direction}_to")


    print("create_world called")
    Room.objects.all().delete()


    #Read data from file and keep in dictonary
    #Dictionary key : running number, starting from 1
    #Dictionary value : tuple of title and description read from data fle
    i = 1
    dataFromFile = {}
    with open("util/data") as f:
        for line in f:
            x = line.split(":")
            print (x)
            title = x[0]
            description = x[1]
            dataFromFile[i] = (title, description)
            i += 1


    #
    #We will create a dictionary of rooms
    #dRoooms key (x,y) cordinates of room
    #dRooms value is the Room object at coordinates (x,y)
    dRooms = {}

    #Counters to track how many links were skipped
    totalSouthSkipped = 0
    totalWestSkipped = 0

    #We are going to place rooms on co-odrinates starting from (100,100)
    #We will go right and up by 25 points.
    #So, first room coordinate is (100,100). Next room in same row will be (125, 100), (150, 100) and so on. Last room
    # in this row will be (350,100)
    #After being done this row, we move to next row above this, which has first room at (100, 125). Its next room will
    # be (125, 125), (150, 125) and so on.
    #This will we keep going up until last row, whose first room will be (100, 350).
    #

    startx, starty, distance = 100,100,25

    #Index to read data from dataFromFile
    dataFileIndex = 1
    for i in range(0, 10): #For each row
        #We are in row number i. So, y cordinate is fixed at 100 + i*25
        #now we will go through each column of this ith row, and set x co-ordinates and create room
        y = starty + i*distance
        for j in range(0,10):
            #X, y co-ordinates of room
            x = startx + j*distance

            #We have x,y co-oridinate to create a room

            print ("Date from file", (dataFromFile[dataFileIndex]))
            #Create room based on title, description, x and y co-ordinates
            room = Room(title = dataFromFile[dataFileIndex][0], description =dataFromFile[dataFileIndex][1], locx = x, locy=y)
            dRooms[(x,y)] = room

            #Connect this room to its neghbour

            #First look north room, which is x, y + 25, but it should exist
            # if y + 25 <= 350:
            #     if (x, y + 25) in dRooms:
            #         northRoom = dRooms[(x, y + 25)]
            #         room.n_to = northRoom
            #         northRoom.s_to = room

            # Look south which is 100,100, south is x, y-25
            if  y-distance >= starty:
                if random.randint(1,10) in (1,2,3,4,5,6,7,8):#Skip 20% of souths
                    southRoom =  dRooms[(x, y - distance)]
                    room.s_to = southRoom
                    southRoom.n_to = room
                else:
                    print("Skip adding south")
                    totalSouthSkipped += 1

            # # Look each which is x+25,y and should exist
            # if x +25 <= 350:
            #     if (x - 35, y) in dRooms:
            #         westRoom = dRooms[(x - 35, y)]
            #     room.w_to = westRoom
            #     westRoom.w_to = room

            #Look west which is x+25,y and should exist
            if x-distance >= startx:
                if random.randint(1, 10) in (1, 2, 3, 4, 5, 6, 7,8):#Skip 20% of west
                    westRoom =dRooms[(x-distance,y)]
                    room.w_to=westRoom
                    westRoom.e_to= room
                else:
                    print("Skip adding west")
                    totalWestSkipped += 1

            dataFileIndex += 1

    for cord, room in dRooms.items():
        print(cord, ":", room)
        room.save()

    print("Total Skipped ", totalSouthSkipped , totalWestSkipped)

    players=Player.objects.all()
    for p in players:
      p.currentRoom=dRooms[0].id
      p.save()

#
#
#
# print("Create world called...")
# roomDict= {}
# i = 1
# with open("util/data") as f:
#     for line in f:
#         x = line.split(":")
#         print (x)
#         title = x[0]
#         description = x[1]
#         room = Room(title=title, description= description)
#         roomDict[i] = room
#         i += 1
#
# roomIds = roomDict.keys()
# random.shuffle(roomIds)
# for i in range(1, len(roomIds)//2):
#     room1 = roomDict[i]
#     room2 = roomDict[i+1]
#     room1.e_to = room2
#     room2.w_to = room1
#
# random.shuffle(roomIds)
# for i in range(1, len(roomIds)//2):
#     room1 = roomDict[i]
#     room2 = roomDict[i+1]
#     room1.n_to = room2
#     room2.s_to = room1
#
# for i, room in roomDict.items():
#     room.save()


#
# r_outside = Room(title="Outside Cave Entrance",
#                description="North of you, the cave mount beckons", locx=100, locy=400)
#
# r_foyer = Room(title="Foyer", description="""Dim light filters in from the south. Dusty
# passages run north and east.""", locx=150, locy=350)
#
# r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm.""", locx=220, locy=230)
#
# r_narrow = Room(title="Narrow Passage", description="""The narrow passage bends here from west
# to north. The smell of gold permeates the air.""", locx=300, locy=245)
#
# r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south.""", locx=290, locy=100)
#
# r_outside.save()
# r_foyer.save()
# r_overlook.save()
# r_narrow.save()
# r_treasure.save()
#
# # Link rooms together
# r_outside.connectRooms(r_foyer, "n")
# r_foyer.connectRooms(r_outside, "s")
#
# r_foyer.connectRooms(r_overlook, "n")
# r_overlook.connectRooms(r_foyer, "s")
#
# r_foyer.connectRooms(r_narrow, "e")
# r_narrow.connectRooms(r_foyer, "w")
#
# r_narrow.connectRooms(r_treasure, "n")
# r_treasure.connectRooms(r_narrow, "s")

# players=Player.objects.all()
# for p in players:
#   p.currentRoom=roomDict[0].id
#   p.save()

