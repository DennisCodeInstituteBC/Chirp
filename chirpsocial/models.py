from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )
    name = models.CharField(max_length=200, unique=False)
    gender = models.CharField(max_length=200, unique=False)
    age = models.IntegerField(null=True, blank=True)  
    bio = models.TextField(blank=True)  
    chirp_cloudinary_img = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.user.username
        
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

class chirp(models.Model):
    user = models.ForeignKey(User,
                             related_name="chirps",
                             on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.body[:30]}..."
        )

# Create a Profile for each new user.
post_save.connect(create_profile, sender=User)


chirp_cloudinary_img = CloudinaryField('image', default='placeholder')