from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path("category/", include("category.urls")),
        path("product/", include("product.urls")),
        path("about/", include("about.urls"))
    ]))
]
