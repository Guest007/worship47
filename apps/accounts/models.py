import uuid

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL,
#                                 on_delete=models.CASCADE,
#                                 related_name='profile',
#                                 )
#     deleted = models.DateTimeField(blank=True, null=True)
#     # data = JSONField(blank=True, default=dict)
#
#     def __str__(self):
#         return f"{self.user.pk}-{self.user.email}"
