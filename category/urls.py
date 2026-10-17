from django.urls import path

from category.views import CategoryCreateAPIVIew, CategoryListAPIView, CategoryUpdateAPIView

urlpatterns = [
    path("", CategoryListAPIView.as_view()),
    path("create/", CategoryCreateAPIVIew.as_view()),
    path("update/<int:pk>", CategoryUpdateAPIView.as_view()),
]