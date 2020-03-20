from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()
router.register('Hello-viewset', views.HelloViewSet, base_name='hello_viewset')


urlpatterns = [
    path('hello-view/', views.HelloBolonhaAPIView.as_view()),
    path('', include(router.urls))
]
