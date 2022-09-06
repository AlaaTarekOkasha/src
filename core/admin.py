from django.contrib import admin
# from .forms import TestemonialsForm, TrainerForm
# from django.db import models
from .models import *
# from email.headerregistry import Group
# from tkinter.tix import TEXT
# from tokenize import Token
# from django.forms import TextInput, Textarea
# from django.contrib.auth.models import Group
from django.utils.html import format_html
# from django.contrib.postgres.fields import ArrayField
# from .models import *

admin.site.site_header = 'EYOUTH CMS'
admin.site.site_title = 'CMS'
admin.site.index_title = 'EYOUTH LANDING PAGES'


@admin.register(Courses)
class CourseLandingPage(admin.ModelAdmin):
    list_display = ('title', 'landing_page')
    filter_horizontal = ("trainers", "testemonials")

    fieldsets = (
        ("Course Info", {"fields": ("title", "description", "image", "price" , 
                                    "hours", "start_date", "content", 
                                    "course_benefits", "user_criteria", "trainers", "testemonials")}),
    )
    add_fieldsets = (
        ("Course Info", {"fields": ("title", "description", "image", "price" , 
                                    "hours", "start_date", "content", 
                                    "course_benefits", "user_criteria", "trainers", "testemonials")}),
    )

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)

    def landing_page(self, obj):
        #coursetitle = obj.title.replace(" ", "") 
        return format_html(f'<a href="https://emarketing.eyouthlearning.com/{obj.slug}" class="default"> View Page</a>')
    # formfield_overrides = {
    #     models.TextField: {'widget': Textarea(attrs={'rows':5, 'cols':60})},
    #     ArrayField: {'widget': Textarea(attrs={'rows':10, 'cols':100})}
    # }
    exclude = ('slug',)

# class TrainerAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#     ArrayField: {'widget': Textarea(attrs={'rows':10, 'cols':100})}
# }

# # Register your models here.
# admin.site.register(Trainer, TrainerAdmin)
# admin.site.register(Testemonial)
# admin.site.register(Course, CourseLandingPage)
# admin.site.unregister(Group)
@admin.register(Trainers)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name',)

    fieldsets = (
        ("Trainer Info", {"fields": ("name", "description", "image")}),
    )
    add_fieldsets = (
        ("Trainer Info", {"fields": ("name", "description", "image")}),
    )

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)


@admin.register(Testemonials)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('description',)

    fieldsets = (
        ("Testimonial Info", {"fields": ("name", "description", "image")}),
    )
    add_fieldsets = (
        ("Testimonial Info", {"fields": ("name", "description", "image")}),
    )

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)
