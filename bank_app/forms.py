from django import forms
from . models import Customer
from multiselectfield.forms.fields import MultiSelectFormField
class MovieForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        # exclude = ['user']
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    materials_provided = MultiSelectFormField(choices=Customer.MATERIALS_PROVIDED_CHOICES, required=False)