from django.urls import path
from kinoman import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from django.conf.urls import url

urlpatterns=[
path('movie',views.MovieView.as_view()),
path('movie/<int:pk>/', views.MovieDetail.as_view()),
path('genre',views.GenreView.as_view()),
path('cinema',views.CinemaView.as_view()),
path('cinema/<int:pk>/', views.CinemaDetail.as_view()),
path('content',views.ContentView.as_view()),
path('content/<int:pk>/', views.ContentDetail.as_view()),
path('moviescomment',views.MoviesCommentView.as_view()),
path('cinemasinformation',views.CinemasInformationView.as_view()),
path('cinemassession',views.CinemasSessionView.as_view()),
path('cinemascomment',views.CinemasCommentView.as_view()),
path('moviefind',views.MovieFindView.as_view()),
path('users/', views.UserList.as_view()),
path('users/<int:pk>/', views.UserDetail.as_view()),
path('ikinoman',views.IkinomanView.as_view()),
path('ikinoman/<int:pk>/', views.IkinomanDetail.as_view()),


]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns=format_suffix_patterns(urlpatterns)

