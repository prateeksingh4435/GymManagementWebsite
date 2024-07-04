from django.contrib import admin
from django.urls import path , include
from gym.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('gym.urls'))
]