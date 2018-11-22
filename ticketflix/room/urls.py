from django.conf import settings
from django.urls import include, path
from django.views.generic import TemplateView
from django.views import defaults as default_views

from .views import *

urlpatterns = [
    path('', RoomList.as_view(template_name='room/room_list.html'), name='room_list'),
    path('view/<int:pk>', RoomView.as_view(template_name='room/room_view.html'), name='room_view'),
    path('new', RoomCreate.as_view(template_name='room/room_form.html'), name='room_new'),
    path('edit/<int:pk>', RoomUpdate.as_view(template_name='room/room_form.html'), name='room_edit'),
    path('delete/<int:pk>', RoomDelete.as_view(template_name='room/room_delete.html'), name='room_delete'),
    path('add_seat_row/<int:pk>', AddSeatRow.as_view(template_name='room/add_seat_row.html'), name='add_seat_row')
]