from django.contrib import admin
from kinoman.models import *
# Register your models here.
admin.site.register(Cinema)
admin.site.register(CinemasInformation)
admin.site.register(MoviesComment)
admin.site.register(CinemasComment)
admin.site.register(Ikinoman)
admin.site.register(Genre)

class MovieAdmin(admin.ModelAdmin):
    list_display =('movies_name', 'movies_year', 'movies_country', 'movies_director', 'movies_actor')
    list_filter=('movies_name', 'movies_year', 'movies_country', 'movies_genre','movies_director', 'movies_actor')
admin.site.register(Movie, MovieAdmin)

class CinemasSessionAdmin(admin.ModelAdmin):
    list_display =('movies_name', 'movies_date', 'movies_time', 'movies_hall', 'movies_format')
admin.site.register(CinemasSession, CinemasSessionAdmin)

class CinemasSessionsPriceAdmin(admin.ModelAdmin):
    list_display =('child_ticket', 'adult_ticket', 'student_ticket')
admin.site.register(CinemasSessionsPrice, CinemasSessionsPriceAdmin)

class ContentAdmin(admin.ModelAdmin):
    list_display =('category', 'title', 'author', 'pub_date')
admin.site.register(Content, ContentAdmin)
