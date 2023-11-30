from django.urls import path
from lesson14app.views import *

urlpatterns = [
    path('', index_page_view, name='index'),
    path('form/', form_page_view, name='form'),
    path('update/<int:pk>', update_page_view, name='update'),
    path('delete-page/<int:pk>', delete_page_view, name='delete'),
]






