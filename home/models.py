from django.db import models

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=300)
    lname = models.CharField(max_length=300)
    email = models.EmailField()
    query = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'msg from ' + self.fname
    
