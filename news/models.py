from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Novosti (models.Model):
    title = models.CharField (max_length=70)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body = models.TextField()
    date = models.DateTimeField()
    img = models.ImageField (blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Пользователь",null=False)
    post = models.ForeignKey(Novosti,on_delete=models.CASCADE,verbose_name="Пост",null=False)
    body = models.TextField()
    created = models.DateTimeField("Дата добавления",auto_now_add=True, null=False, blank=True)


    class Meta:
        ordering = ('created',)

    def __str__(self):
        return "{}".format(self.user)