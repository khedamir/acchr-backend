from django.contrib.auth.models import AbstractUser
from django.db import models

from core.utils.user_manager import UserManager
from django.utils.translation import gettext_lazy as _


class Image(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('Имя'))
    url = models.FileField(upload_to='images', verbose_name=_('Файл изображения'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{type(self).__name__}: {self.name}"

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class User(AbstractUser):
    full_name = models.CharField(max_length=254, blank=True, null=True, verbose_name=_('ФИО'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    email = None
    first_name = None
    last_name = None

    REQUIRED_FIELDS = []

    is_staff = models.BooleanField(
        _("staff status"),
        default=True,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    is_superuser = models.BooleanField(
        _("superuser status"),
        default=True,
        help_text=_(
            "Designates that this user has all permissions without "
            "explicitly assigning them."
        ),
    )

    objects = UserManager()

    class Meta:
        verbose_name = 'Администрация'

    def __str__(self):
        return f"{type(self).__name__}: {self.username} - {self.full_name} "


