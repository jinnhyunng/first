from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mysite/', include('mysite.urls')),
]

from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
]