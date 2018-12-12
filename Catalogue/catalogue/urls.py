from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from catalogue.views.CatalogueView import CatalogueViewSet
from catalogue.views.CategoryView import CategoryViewSet

router = DefaultRouter()

router.register(r'catalogue', CatalogueViewSet, 'Catalogue')
router.register(r'category', CategoryViewSet, 'Category')

urlpatterns = [
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)