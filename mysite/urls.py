from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('first/', include('first.urls')),
    path('admin/', admin.site.urls),
]