from PIL import Image
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CompanySize(models.Model):
    people = models.CharField(max_length=30)

    def __str__(self):
        return self.people

class LanguageStack(models.Model):
    title = models.CharField(max_length=200, blank=False)
    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title


class Post(models.Model):
    name = models.CharField(max_length=200)
    estd = models.CharField(max_length=200)
    size = models.ForeignKey(CompanySize, on_delete=models.SET_NULL, blank=False, null=True)
    address = models.CharField(max_length=400)
    websitelink = models.URLField(max_length=200)
    tech = models.ManyToManyField(LanguageStack)
    logo = models.ImageField(
        default='default.png', upload_to='uploads/%Y/%m/%d/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'Added {self.name} Profile'

    class Meta:
        ordering = ['name']

    def save(self):
        super().save()
        img = Image.open(self.logo.path)
        (width,height) = img.size
        if height > 200:
            height = 200
        if width > 300:
            width = 300
        size = (width,height)
        img = img.resize(size, Image.ANTIALIAS)
        img.save(self.logo.path)

    
