from django.contrib import admin
from django.urls import path
from univtalk_main import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('message',main.Message),
	path('keyboard/',main.Keyboard),
]
