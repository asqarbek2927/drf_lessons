from django.urls import path
from about.views import get_about, create_about, detail_about

urlpatterns = [
    path("", get_about),
    path("create/", create_about),
    path("detail/<int:pk>", detail_about),
]
