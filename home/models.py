from django.db import models

class Contact(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 250)
    phone  = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return "Message from" + self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    message = models.TextField()
    picture = models.ImageField(upload_to='media')
    

