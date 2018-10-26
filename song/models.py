from django.db import models
from slugger import AutoSlugField


class Category(models.Model):
    # ALL = "Основные"
    # CHILD = 'Детские'
    # CHRISTMAS = 'Рождественские'
    # EASTER = 'Пасхальные'
    #
    # song_genre = (
    #     (ALL, "Основные"),
    #     (CHILD, "Детские"),
    #     (CHRISTMAS, "Рождественские"),
    #     (EASTER, 'Пасхальные')
    # )
    name = models.CharField('Name', max_length=20, null=True)
    slug = AutoSlugField(populate_from='name', null=True)
    image = models.ImageField(null=True, blank=True)

    # choice = models.CharField(
    #     max_length=20,
    #     choices=song_genre,
    #     default=ALL,
    #     blank=True
    # )

    def __str__(self):
        return self.name


class Link(models.Model):
    song = models.ForeignKey('Song', on_delete=models.CASCADE)
    url = models.URLField(max_length=200, blank=True)


class Song(models.Model):
    title = models.CharField(max_length=200, blank=True)
    title_eng = models.CharField(max_length=200, blank=True)
    text = models.TextField(blank=True)
    text_eng = models.TextField(blank=True)
    accords = models.TextField(blank=True)
    presentation = models.FileField(upload_to='presentations/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


