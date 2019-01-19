from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from wish.views.WishView import WishViewSet

router = DefaultRouter()

router.register(r'wishlist', WishViewSet, 'Wish')

urlpatterns = [
    url(r'^wish/users/$', WishViewSet.as_view({'get': 'get_user_email'})),
    path('', include(router.urls))
]