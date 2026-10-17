from django.urls import path
from product.views import ProductCreateAPIView, ProductUpdateAPIView, ProductListAPIView


urlpatterns = [
    path("create/", ProductCreateAPIView.as_view()),
    path("update/<int:pk>", ProductUpdateAPIView.as_view()),
    path("", ProductListAPIView.as_view())
]