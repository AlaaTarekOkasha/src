from mixer.backend.django import Mixer, GenFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.conf import settings
from django.urls import reverse
from core.models import (
    Courses, 
    Testemonials, 
    Trainers
)

mixer = Mixer(factory=GenFactory)

__all__ = [
    "mixer",
    "APITestCase",
    "status",
    "settings",
    "reverse",

    # models
    "Courses",
    "Testemonials",
    "Trainers"
]