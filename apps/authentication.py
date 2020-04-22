from apps.models import Admin
from django.contrib.auth.models import User


class AdminBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            admin = Admin.objects.get(username=username)
            if Admin.objects.get(password=password):
                return admin
            return None
        except Admin.DoesNotExist:
            return None

    def get_admin(self, username):
        try:
            return Admin.objects.get(pk=username)
        except Admin.DoesNotExist:
            return None
