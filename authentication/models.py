from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomBaseUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, username, password, email=None, **kwargs):
        """Create and return a `User` with an email, username and password."""
        if not username:
            raise TypeError("Users must have a username.")

        if not password:
            raise TypeError("User must have a  papssword.")

        user = self.model(
            username=username, password=password, email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, username, password, email=None, **kwargs):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if not password:
            raise TypeError("Superusers must have a password.")

        if not username:
            raise TypeError("Superusers must have a unique username.")

        user = self.create_user(
            username=username, password=password, email=email, **kwargs
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)

        return user
    
        def has_module_perms(self, *args): # or add
            return True


class User(AbstractUser, PermissionsMixin):
    """
    ...
    """
    username = models.CharField(
        _("Username"), db_index=True, unique=True, max_length=255
    )
    first_name = models.CharField(
        _("First Name"), max_length=255, null=True, blank=True,
    )
    last_name = models.CharField(
        _("Last Name"), max_length=255, null=True, blank=True
    )
    cell = models.CharField(
        _("Phone number"), max_length=15, null=True, blank=True
    )
    email = models.EmailField(
        _("Email"), 
        # unique=True,
        null=True,
        blank=True,
        error_messages={
            'unique': _("A user with that email already exists."),
        }
    )
    created_at = models.DateTimeField(
        _("Created At"), 
        auto_now_add=True,
        null=True,
        blank=False,
    )
    updated_at = models.DateTimeField(
        _("Updated At"),
        auto_now=True,
        null=True,
        blank=False,
    )
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    date = models.DateTimeField(auto_now_add=True)
    
    
    objects = CustomBaseUserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta(AbstractUser.Meta):
        pass

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.ForeignKey('User', null=True, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user}-profile-{self.pk}'
