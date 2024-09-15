from django.urls import path, include
from rest_framework import routers
from .viewsets import forum_viewset, message_viewset, topic_viewset


router = routers.DefaultRouter()
router.register(r'forums', forum_viewset.ForumViewset, basename="forums")
router.register(r'topics', topic_viewset.TopicViewSet, basename="topics")
router.register(r'messages', message_viewset.MessageViewSet, basename="messages")

app_name ='api'

urlpatterns = [
    path('', include(router.urls)),
]
