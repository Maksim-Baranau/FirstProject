from typing import Any

from django.db import models
from django.contrib.auth.models import User


class ycity(models.Model):
    name: Any = models.CharField(max_length=50)
    about: Any = models.TextField(blank=True, null=True)
    age: Any = models.IntegerField(blank=True, null=True)
    img: Any = models.ImageField(upload_to='images/')

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"pk={self.pk}, "
            f"name={self.name!r}, "
            f"age={self.age},"
            f"surname={self.about},"
            f"img={self.img},"
            f")"
        )

    #def is_valid(self):
        #pass

class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio=models.TextField(null=True, blank=True)
    facebook = models.CharField(max_length=50, null=True, blank=True)
    twitter = models.CharField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)
def __str__(self):
    return str(self.user)