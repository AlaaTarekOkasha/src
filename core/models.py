from multiprocessing.util import abstract_sockets_supported
from venv import create
from django.contrib.auth import get_user_model
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.timezone import now
User = get_user_model()

class TimeStamp(models.Model): 
    created_at = models.DateTimeField(default = now, editable=False)
    updated_at = models.DateTimeField(default = now, editable=False)
    class Meta: 
        abstract = True 

class DeletedAbstract(models.Model): 
    is_deleted = models.BooleanField(default = False)
    deleted_at = models.DateTimeField(default = now, editable=False)
    class Meta: 
        abstract = True
    
class ModelsQs(models.QuerySet):
    def live(self, *args, **kwargs):
        kwargs['is_deleted'] = False
        return super().filter(*args, **kwargs)

class Trainers(DeletedAbstract, TimeStamp, models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = RichTextField()
    image = RichTextUploadingField()
    objects = ModelsQs.as_manager()
    
    def __str__(self):
        return self.name

class Testemonials(DeletedAbstract, TimeStamp, models.Model):
    name = models.CharField(max_length=150)
    description = RichTextField()
    image = RichTextUploadingField()
    objects = ModelsQs.as_manager()
    
    def __str__(self):
        return self.name

class Courses(DeletedAbstract, TimeStamp, models.Model):
    title = models.CharField(max_length=150, unique=True)
    description = RichTextField()
    image = RichTextUploadingField()
    price = models.CharField(max_length=150)
    content = RichTextField(default ="None")
    end_content = RichTextField(default ="None")
    criteria = RichTextField(default ="None")
    trainers = models.ManyToManyField(Trainers, related_name="trainers")
    testemonials = models.ManyToManyField(Testemonials, related_name="testemonials")
    objects = ModelsQs.as_manager()

    def __str__(self):
        return self.title

    @property
    def trainers_list(self):
        return [{
            "name": i.name,
            "description": i.description,
            "image": i.image
        } for i in self.trainers.all()]

    @property
    def testemonials_list(self):
        return [{
            "name": i.name,
            "description": i.description,
            "image": i.image
        } for i in self.testemonials.all()]
