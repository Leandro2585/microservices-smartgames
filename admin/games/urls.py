from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('games/', GameViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('games/<str:pk>', GameViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))
]
