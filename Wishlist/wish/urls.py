from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from wish.views.WishView import WishViewSet

router = DefaultRouter()

router.register(r'wish', WishViewSet, 'Wish')

urlpatterns = [
    path('', include(router.urls))
]