from multiprocessing.util import abstract_sockets_supported
from venv import create
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timezone import now

User = get_user_model()

def courseImageUpload(instance, fileName):
    return f'uploads/courses/{fileName}'

def trainersImageUpload(instance, fileName):
    return f'uploads/trainers/{fileName}'

def testemonialsImageUpload(instance, fileName):
    return f'uploads/testemonials/{fileName}'
# ----------------------------------------------------------------------------------------------------------

class TimeStamp(models.Model): 
    created_at = models.DateTimeField(default = now, editable=False)
    updated_at = models.DateTimeField(default = now, editable=False)
    class Meta: 
        abstract = True 
# ----------------------------------------------------------------------------------------------------------

class DeletedAbstract(models.Model): 
    is_deleted = models.BooleanField(default = False)
    deleted_at = models.DateTimeField(default = now, editable=False)
    class Meta: 
        abstract = True
# ----------------------------------------------------------------------------------------------------------

class ModelsQs(models.QuerySet):
    def live(self, *args, **kwargs):
        kwargs['is_deleted'] = False
        return super().filter(*args, **kwargs) 
# ----------------------------------------------------------------------------------------------------------

class Trainer(DeletedAbstract, TimeStamp, models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=1000000)
    image = models.ImageField(upload_to = trainersImageUpload, null=True)
    objects = ModelsQs.as_manager()
    
    def __str__(self):
        return self.name
# ----------------------------------------------------------------------------------------------------------

class Testemonial(DeletedAbstract, TimeStamp, models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1000000)
    image = models.ImageField(upload_to = testemonialsImageUpload, null=True)
    objects = ModelsQs.as_manager()
    
    def __str__(self):
        return self.name
# ----------------------------------------------------------------------------------------------------------

class Course(DeletedAbstract, TimeStamp, models.Model):
    title = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=1000000)
    image = models.ImageField(upload_to = courseImageUpload, null=True)
    price = models.IntegerField()
    hours = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    trainers = models.ManyToManyField(Trainer, related_name="trainers")
    testemonials = models.ManyToManyField(Testemonial, related_name="testemonials")
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
# ----------------------------------------------------------------------------------------------------------

class Content(DeletedAbstract, TimeStamp, models.Model):
    course = models.ForeignKey(Course, related_name='content_list', on_delete = models.CASCADE)
    description = models.CharField(max_length=1000000)
    objects = ModelsQs.as_manager()
    
    def __str__(self):
        return '%s' % (self.description)
# ----------------------------------------------------------------------------------------------------------

class EndContent(DeletedAbstract, TimeStamp, models.Model):
    course = models.ForeignKey(Course, related_name='end_content_list', on_delete = models.CASCADE)
    description = models.CharField(max_length=1000000)
    objects = ModelsQs.as_manager()
    
    def __str__(self):
        return '%s' % (self.description)
# ----------------------------------------------------------------------------------------------------------

class UserCriteria(DeletedAbstract, TimeStamp, models.Model):
    course = models.ForeignKey(Course, related_name='user_criteria_list', on_delete = models.CASCADE)
    description = models.CharField(max_length=1000000)
    objects = ModelsQs.as_manager()
    
    def __str__(self):
        return '%s' % (self.description)
# ----------------------------------------------------------------------------------------------------------
