from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


class TopicModel(DateTimeModel):
    forum = models.ForeignKey('forum.ForumModel', related_name='topic_forum_ids', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    
    