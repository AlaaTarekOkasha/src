from ckeditor.fields import RichTextField
from django.db import models
from utils import (
    TimeStampModel, 
    DeletedModel, 
    testemonialsImageUpload
)

class TestemonialQuerySet(models.QuerySet):
    def live(self, *args, **kwargs):
        kwargs['is_deleted'] = False
        return super().filter(*args, **kwargs)  

class Testemonials(TimeStampModel, DeletedModel, models.Model):
    name = models.CharField(max_length=150)
    description = RichTextField()
    image = models.ImageField(upload_to = testemonialsImageUpload, null=True)

    objects = TestemonialQuerySet.as_manager()
    
    def __str__(self):
        return self.name