from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view
from rest_framework import permissions

documentation_view = get_schema_view(
    openapi.Info(
        title="Cats API",
        default_version="v0",
        description="Cats API documentation page",
        contact=openapi.Contact(email="math.lima.andrade@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
