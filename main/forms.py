from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Importing Captcha
from captcha.fields import ReCaptchaField


# create a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # Adding reCaptcha field    
    captcha = ReCaptchaField()