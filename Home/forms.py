from django import forms

from Collection.models import Member


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Member
        # fields = '__all__'
        exclude = ['is_active']
