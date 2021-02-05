from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100)
