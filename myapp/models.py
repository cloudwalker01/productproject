from django.db import models

# Create your models here.

class Product(models.Model):
    title=models.CharField(max_length=50)
    price=models.PositiveIntegerField()
    description=models.CharField()

    def __str__(self):
        return self.title

    

# class Author(models.Model):
#     fname=models.CharField(max_length=50)
#     lname=models.CharField(max_length=50)
#     email=models.EmailField()

#     def __str__(self):
#         return self.fname

# class Publisher(models.Model):
#     name=models.CharField(max_length=50)
#     street=models.CharField(max_length=50)
#     city=models.CharField(max_length=50)
#     state=models.CharField(max_length=50)
#     country=models.CharField(max_length=50)
#     website=models.URLField(max_length=50)
    
#     def __str__(self):
#         return self.name

# class Book(models.Model):
#     title=models.CharField(max_length=50)
#     date=models.DateField(max_length=50)
#     author=models.ManyToManyField(Author)
#     publisher=models.ForeignKey(Publisher, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title

