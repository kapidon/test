from django.urls import path
from .views import DetailView, ListView, UpdateView


urlpatterns = [
    path('detail/<int:pk>', DetailView.as_view(), name='detail'),
    path('update/<int:pk>', UpdateView.as_view(), name='update'),
    path('list/', ListView.as_view(), name='list')
]
