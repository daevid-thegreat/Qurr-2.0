from django.db import models

# Create your models here.


class Link(models.Model):
    url = models.URLField()
    shortcode = models.CharField(max_length=15, unique=True, blank=True)

    def __str__(self):
        return self.url


