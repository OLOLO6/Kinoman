from django.shortcuts import render

# Create your views here.
from kinoman.models import *
from kinoman.serializers import *
from rest_framework import generics
from rest_framework.response import *
from django.http import Http404
from rest_framework.views import APIView
from django.contrib.auth.models import User
from kinoman.serializers import UserSerializer
from rest_framework import filters
import django_filters
import datetime
from django.core.exceptions import ValidationError
from .permissions import *



class MovieView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = Movie_Serializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def post(self, request):
        data=(request.data['movies_premiere'])
        if data > datetime.date.today():
            raise ValidationError(_('Invalid date'))
        return data


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = Movie_Serializer


class CinemaView(generics.ListCreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = Cinema_Serializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializers):
        serializers.save(owner=self.request.user)


class CinemaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = Cinema_Serializer


class ContentView(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = Content_Serializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializers):
        serializers.save(owner=self.request.user)


class ContentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = Content_Serializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class CinemasInformationView(generics.ListCreateAPIView):
    queryset = CinemasInformation.objects.all()
    serializer_class = CinemasInformation_Serializer



class MoviesCommentView(generics.ListCreateAPIView):
    queryset = MoviesComment.objects.all()
    serializer_class = MoviesComment_Serializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializers):
        serializers.save(owner=self.request.user)


class CinemasSessionsPriceView(generics.ListCreateAPIView):
    queryset = CinemasSessionsPrice.objects.all()
    serializer_class = CinemasSessionsPrice_Serializer


class CinemasSessionView(generics.ListCreateAPIView):
    queryset = CinemasSession.objects.all()
    serializer_class = CinemasSession_Serializer


class CinemasCommentView(generics.ListCreateAPIView):
    queryset = CinemasComment.objects.all()
    serializer_class = CinemasComment_Serializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializers):
        serializers.save(owner=self.request.user)


class IkinomanView(generics.ListCreateAPIView):
    queryset = Ikinoman.objects.all()
    serializer_class = Ikinoman_Serializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializers):
        serializers.save(owner=self.request.user)


class IkinomanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ikinoman.objects.all()
    serializer_class = Ikinoman_Serializer

class GenreView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = Genre_Serializer


class MovieFindView(generics.ListAPIView):
    serializer_class = Movie_Serializer
    queryset = Movie.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['movies_name', 'movies_year', 'movies_country', 'movies_genre', 'movies_director',
                        'movies_actor',
                        'movies_duration', 'movies_age_limit', 'movies_premiere', 'movies_story', 'movies_trailer',
                        'movies_other', 'movies_comments']


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

