from django.db import models
from django.contrib.auth.models import User
# Create your models here.






class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    create_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_data','-update_data']






