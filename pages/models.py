from turtle import title
from django.db import models

class PagesModel(models.Model):
    title=models.CharField(max_length=150)
    body=models.TextField()
    author=models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)