from django.contrib import admin
from django.urls import path, include

#this is a refresher
#request method -> http object that is being sent
#the function just returns a simple http response


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    
]