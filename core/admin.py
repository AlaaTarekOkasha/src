from email.headerregistry import Group
from tokenize import Token
from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.html import format_html
from .models import *

admin.site.site_header = 'EYOUTH CMS'
admin.site.site_title = 'CMS'
admin.site.index_title = 'EYOUTH LANDING PAGES'

class ContentAdmin(admin.ModelAdmin):
    list_display = ('course', 'description')
    list_filter = ('course',)

class EndContentAdmin(admin.ModelAdmin):
    list_display = ('course', 'description')
    list_filter = ('course',)

class UserCriteriaAdmin(admin.ModelAdmin):
    list_display = ('course', 'description')
    list_filter = ('course',)

class CourseLandingPage(admin.ModelAdmin):
    list_display = ('title', 'landing_page')
    def landing_page(self, obj): 
        return format_html(f'<a href="https://emarketing.eyouthlearning.com/{obj.id}" class="default"> View Page</a>')

# Register your models here.
admin.site.register(Trainer)
admin.site.register(Testemonial)
admin.site.register(Course, CourseLandingPage)
admin.site.register(Content, ContentAdmin)
admin.site.register(CourseBenefit, EndContentAdmin)
admin.site.register(UserCriteria, UserCriteriaAdmin)
admin.site.unregister(Group)
