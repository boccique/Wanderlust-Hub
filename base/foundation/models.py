from django.db import models


class RegisteredUser(models.Model):
    username = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    passwd = models.CharField(max_length=50, blank=True, null=True)
    fname = models.CharField(max_length=100, blank=True, null=True)
    lname = models.CharField(max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    bio = models.TextField(max_length=10000, blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.username
