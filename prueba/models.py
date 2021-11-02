from django.db import models
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    nameproduct = models.CharField(max_length=40)
    stockInicial = models.IntegerField()
    stockActual = models.IntegerField()
    precio = models.IntegerField()
    estado = models.BooleanField()
    createDate = models.DateField()
    updateDate = models.DateField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
