from django.urls import path

# In the same folder, therefore using . (titik)
from . import views

urlpatterns = [
    path('', views.index, name='index')
]