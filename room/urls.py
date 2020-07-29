from django.urls import path

from . import views

app_name = 'room'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('new/', views.create_room, name='new'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
