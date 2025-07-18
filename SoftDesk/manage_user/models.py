from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    date_of_birth = models.DateField(verbose_name="Date de naissance")
    can_be_contacted = models.BooleanField(default=False, verbose_name="peut être contacté")
    can_data_be_shared = models.BooleanField(default=False, verbose_name="partage des données autorisé")

