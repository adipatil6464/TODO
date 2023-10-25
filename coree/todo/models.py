from django.db import models

class Tasks(models.Model):
    content = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.content 

class InProgress(models.Model):
    content = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.content

class Complete(models.Model):
    content = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.content


# Create your models here.
