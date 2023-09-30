from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("myintro.urls")),
    path("admin/", admin.site.urls),
]