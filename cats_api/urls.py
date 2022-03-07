from django.contrib import admin
from django.urls import path, include
from .docs import documentation_view

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include('cats.urls')),
    path('', include("django_prometheus.urls"), name="django-prometheus"),
    path('docs', documentation_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]
