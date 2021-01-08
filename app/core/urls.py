from django.urls import path
from .views import upload_members_view, upload_inventory_view

app_name='core'

urlpatterns = [
    path('members', upload_members_view, name='upload-view'),
    path('inventory', upload_inventory_view, name='inventory-view'),
    path('book', ,name=''),
    path('cancel', ,name='')
]