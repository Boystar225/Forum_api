from django.db import models
from sujet.models.sujet_model import SujetModel

class MessageModel(models.Model):
    topic = models.ForeignKey(SujetModel, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message de {self.topic.title}"