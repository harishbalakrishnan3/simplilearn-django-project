from django import forms
from patientManagement.models import UserInfo


class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ("first_name", "last_name", "dob")


class CheckForm(forms.Form):
    uniqueID = forms.IntegerField()
