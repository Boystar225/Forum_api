from django.db import models
from forum.models.forum_model import ForumModel

class SujetModel(models.Model):
    forum = models.ForeignKey(ForumModel, related_name='sujets', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    