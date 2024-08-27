from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=50, verbose_name="Author")
    title = models.CharField(max_length=200, verbose_name="Title")
    text = models.TextField(verbose_name="Post text")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Created at", editable=False)
    image = models.ImageField(upload_to='posts/', null=True, verbose_name='Image')

    class Meta:
        verbose_name = "Post"           # table name
        verbose_name_plural = "Posts"   # table name plural

    def __str__(self):
        return self.title

