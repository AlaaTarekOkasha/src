from ckeditor.fields import RichTextField
from django.db import models
from utils import (
    TimeStampModel, 
    DeletedModel, 
    trainersImageUpload
)


class TrainerQuerySet(models.QuerySet):
    def live(self, *args, **kwargs):
        kwargs['is_deleted'] = False
        return super().filter(*args, **kwargs) 

class Trainers(TimeStampModel, 
               DeletedModel, 
               models.Model):

    name = models.CharField(max_length=150, unique=True)
    description = RichTextField()
    image = models.ImageField(upload_to = trainersImageUpload, null=True)
    
    objects = TrainerQuerySet.as_manager()
    
    def __str__(self):
        return self.name