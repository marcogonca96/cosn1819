from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from login.views.Auth import AuthViewSet

router = DefaultRouter()

#router.register(r'products/acknowledge', MasterdataProducts3PLViewSet, 'Products3PL')

urlpatterns = [
    url(r'login/', AuthViewSet.as_view({'post': 'login'}), name='login'),
    path('', include(router.urls))
]
