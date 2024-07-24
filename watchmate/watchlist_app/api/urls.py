from django.urls import path
from watchlist_app.api.views import WatchListAV,WatchDetailAV,StreamiPlatformListAV,StreamPlatformDetailAV


urlpatterns = [
    path('list/',WatchListAV.as_view(),name = 'movie-list'),
    path('<int:pk>',WatchDetailAV.as_view(), name='movie-details'),
    path('stream/',StreamiPlatformListAV.as_view(), name ='stream'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream_platform_detail'),
]
