from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField(max_length=60)
    description = models.TextField()
    authname=models.CharField(max_length=15)
    img=models.ImageField(upload_to='blog',blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)

    def _str_(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/')
    text = models.TextField()

    def __str__(self):
        return self.name