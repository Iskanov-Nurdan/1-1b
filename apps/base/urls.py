from django.urls import path
from apps.base import views

urlpatterns = [
    path("", views.name_list, name="name_list")
]