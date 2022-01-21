from django.urls import path

from .views import GameViewSet

urlpatterns = [
    path('games', GameViewSet.as_view({
        'get': 'load',
        'post': 'create'
    })),
    path('games/<str:pk>', GameViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))
]
