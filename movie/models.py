from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    preview = models.ImageField(upload_to='previews')
    title = models.CharField(max_length=100)
    description = models.TextField()
    rate = models.FloatField(default=0)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='director', null=True)
    genres = models.ManyToManyField(Genre, blank=True)

    @property
    def filtered_reviews(self):
        return self.reviews.filter(stars__gte=3)  # if you use related_name  "stars__gte=3 Включительно 3"
        # return Review.objects.filter(movie=self, star__gt=3)   "No related_name"  "stars__gt=3 Не включительно 3"

    @property
    def director_name(self):
        return self.director.name if self.director else ""

    def __str__(self):
        return self.title


STARS_CHOICES = (
    (1, '* '),
    (2, 2 * '* '),
    (3, 3 * '* '),
    (4, 4 * '* '),
    (5, 5 * '* ')
)


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(default=5, choices=STARS_CHOICES)

    def __str__(self):
        return self.text
