from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo,name="todo"),
    path('delete_item/<int:pk>', views.deleteItem, name='deleteItem'),
    path('update_item<int:pk>', views.updateItem, name='updateItem'),
    path('showitem/', views.showitem, name='showitem'),
]