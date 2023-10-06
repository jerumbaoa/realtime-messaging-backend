from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    """ Manager which contains methods used by the User model
    """
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        instance = self.model(email=email, username=email)
        instance.set_password(password)
        instance.save()

        return instance

    def create_superuser(self, email, password, **kwargs):

        instance = self.create_user(email, password, **kwargs)
        instance.is_admin = True
        instance.is_staff = True
        instance.is_superuser = True
        instance.save()

        return instance