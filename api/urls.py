from django.urls import path, include
from django.conf import settings


app_name = "api"

urlpatterns = [

    path("", include("core.urls", namespace="core")),
]

if settings.DEBUG:
    from drf_yasg import openapi
    from drf_yasg.views import get_schema_view

    schema_view = get_schema_view(
        openapi.Info(
            title="Landing API",
            default_version='v1'
        ),
        public=True,
    )

    urlpatterns = [
        path("docs/", schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui")
    ] + urlpatterns