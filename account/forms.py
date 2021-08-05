from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username','emial','password1','password2')
        model = get_user_model
        labels = {'username':'Display Name' ,'email':'Emial Address'}