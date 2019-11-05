from django.db import models

class Content(models.Model):
    CATEGORIES = (('1', 'Новости'),
                  ('2', 'Статьи'),
                  ('3', 'Рецензии'),
                  ('4', 'Интервью'),
                  ('5', 'События')
                  )
    category = models.CharField('Категория', max_length=20, default='', choices=CATEGORIES)
    title = models.CharField('Название', max_length=100, default='')
    text = models.TextField('Текст публикации', help_text='Введите текст')
    author = models.CharField('Автор', max_length=50, default='', blank=True, null=True)
    pub_date = models.DateTimeField('Дата публикации', default='')
    reference = models.CharField('Ссылки', max_length=200, default='', blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='Owner', on_delete=models.CASCADE, default='',
                              verbose_name='Создатель')

    class Meta:
        verbose_name = 'Материалы'
        verbose_name_plural = 'Материалы'

    def __str__(self):
        return self.title
class Genre(models.Model):
    genres_name=models.CharField('Наименование жанра', max_length=100, default='')
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
    def __str__(self):
        return self.genres_name

class Movie(models.Model):
    LIMITS = (('1', '6+'),
              ('2', '12+'),
              ('3', '14+'),
              ('4', '16+'),
              ('5', '18+')
              )

    movies_name = models.CharField('Название', max_length=100, unique=True, default='')
    movies_year = models.IntegerField('Год выпуска')
    movies_country = models.CharField('Производство', max_length=50, default='')
    movies_genre = models.ManyToManyField(Genre, max_length=50, default='', verbose_name='Жанр')
    movies_director = models.CharField('Режиссёр', max_length=50, default='')
    movies_actor = models.CharField('Актёры', max_length=250, default='')
    movies_duration = models.TimeField('Продолжительность')
    movies_age_limit = models.CharField('Возрастное ограничение', max_length=20, default='', choices=LIMITS)
    movies_premiere = models.DateField('Премьера', max_length=50, default='')
    movies_story = models.TextField('Сюжет')
    movies_trailer = models.CharField('Трейлер', max_length=50, default='')
    movies_other = models.ManyToManyField(Content, verbose_name='Другое', blank=True)

    def __str__(self):
        return self.movies_name

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def validate(self):
        if self.movies_premiere > timezone.now:
            raise serializers.ValidationError("finish must occur after start")
        return data


class MoviesComment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, help_text='Выберите фильм',
                              verbose_name='Название фильма')
    name_of_publication = models.CharField('Заголовок', max_length=100, default='', help_text='Введите заголовок')
    text_of_publication = models.TextField('Текст публикации', help_text='Введите текст')
    date_of_publication = models.DateTimeField('Дата публикации')
    owner = models.ForeignKey('auth.User', related_name='Commen_owner', on_delete=models.CASCADE, verbose_name='Создатель')
    class Meta:
        verbose_name = 'Комментарий к фильму'
        verbose_name_plural = 'Комментарии к фильму'

    def __str__(self):
        return f'{self.name_of_publication} -- {self.date_of_publication}'



class CinemasInformation(models.Model):
    cinemas_address = models.CharField('Адрес', max_length=100, default='')
    cinemas_official_website = models.CharField('Оффициальный сайт', max_length=100, default='')
    cinemas_social_media = models.CharField('Социальные сети', max_length=100, default='')
    class Meta:
        verbose_name = 'Информация о кинотеатрах'
        verbose_name_plural = 'Информация о кинотеатре'

    def __str__(self):
        return f'Контакты {self.cinemas_social_media}'



class CinemasSessionsPrice(models.Model):
    child_ticket = models.IntegerField('Детский билет')
    adult_ticket = models.IntegerField('Взрослый билет')
    student_ticket = models.IntegerField('Студенческий билет')
    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'

    def __str__(self):
        return f'{self.child_ticket} Детский \n' \
               f'{self.adult_ticket} Взрослый \n' \
               f'{self.student_ticket} Студенческий'


class CinemasSession(models.Model):
    movies_name = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Название фильма')
    movies_date = models.DateField('Дата')
    movies_time = models.TimeField('Время')
    movies_hall = models.CharField('Зал', max_length=20, default='')
    movies_format = models.CharField('Формат', max_length=20, default='')
    movies_price = models.OneToOneField(CinemasSessionsPrice, on_delete=models.CASCADE, verbose_name='Цена')
    class Meta:
        verbose_name = 'Сеанс'
        verbose_name_plural = 'Сеансы'

    def __str__(self):
        return self.movies_name.movies_name

class Cinema(models.Model):
    cinemas_name = models.CharField('Название', max_length=20, default='')
    cinemas_information = models.OneToOneField(CinemasInformation, on_delete=models.CASCADE, verbose_name='О Кинотеатре')
    cinemas_actions = models.TextField('Описание', null=True, blank=True)
    cinemas_sessions = models.OneToOneField(CinemasSession, on_delete=models.CASCADE, verbose_name='Сеансы', blank=True)
    cinemas_hall = models.CharField('Вместительность', max_length=20, default='')
    owner = models.ForeignKey('auth.User', related_name='cinema_owner', on_delete=models.CASCADE, default='',
                              verbose_name='Создатель')
    class Meta:
        verbose_name = 'Кинотеатр'
        verbose_name_plural = 'Кинотеатры'

    def __str__(self):
        return self.cinemas_name

class CinemasComment(models.Model):
    cinema=models.ForeignKey(Cinema, on_delete=models.CASCADE, help_text='Выберите кинотеатр',
                              verbose_name='Название кинотеатра')
    name_of_publication = models.CharField('Заголовок', max_length=100, default='', help_text='Введите заголовок')
    text_of_publication = models.TextField('Текст публикации', help_text='Введите текст')
    date_of_publication = models.DateTimeField('Дата публикации')
    owner = models.ForeignKey('auth.User', related_name='owner_comment', on_delete=models.CASCADE,
                              verbose_name='Создатель')

    class Meta:
        verbose_name = 'Отзыв о кинотатре'
        verbose_name_plural = 'Отзывы о кинотеатре'

    def __str__(self):
        return f'{self.name_of_publication} -- {self.date_of_publication}'


class Ikinoman(models.Model):
    archive_name=models.CharField('Название подборки', max_length=100, default='', help_text='Введите название подборки')
    archive = models.ManyToManyField(Movie, verbose_name='Мои рекомендации', blank=True)
    owner = models.ForeignKey('auth.User', related_name='kino_owner', on_delete=models.CASCADE, default='',
                              verbose_name='Создатель')
    class Meta:
        verbose_name = 'Киномания'
        verbose_name_plural = 'Киномании'

    def __str__(self):
        return self.archive_name

