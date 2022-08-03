from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField()
    remember_password = forms.BooleanField(initial=True)

class Conversor(forms.Form):
    origin_coin = forms.CharField()
    destiny_coin = forms.CharField()

from .models import Category
class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'     