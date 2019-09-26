from django.contrib.auth.models import User
from adventure.models import Player, Room

print("Create world called Cassiopiae")

Room.objects.all().delete()

r_addNewRoom = Room(title="New Room", description="""This is new room...""")

s_segin = Room(title="Epsilon Cassiopeiae (Segin)",
               description="First star in the Cassiopeia Constellation",
               x=100,
               y=400)

s_ruchbah = Room(title="Delta Cassiopeiae (Ruchbah)",
                 description="Second star in the Cassiopeia Constellation",
                 x=150,
                 y=350)

s_navi = Room(title="Gamma Cassiopeiae (Tsih, Navi)",
              description="Third star in the Cassiopeia Constellation",
              x=220,
              y=230)

s_shedar = Room(title="Alpha Cassiopeiae (Shedar",
                description="Fourth star in the Cassiopeia Constellation",
                x=300,
                y=245)

s_caph = Room(title="Beta Cassiopeiae (Caph)",
              description="Fifth star in the Cassiopeia Constellation",
              x=290,
              y=100)

s_segin.save()
s_ruchbah.save()
s_navi.save()
s_shedar.save()
s_caph.save()
r_addNewRoom.save()

# Link rooms together
s_segin.connectRooms(s_ruchbah, "e")
s_ruchbah.connectRooms(s_navi, "n")

s_navi.connectRooms(s_shedar, "e")
s_shedar.connectRooms(s_caph, "n")

players = Player.objects.all()
for p in players:
    p.currentRoom = s_segin.id
    p.save()


# r_outside = Room(title="Outside Cave Entrance",
#                description="North of you, the cave mount beckons")

# r_foyer = Room(title="Foyer", description="""Dim light filters in from the south. Dusty
# passages run north and east.""")

# r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm.""")

# r_narrow = Room(title="Narrow Passage", description="""The narrow passage bends here from west
# to north. The smell of gold permeates the air.""")

# r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south.""")

# r_addNewRoom = Room(title="New Room", description="""This is new room...""")

# r_outside.save()
# r_foyer.save()
# r_overlook.save()
# r_narrow.save()
# r_treasure.save()
# r_addNewRoom.save()

# # Link rooms together
# r_outside.connectRooms(r_foyer, "n")
# r_foyer.connectRooms(r_outside, "s")

# r_foyer.connectRooms(r_overlook, "n")
# r_overlook.connectRooms(r_foyer, "s")

# r_foyer.connectRooms(r_narrow, "e")
# r_narrow.connectRooms(r_foyer, "w")

# r_narrow.connectRooms(r_treasure, "n")
# r_treasure.connectRooms(r_narrow, "s")

# r_outside.connectRooms(r_addNewRoom, 'e')

# players=Player.objects.all()
# for p in players:
#   p.currentRoom=r_outside.id
#   p.save()
