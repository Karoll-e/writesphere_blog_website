from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageOps
#import cv2 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.png", upload_to="profile_pics")
    job_label = models.CharField(max_length=20)
    description = models.TextField(default="404 bio not found")

    def __str__(self):
        return f"{self.user.username} Profile"
    
    def save(self, *args, **kwargs):
        self.job_label = self.job_label.upper()
        super().save(*args,**kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            resized = ImageOps.fit(img, output_size, Image.ANTIALIAS)
            resized.save(self.image.path)



