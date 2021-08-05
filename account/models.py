from django.contrib.auth.models import PermissionsMixin, User


class User(User, PermissionsMixin):
    def __str__(self):
        return '@{}'.format(self.username)
