from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class User(AbstractBaseUser, PermissionsMixin):
    nombre_usuario = models.CharField(_('username'), max_length=150, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    cumpleaños = models.DateField(_('birthday'), null=True, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'nombre_usuario'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.nombre_usuario

