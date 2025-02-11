from django.urls import path
from .chat_consumers import ChatConsumer
from . import views

app_name='chatapp'


urlpatterns = [
    
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
    path('direct',views.DirectMessage.as_view(),name='messages'),

]
