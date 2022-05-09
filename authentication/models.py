from django.db import models

class Authentication(models.Model):
    username = models.CharField(max_length=200)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    pass1 = models.CharField(max_length=200)
    pass2 = models.CharField(max_length=200)




