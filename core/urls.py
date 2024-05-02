from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static




schema_view = get_schema_view(
   openapi.Info(
      title="Fast Food API",
      default_version='v1',
      description="Fast Food",
      terms_of_service="https://www.github.com/quvvatullayev",
      contact=openapi.Contact(email="quvvatullayev@gmil.com"),
      license=openapi.License(name="Uzbekston Samarqand"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('bus_ip/', include('bus_ip.urls')),
    path('auth/', include('rest_framework.urls'), name='auth'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
