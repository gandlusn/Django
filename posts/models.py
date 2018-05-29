from django.db import models
import django.db
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=200)
    url = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User,on_delete=django.db.models.deletion.CASCADE)
    votes_total = models.IntegerField(default=1)
    content = models.TextField()