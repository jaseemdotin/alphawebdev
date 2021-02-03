from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
class alphasignupform(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = alpha_signup
        fields = UserCreationForm.Meta.fields+('firstname','lastname','city','pincode','email','phonenumber','astatus')

class alphacategoryform(ModelForm):
    class Meta:
        model=alpha_category
        fields='__all__'

class alphaproductsform(ModelForm):
    class Meta:
        model=alphaproducts1
        fields='__all__'


class lapspecform(ModelForm):
    class Meta:
        model=lapspec
        fields='__all__'

class ramspec(ModelForm):
    class Meta:
        model=ramspec
        fields='__all__'

class cameraspec(ModelForm):
    class Meta:
        model=cameraspec
        fields='__all__'

class productstatusform(ModelForm):
    class Meta:
        model=alphaproducts1
        fields=('spec_status',)


