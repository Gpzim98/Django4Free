from django.contrib import admin
from django.urls import path, include
from .views import home, detail, save, update, delete

urlpatterns = [
    path('', home),
    path('save/', save, name="save"),
    path('detail/<int:id>', detail, name='detail'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
]
