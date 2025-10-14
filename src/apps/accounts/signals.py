from typing import Any

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .models import Profile, User


@receiver(post_save, sender=User, dispatch_uid="create_update_profile")
def create_or_update_user_profile(sender: Any, instance: Any, created: bool, **kwargs: Any) -> None:
    profile, _ = Profile.objects.get_or_create(user=instance)
    if created:
        Token.objects.create(user=instance)
    profile.save()
