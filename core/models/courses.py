from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from django.db import models
from utils import (
    DeletedModel,
    TimeStampModel,
    courseImageUpload
)


class CoursesQuerySet(models.QuerySet):
    def live(self, *args, **kwargs):
        kwargs['is_deleted'] = False
        return super().filter(*args, **kwargs) 


class Courses(TimeStampModel, 
              DeletedModel, 
              models.Model):

    title = models.CharField(max_length=150, unique=True)
    slug = AutoSlugField(populate_from="title", unique=True)
    description = models.TextField(max_length=1000000)
    image = models.ImageField(upload_to = courseImageUpload, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    hours = models.IntegerField()
    start_date = models.DateField(null=True, blank=True)
    content = RichTextField()
    course_benefits = RichTextField()
    user_criteria = RichTextField()
    trainers = models.ManyToManyField("core.Trainers", related_name="trainers")
    testemonials = models.ManyToManyField("core.Testemonials", related_name="testemonials")

    objects = CoursesQuerySet.as_manager()

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

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