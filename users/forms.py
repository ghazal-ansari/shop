from django import forms
from .models import User
class LoginForm(forms.Form):
    username = forms.CharField(label='نام کاربری',max_length=20)
    password = forms.CharField(label='پسورد',max_length=20,widget=forms.PasswordInput)
class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','first_name','last_name','national_code','role']


class OtpForm(forms.Form):
    phone = forms.CharField(label="شماره تماس",max_length=11)

class VerifyCode(forms.Form):
    code = forms.CharField(label="کد تایید",max_length=11)