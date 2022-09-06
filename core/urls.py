from django.urls import path
from .views import *

app_name = "core"

urlpatterns = [

    path("course/view/", CourseView.as_view(), name="list_courses"),
    path("trainer/view/", TrainerView.as_view(), name="list_trainers"),
    path("testemonial/view/", TestemonialView.as_view(), name="list_testimonials"),
    
]