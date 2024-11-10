from django import forms

from profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['bio']
        labels = {
            'nickname': 'Nickname:',
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'chef': 'Chef:',
        }


class CreateProfileForm(ProfileBaseForm):
    pass


class EditProfileForm(ProfileBaseForm):
    pass