from django.contrib.auth.models import User
from adventure.models import Player, Room


def create():
  print("Create star system...")

  Room.objects.all().delete()

  # create rooms
  epsilon_lyrae = Room(title="Epsilon Lyrae", 
                      description="Famously known as being a double star – two stars in one with each star is also a double. The double double star!", 
                      locx=250, 
                      locy=60)
  alpha_lyrae = Room(title="Alpha Lyrae (Vega, Fidis, Harp Star)", 
                      description="Brightest star in Lyra constellation and the fifth brightest star in the sky.", 
                      locx=308, 
                      locy=110)
  zeta1_lyrae = Room(title="Zeta1 Lyrae", 
                      description="Contains as many as 7 individual stars. However is often over looked by near by neighbors.", 
                      locx=288, 
                      locy=168)
  delta2_lyrae = Room(title="Delta2 Lyrae", 
                      description="Pulsating luminous giant star consisting of one super hot blue star, next to a yellow star.", 
                      locx=187, 
                      locy=183)
  gamma_lyrae = Room(title="Gamma Lyrae (Sulafat)", 
                      description="Second-brightest star in the northern constellation and can be seen with the naked eye from Earth.", 
                      locx=147, 
                      locy=338)
  beta_lyrae = Room(title="Beta Lyrae", 
                      description="'Made of 2 stars that are so close that their shapes are heavily distorted by mutual gravitation forces: the stars have ellipsoidal shapes.", 
                      locx=236, 
                      locy=325)

  # save newly created rooms
  epsilon_lyrae.save()
  alpha_lyrae.save()
  zeta1_lyrae.save()
  delta2_lyrae.save()
  gamma_lyrae.save()
  beta_lyrae.save()

  # create links between rooms
  epsilon_lyrae.connectRooms(alpha_lyrae, "s")

  alpha_lyrae.connectRooms(epsilon_lyrae, "n")
  alpha_lyrae.connectRooms(zeta1_lyrae, "s")

  zeta1_lyrae.connectRooms(alpha_lyrae, "n")
  zeta1_lyrae.connectRooms(beta_lyrae, "s")
  zeta1_lyrae.connectRooms(delta2_lyrae, "w")

  delta2_lyrae.connectRooms(gamma_lyrae, "s")
  delta2_lyrae.connectRooms(zeta1_lyrae, "e")

  gamma_lyrae.connectRooms(delta2_lyrae, "n")
  gamma_lyrae.connectRooms(beta_lyrae, "e")

  beta_lyrae.connectRooms(zeta1_lyrae, "n")
  beta_lyrae.connectRooms(gamma_lyrae, "w")

  # reset all players to starting room
  players=Player.objects.all()
  for p in players:
    p.currentRoom=epsilon_lyrae.id
    p.save()
