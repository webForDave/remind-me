from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("create/", views.create_capsule, name="create_capsule"),
    path("<str:title>/detail", views.capsule_detail, name="capsule_detail"),
    path("<str:title>/update", views.update_capsule, name="update_capsule"),
]