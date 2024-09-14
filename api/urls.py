from django.urls import path, include
from rest_framework import routers
from .viewsets.forum_viewset import ForumViewset
from .viewsets.message_viewset import MessageViewSet
from .viewsets.sujet_viewset import SujetViewSet

routers = routers.DefaultRouter()
routers.register(r'forums', ForumViewset, basename="forums")
routers.register(r'sujets', SujetViewSet, basename="sujets")
routers.register(r'messages', MessageViewSet, basename="messages")

app_name ='api'

urlpatterns = [
    path('', include(routers.urls)),
]
