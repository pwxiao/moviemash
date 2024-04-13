from django.urls import path

from . import views
app_name = 'votes' 
urlpatterns = [
    path("", views.vote_for_movies, name="index"),
    path('vote/', view=views.vote, name='vote'), 
     path('rank/', view=views.rank, name='rank'),
]