from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=200)
    status=models.IntegerField(default=1)

    def __str__(self):
        return self.user_name


class Connective(models.Model):
    user_name = models.CharField(max_length=200)
    status=models.IntegerField(default=1)

    def __str__(self):
        return self.user_name
