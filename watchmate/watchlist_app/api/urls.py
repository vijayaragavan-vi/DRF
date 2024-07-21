from django.urls import path
from watchlist_app.api.views import MovieListAV,MoveiDetailAV


urlpatterns = [
    path('list/',MovieListAV.as_view(),name = 'movie-list'),
    path('<int:pk>',MoveiDetailAV.as_view(), name='movie-details'),
]
