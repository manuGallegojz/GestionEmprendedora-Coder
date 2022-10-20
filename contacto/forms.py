from django import forms

class ContactoFormulario(forms.Form):

    asunto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
