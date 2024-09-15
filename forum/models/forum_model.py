from django.db import models
from base.models.helpers.named_date_time_model import NamedDateTimeModel


class ForumModel(NamedDateTimeModel):
    description = models.TextField()
    
    