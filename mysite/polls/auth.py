# from django.contrib.auth.models import User
from .models import User







class UsernamePasswordAuth(object):

    def authenticate(self, username=None, password=None):
        print("UsernamePasswordAuth.........")
        print("UsernamePasswordAuth.authenticate")
        try:
            print('userName:'+username)
            print(User.objects.all())
            user = User.objects.get(username=username)
            print(user is None)
            print("UsernamePasswordAuth.11111")
            if user.check_password(password):
                print("UsernamePasswordAuth.222222")
                return user
        except User.DoesNotExist:
            print("UsernamePasswordAuth.33333333")
            return None

    def get_user(self, user_id):
        print("UsernamePasswordAuth.get_user")
        try:
            user = User.objects.get(pk=user_id)
            return user
        except User.DoesNotExist:
            return None



   