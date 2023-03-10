from dataclasses import dataclass
from typing import Type
from typing import final

from django.db import models

from app_maksim_baranau.bob.interfaces import UseCase
from app_maksim_baranau.models import ycity
from app_maksim_baranau.scheme.ycity import ycitySchema


@final
@dataclass(slots=True)
class GetAllycityUseCase(UseCase):
    model: Type[models.Model] = ycity

    def __call__(self) -> list:
        return list(self.model.objects.all())


@final
@dataclass(slots=True)
class SaveycityUseCase(UseCase):
    ycity: ycitySchema
    model: Type[models.Model] = ycity

    def __call__(self) -> None:
        db_obj = self.model(**self.ycity.dict())
        db_obj.save()