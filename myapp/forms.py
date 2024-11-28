from django import forms
from .models import NewsletterSubscription

class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']

        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'required js-validity-check d-block width-full height-md-full mb-2 mb-md-0 f4-mktg newsletter-field rounded-2',
                'placeholder': 'Your email address',
                'style': 'border: none; outline: none;background-color: transparent;'
            })
        }

    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'required js-validity-check d-block width-full height-md-full mb-2 mb-md-0 f4-mktg newsletter-field rounded-2',
            'placeholder': 'Your email address',
            'style': 'border: none; outline: none;background-color: transparent;'
        })
    )
