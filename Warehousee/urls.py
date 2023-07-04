from django.urls import path
from product_management.views import create_view, list_view, detail_view, update_view, delete_view

urlpatterns = [
    path('', list_view, name='list_view'),
    path('create/', create_view, name='create_view'),
    path('detail/<int:id>/', detail_view, name='detail_view'),
    path('update/<int:id>/', update_view, name='update_view'),
    path('delete/<int:id>/', delete_view, name='delete_view'),
]
