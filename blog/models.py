from django.db import models

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    contents = models.TextField()
    slug = models.CharField(max_length=130)
    author = models.CharField(max_length=25)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return 'Gazal/Poem ' + self.title + ' by ' + self.author   
