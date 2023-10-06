from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


# Create your models here.
class User(AbstractBaseUser):
    """ Model which contains user's informations,
        inherited from django AbstractBaseUser
    """
    username = models.CharField(max_length=150, unique=True)
    display_name = models.CharField(max_length=150, null=True, blank=True)
    full_name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(_('email'))

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))

    objects = UserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        indexes = [
            models.Index(fields=['username']),
        ]

    def __str__(self):
        return f'{self.username}'
