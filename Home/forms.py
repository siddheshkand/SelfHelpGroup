from django import forms

from Collection.models import Member


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Member
        # fields = '__all__'
        exclude = ['is_active', 'user']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', })
