from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import shortuuid
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.core.files.storage import default_storage
from django.template.defaultfilters import striptags


class Category(models.Model):
    name = models.CharField(max_length=70)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name.capitalize()


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField(null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="likedposts", through="LikedPost")
    header_image = models.ImageField(
        default="default_header_image.png", null=True, blank=True, upload_to="post_pics"
    )
    cropped_image_1000x420 = ImageSpecField(
        source="header_image",
        processors=[ResizeToFill(1000, 420)],
        format="JPEG",
        options={"quality": 90, "auto_cleanup": True},
    )
    cropped_image_420x420 = ImageSpecField(
        source="header_image",
        processors=[ResizeToFill(580, 580)],
        format="JPEG",
        options={"quality": 90, "auto_cleanup": True},
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

    def get_cleaned_content(self):
        cleaned_content = striptags(self.content)
        return cleaned_content

    def reading_time(self):
        words_per_minute = 200
        words = self.content.split()
        total_words = len(words)
        reading_time = total_words // words_per_minute
        if reading_time == 0:
            return 1
        return round(reading_time)
    
class LikedPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} : {self.post.title}"
