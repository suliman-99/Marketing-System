from django import forms
from .models import *

class AddMarketerForm(forms.ModelForm):

    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    email = forms.EmailField(required=False)

    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Marketer
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 
                  'withdrawal_threshold', 'commission', 'gender', 'reference_link')


class ChangeMarketerForm(forms.ModelForm):

    class Meta:
        model = Marketer
        fields = ('username', 'first_name', 'last_name', 
                  'withdrawal_threshold', 'commission', 'gender', 'reference_link')

    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    email = forms.EmailField(required=False)
    is_active = forms.BooleanField()

    def get_initial_for_field(self, field, field_name):
        marketer = self.instance
        if field_name == 'username':
            return marketer.user.username
        elif field_name == 'first_name':
            return marketer.user.first_name
        elif field_name == 'last_name':
            return marketer.user.last_name
        elif field_name == 'email':
            return marketer.user.email
        elif field_name == 'is_active':
            return marketer.user.is_active
        
        return super().get_initial_for_field(field, field_name)
