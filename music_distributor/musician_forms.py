__author__ = 'william'

from django import forms

Type_choices = (
    ('', 'Select your category'),
    ('musician', 'Musician'),
    ('user', 'User')
)

song_type = (
    ('', 'Select the song type'),
    ('hip-hop', "Hip-Hop"),
    ('rnb', "RNB"),
    ('country', "Country"),
    ('gospel', "Gospel")
)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=15, label="Username", widget=forms.TextInput(attrs={'class':'form-control', "placeholder":"Begin with your country code"}))
    password = forms.CharField(max_length=15, label="Password", widget=forms.PasswordInput(attrs={'class':'form-control', "placeholder":"Enter your Password"}))


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=15, label="Username", widget=forms.TextInput(attrs={'class':'form-control', "placeholder":"Enter your username"}))
    email = forms.EmailField(max_length=75, label="Email",   widget=forms.TextInput(attrs={'class':'form-control', "placeholder":"Enter your Email"}))
    contact = forms.CharField(max_length=15, label="Contact", widget=forms.TextInput(attrs={'class':'form-control', "placeholder":"Begin with your country code"}))
    password = forms.CharField(max_length=15, label="Password", widget=forms.PasswordInput(attrs={'class':'form-control', "placeholder":"Enter the password"}))
    password2 = forms.CharField(max_length=15, label="Password(Again)", widget=forms.PasswordInput(attrs={'class':'form-control', "placeholder":"Enter the password Again"}))
    user_type = forms.ChoiceField(choices=Type_choices, label='Category')


class VerifyForm(forms.Form):
    code = forms.CharField(max_length=10, label="Verification Code", widget=forms.TextInput(attrs={'class':'form-control', "placeholder":"Enter the verification code"}))


class SongUploadForm(forms.Form):
    title = forms.CharField(max_length=30, label="Title", widget=forms.TextInput(attrs={'class':'form-control'}) )
    description = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}), label="Song Description")
    genre = forms.ChoiceField(choices=song_type, label="Genre")
    song = forms.FileField(label="Song")


class AlbumForm(forms.Form):
    name = forms.CharField(max_length=20, label="Album Title", widget=forms.TextInput(attrs={'class':'form-control', "placeholder":"The Album Title" }) )
    description = forms.CharField(max_length=300, label="Description", widget=forms.TextInput(attrs={'class':'form-control', "placeholder":"description"}) )
    language = forms.CharField(max_length=20, label="Language", widget=forms.TextInput(attrs={'class':'form-control', "placeholder":"language"}))
    cover_pic = forms.ImageField(label="Cover Picture")


class EditAccountForm(forms.Form):
    brief_desc = forms.CharField(max_length=300, label="Brief description", widget=forms.TextInput(attrs={'class':'form-control', "placeholder":"A brief description about you" }) )
    image = forms.ImageField()


class EditPasswordForm(forms.Form):
    old_password = forms.CharField(max_length=15, label="Old Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=15, label="New Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(max_length=15, label="New Password(Again)", widget=forms.PasswordInput(attrs={'class':'form-control'}))

