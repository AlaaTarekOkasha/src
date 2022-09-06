from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static  
from core.views import *
# from rest_framework.authtoken.views import obtain_auth_token
# from core import views
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    # re_path(r'^rest-auth/', include('dj_rest_auth.urls')),
    # path('api/token/', obtain_auth_token, name='obtain-token'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/v1/', include("api.urls", namespace="api")),
    
    # path('api/v1/course/view/', CourseView.as_view(), name='course-view'),
    # path('api/v1/content/view/', ContentView.as_view(), name='content-view'),
    # path('api/v1/course-benefits/view/', EndContentView.as_view(), name='course-benefits-view'),
    # path('api/v1/criteria/view/', UserCriteriaView.as_view(), name='criteria-view'),
    # path('api/v1/trainer/view/', TrainerView.as_view(), name='trainer-view'),
    # path('api/v1/testemonial/view/', TestemonialView.as_view(), name='testemonial-view'),
]

if os.environ.get('DJANGO_SETTINGS_MODULE').rsplit('.', 1)[1] == 'local':
    from django.conf import settings
    from django.conf.urls.static import static
    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)