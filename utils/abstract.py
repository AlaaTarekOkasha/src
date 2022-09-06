from django.db import models
from django.utils.timezone import now


class TimeStampModel(models.Model): 
    created_at = models.DateTimeField(default = now, editable=False)
    updated_at = models.DateTimeField(default = now, editable=False)
    class Meta: 
        abstract = True 


class DeletedModel(models.Model): 
    is_deleted = models.BooleanField(default = False)
    deleted_at = models.DateTimeField(default = now, editable=False)
    class Meta: 
        abstract = True