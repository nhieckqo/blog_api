from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'posts/<pk>/comments/', views.PostViewSet.as_view({'get':'comment','post':'comment'})),
    path(r'posts/<pk>/comments/<comment>/', views.PostViewSet.as_view({'delete':'remove_comment'})),
    ]
