from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    variant = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='collection/album_covers/', blank=True, null=True)

    def __str__(self):
        return self.title
