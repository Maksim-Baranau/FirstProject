from typing import Any

from django.db import models


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
