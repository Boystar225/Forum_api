from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


class MessageModel(DateTimeModel):
    topic = models.ForeignKey('topic.TopicModel', related_name='message_topic_ids', on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
        return f"Message de {self.topic.title}"