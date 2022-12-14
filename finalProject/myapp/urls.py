from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *

urlpatterns = [
    path("api/v1/pro-list", ProductsListAPIView.as_view()),
    path("api/v1/cat-list", CategoriesListAPIView.as_view()),
    path("api/v1/subcat-list/<int:pk>", SubCategoriesListAPIView.as_view()),
    path("api/v1/subcat-list", SubCategoriesListAPIView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
