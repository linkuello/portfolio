from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Ваш email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Ваше сообщение'}))
