from django.db import models

# Create your models here.

def home(request):
    return HttpResponse('Hello I am working')