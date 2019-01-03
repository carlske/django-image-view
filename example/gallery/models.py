from django.db import models

# Create your models here.


class Gallery(models.Model):
    """ Gallety Model """
    name = models.CharField(max_length=80)
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name