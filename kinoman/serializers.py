from rest_framework import serializers
from kinoman.models import *
from django.contrib.auth.models import User


class Movie_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('movies_name', 'movies_year', 'movies_country', 'movies_genre', 'movies_director', 'movies_actor',
                  'movies_duration', 'movies_age_limit', 'movies_premiere', 'movies_story', 'movies_trailer',
                  'movies_other')


class MoviesComment_Serializer(serializers.ModelSerializer):
    class Meta:
        model = MoviesComment
        fields = ('movie', 'name_of_publication', 'text_of_publication', 'date_of_publication', 'owner')

class Genre_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('__all__')

class Cinema_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ('cinemas_name', 'cinemas_information', 'cinemas_actions', 'cinemas_sessions', 'cinemas_hall', 'owner')

class Content_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('category', 'title', 'text', 'author', 'pub_date', 'reference', 'owner')


class CinemasInformation_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CinemasInformation
        fields = ('cinemas_address', 'cinemas_official_website', 'cinemas_social_media')


class CinemasSession_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CinemasSession
        fields = ('movies_name', 'movies_date', 'movies_time', 'movies_hall', 'movies_format', 'movies_price')

class CinemasSessionsPrice_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CinemasSessionsPrice
        fields = ('child_ticket', 'adult_ticket', 'student_ticket')


class CinemasComment_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CinemasComment
        fields = ('cinema', 'name_of_publication', 'text_of_publication', 'date_of_publication', 'owner')


class Ikinoman_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ikinoman
        fields = ('archive_name', 'archive', 'owner')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined', 'password', 'is_superuser', 'is_staff', 'is_active')
