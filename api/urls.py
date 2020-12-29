from django.urls import path


app_name = 'api'

from . views import (
    RoomView,
)


urlpatterns = [
    path('',RoomView.as_view(), name='main'),
]
