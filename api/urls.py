from django.urls import include, path, re_path
from django.conf.urls import url
from rest_framework.authtoken import views
#from . import api
urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls'))
]




