from django.db import models


class Rawdata(models.Model):
    data = models.TextField()


class Outputdata(models.Model):
    data = models.TextField()
