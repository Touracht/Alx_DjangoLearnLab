from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)