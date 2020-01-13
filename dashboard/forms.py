from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required = True)
    email = forms.EmailField(required=True)
    city = forms.CharField(required = True)
    Football_Experience = forms.CharField(widget=forms.Textarea, required=True)
