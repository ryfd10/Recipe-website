from django.db import models

# Create your models here.

class Author(models.Model):
    name=models.CharField(max_length=20)
    Email=models.EmailField(max_length=50)

class Recipe(models.Model) :
    name=models.CharField(max_length=30)
    Time_of_preparing=models.IntegerField()
    slug = models.CharField(max_length=300)
    level=models.IntegerField()
    ingredients_list=models.TextField()
    instructions=models.TextField()
    image = models.ImageField(upload_to='images/', default=None)
    author=models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.name