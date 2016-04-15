from django import forms
from .models import *
from registration.forms import RegistrationForm

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        exclude = ('user',)

class UserProfileRegistrationForm(RegistrationForm):
    city = forms.CharField()

class UserProfileUpdateForm(RegistrationForm):
    city = forms.CharField()
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',)

class QuestionCreateWizardForm1(forms.Form):
    title = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))

class QuestionCreateWizardForm2(forms.Form):
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

class QuestionCreateWizardForm3(forms.Form):
    visibility = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=VISIBILITY_CHOICES)
    