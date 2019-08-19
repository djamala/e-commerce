from django import forms
from django.core.validators import ValidationError, validate_email
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    username = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password =  forms.CharField(required=True, max_length=30, widget=forms.PasswordInput(attrs={'placeholder':'Mot de passe'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'placeholder':'Adress Email'}))
    class Meta:
        model = User
        fields = ['username','email','password']
       
    def clean_username(self):
        user = self.cleaned_data['username']
        try:
            match = User.objects.get(username=user)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError("Le nom d'utilisateur existe déjà")

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            mt = validate_email(email)
        except:
            return forms.ValidationError("Adresse email incorrect !")
        return email


class LoginForm(forms.ModelForm):
    username = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(required=True, max_length=30, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    remember_user = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not username and not password:
            raise forms.ValidationError("Veillez renseigner un nom utilisateur et un  mot de passe")

        try:
            user = User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist:
            raise forms.ValidationError("Nom utilisateur invalide, veillez réessayr plus tard")

        if not user.check_password(self.cleaned_data['password']):
            raise forms.ValidationError("Mot de passe invalide, veillez réessayr plus tard")

        return self.cleaned_data