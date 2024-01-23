
from django.contrib import admin
from django.urls import path
from tarjimon.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , home_page , name='home')

]
