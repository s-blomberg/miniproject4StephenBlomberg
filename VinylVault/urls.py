#### INF601 - Advanced Programming in Python
#### Stephen Blomberg
#### Mini Project 4

from django.contrib import admin
from django.urls import include, path

#master url paths

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('collection.urls')),  # Root URL
    path('accounts/', include('django.contrib.auth.urls')),  # Built-in auth URLs
]

