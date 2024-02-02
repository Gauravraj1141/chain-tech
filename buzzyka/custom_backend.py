# custom_backend.py

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        print(UserModel,'>>>it is usermodels')

        try:
            print(username,'>>>It is username')
            print(password,'>>>It is username')
            user = UserModel.objects.get(username=username)
            print(user,'>>>user model ')
            
        except UserModel.DoesNotExist:
            return None

        print(user.check_password(password),">>>checking password")
        if user.check_password(password):
            return user

        return None
