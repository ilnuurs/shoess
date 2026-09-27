from django.urls import path
from .views import SneakerListView

urlpatterns = [

    path('sneakers/', SneakerListView.as_view(), name='sneakers-list'), 
]