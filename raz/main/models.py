from django.db import models
from django.urls import reverse


class TeamMembers(models.Model):
    FullName = models.CharField(max_length=50)
    IdentityNumber = models.IntegerField()
    Image = models.ImageField(upload_to='static/teammembers/')
    Bio = models.TextField()

    def get_absolute_url(self):
        return reverse('main:dteammember', kwargs={'pk': self.pk})

    def __str__(self):
        return self.FullName
