from multiprocessing.util import abstract_sockets_supported
from venv import create
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timezone import now
from django.contrib.postgres.fields import ArrayField
from django.utils.text import slugify

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
    description = ArrayField(models.TextField(max_length=1000000, null=True,),help_text='Please use ( , ) to add a new bullet point. Example: Educaction is important, Health is wealth')
    image = models.ImageField(upload_to = trainersImageUpload, null=True)
    objects = ModelsQs.as_manager()
    
    def __str__(self):
        return self.name
# ----------------------------------------------------------------------------------------------------------

class Testemonial(DeletedAbstract, TimeStamp, models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=1000000)
    image = models.ImageField(upload_to = testemonialsImageUpload, null=True)
    objects = ModelsQs.as_manager()
    
    def __str__(self):
        return self.name
# ----------------------------------------------------------------------------------------------------------

class Course(DeletedAbstract, TimeStamp, models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=250, unique=True, null=True, blank=True, help_text='Note: Slug must be in English and consist of letters, numbers or underscores. Slug will appear in the course URL. >> Example: Course Title is ( Programming Course ) or ( كورس البرمجة ) - Slug must be ( programing-course ) and Course URL will be ( https://emarketing.eyouthlearning.com/programing-course )')
    description = models.TextField(max_length=1000000)
    image = models.ImageField(upload_to = courseImageUpload, null=True)
    price = models.IntegerField()
    hours = models.IntegerField()
    start_date = models.DateField(blank=True, null=True)
    content = ArrayField(models.TextField(max_length=1000000,),help_text='Please use ( , ) to add a new bullet point. Example: Educaction is important, Health is wealth')
    course_benefits = ArrayField(models.TextField(max_length=1000000,), help_text='Please use ( , ) to add a new bullet point. Example: Educaction is important, Health is wealth')
    user_criteria = ArrayField(models.TextField(max_length=1000000,), help_text='Please use ( , ) to add a new bullet point. Example: Educaction is important, Health is wealth')
    trainers = models.ManyToManyField(Trainer, related_name="trainers")
    testemonials = models.ManyToManyField(Testemonial, related_name="testemonials")
    objects = ModelsQs.as_manager()

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     value = self.title
    #     self.slug = slugify(value, allow_unicode=True)
    #     super().save(*args, **kwargs)

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