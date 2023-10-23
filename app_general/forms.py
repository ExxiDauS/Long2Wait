from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile
# from django.urls import reverse_lazy
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit, Layout, Field

class RegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = "w-[500px] rounded-md placeholder-[#DFB17E] bg-[#EADBC8] py-3 px-6 text-base font-['Prompt'] text-[#0F2C59] outline-none focus:border-[#6A64F1] focus:shadow-md"
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['class'] = "w-[500px] rounded-md placeholder-[#DFB17E] bg-[#EADBC8] py-3 px-6 text-base font-['Prompt'] text-[#0F2C59] outline-none focus:border-[#6A64F1] focus:shadow-md"
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = "w-[500px] rounded-md placeholder-[#DFB17E] bg-[#EADBC8] py-3 px-6 text-base font-['Prompt'] text-[#0F2C59] outline-none focus:border-[#6A64F1] focus:shadow-md"
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

    email = forms.EmailField(max_length=100, required=True, widget=forms.EmailInput(attrs={
        'class': 'w-[500px] rounded-md placeholder-[#DFB17E] bg-[#EADBC8] py-3 px-6 text-base font-["Prompt"] text-[#0F2C59] outline-none focus:border-[#6A64F1] focus:shadow-md',
        'type': 'email',
        'placeholder': 'Email',
        }))
    displayname = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'w-[500px] rounded-md placeholder-[#DFB17E] bg-[#EADBC8] py-3 px-6 text-base font-["Prompt"] text-[#0F2C59] outline-none focus:border-[#6A64F1] focus:shadow-md',
        'type': 'text',
        'placeholder': 'Display Name',
        }))
    class Meta(UserCreationForm.Meta):
        models = User
        fields = ('username', 'displayname', 'email', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name")

class ExtendedProfileForm(forms.ModelForm):
    prefix = "extended"

    class Meta:
        model = Profile
        fields = ('nickname',)
        labels = {
            "nickname": "ชื่อเล่น",
        }