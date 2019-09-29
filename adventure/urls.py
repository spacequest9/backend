from django.conf.urls import url
from . import api

urlpatterns = [
    url('createworld', api.createworld),
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
    url('rooms', api.getRooms),
     #url('room', api.addRooms),
]