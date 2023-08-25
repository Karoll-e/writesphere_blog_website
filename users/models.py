from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from PIL import Image, ImageOps
#import cv2 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.png", upload_to="profile_pics")
    bio = models.TextField(default="404 bio not found")

    def __str__(self):
        return f"{self.user.username} Profile"
    
    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)
        try:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                resized = ImageOps.fit(img, output_size, Image.ANTIALIAS)
                resized.save(self.image.path)
        except (FileNotFoundError, ValidationError, OSError):
            pass




