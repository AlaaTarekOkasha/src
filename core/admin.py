from email.headerregistry import Group
from tkinter.tix import TEXT
from tokenize import Token
from django.contrib import admin
from django.forms import TextInput, Textarea
from django.contrib.auth.models import Group
from django.utils.html import format_html
from django.contrib.postgres.fields import ArrayField
from .models import *

admin.site.site_header = 'EYOUTH CMS'
admin.site.site_title = 'CMS'
admin.site.index_title = 'EYOUTH LANDING PAGES'

class CourseLandingPage(admin.ModelAdmin):
    list_display = ('title', 'landing_page')
    def landing_page(self, obj):
        #coursetitle = obj.title.replace(" ", "") 
        return format_html(f'<a href="https://emarketing.eyouthlearning.com/{obj.slug}" class="default"> View Page</a>')
    formfield_overrides = {
    models.TextField: {'widget': Textarea(attrs={'rows':5, 'cols':60})},
    ArrayField: {'widget': Textarea(attrs={'rows':10, 'cols':100})}
    }
    exclude = ('slug',)

class TrainerAdmin(admin.ModelAdmin):
    formfield_overrides = {
    ArrayField: {'widget': Textarea(attrs={'rows':10, 'cols':100})}
}

# Register your models here.
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Testemonial)
admin.site.register(Course, CourseLandingPage)
admin.site.unregister(Group)
