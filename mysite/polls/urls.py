from django.urls import path

# In the same folder, therefore using . (titik)
from . import views

app_name = 'polls'

urlpatterns = [
    # example: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results
    path('<int:question_id>/result/', views.results, name='results'),
    # ex: /polls/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]