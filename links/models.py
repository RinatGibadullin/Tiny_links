from django.db import models


class Link(models.Model):
    orig_link = models.CharField(max_length=200)
    tiny_link = models.CharField(max_length=50)

    def __str__(self):
        return self.tiny_link
