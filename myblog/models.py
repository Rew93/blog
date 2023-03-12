from django.db import models


# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    image = models.ImageField(upload_to='post_image')