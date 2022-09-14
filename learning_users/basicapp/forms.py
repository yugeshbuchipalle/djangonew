from django import forms
from django.contrib.auth.models import User
from basicapp.models import UserprofileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields  = ('username','password','email')


class UserprofileInfoForm(forms.ModelForm):
    class Meta():
        model = UserprofileInfo
        fields = ('portifilo_site','profile_pic')
