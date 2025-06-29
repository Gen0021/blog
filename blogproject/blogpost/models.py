from django.db import models

# Create your models here.
class FirstModel(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()
    
CATEGORY = (('hobby','趣味'),('stydy','学習'),('other','その他  '))
    
class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    postdate = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length = 50,
        choices = CATEGORY
    )
    list_display = ("id","title")
    def __str__(self):
        return self.title
    
