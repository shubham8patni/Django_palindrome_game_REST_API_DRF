from django import views
from django.urls import path
from .views import create, getBoard, updateBoard, updateBoardString, listview

urlpatterns = [
    path('', create, name = 'create-game'),
    path('<int:id>/', getBoard, name = 'get-board'),
    path('<int:id>/update/', updateBoard, name = 'update-board'),
    path('<int:id>/update1/', updateBoardString, name = 'update-board-string'),
    path('all/', listview, name = 'list-view'),
]