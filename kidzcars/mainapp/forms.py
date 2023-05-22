from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ClearableFileInput
from .models import Car, Brand

class NewUserForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class NewCarForm(forms.ModelForm):
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), widget=forms.Select(attrs={'placeholder': 'Brand'}))
    model = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Model'}))
    generation = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Generation'}))
    year = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Year'}))

    class Meta:
        model = Car
        fields = ['brand', 'model', 'generation', 'year']

class NewBrandForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Brand name'}))
    logo = forms.ImageField(required=True, widget=ClearableFileInput(attrs={'placeholder': 'Logo'}))
    year = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Year of creation'}))

    class Meta:
        model = Brand
        fields = ['name', 'logo', 'year']