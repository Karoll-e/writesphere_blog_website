from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import shortuuid
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=70)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name.capitalize()

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    header_image = models.ImageField(null=True, blank=True, upload_to="post_pics")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    def reading_time(self):
        words_per_minute = 200  
        words = self.content.split()
        total_words = len(words)
        reading_time = total_words // words_per_minute
        if reading_time == 0:
            return 1
        return round(reading_time)



