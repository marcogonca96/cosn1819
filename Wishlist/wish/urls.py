
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from wish.views.WishView import WishViewSet

router = DefaultRouter()

router.register(r'wishlist', WishViewSet, 'Wish')

urlpatterns = [
    path('', include(router.urls))
]