from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_("name"), max_length=100,
                            blank=True,
                            null=True)
    email = models.EmailField(_("Email Address"), max_length=254, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    s_email = models.EmailField(blank=True, null=True, unique=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(max_length=255, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "password"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return f"{self.name} "


SUBSCRIPTION = (
    ('F', 'FREE'),
    ('D', 'DAY'),
    ('M', 'MONTH'),
)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_premium = models.BooleanField(default=False)
    premium_expiry_date = models.DateField(null=True, blank=True)
    subscription_type = models.CharField(max_length=100,choices=SUBSCRIPTION,default='FREE')
    q_attempt= models.BigIntegerField(null=True, blank=True,default=0)
    addiotional_info= models.JSONField(encoder=None,blank=True, null=True)
    image=models.ImageField(upload_to='uploads/',blank=True, null=True)

