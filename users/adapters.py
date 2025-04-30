from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.forms import ValidationError

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)
        user.email = data.get('email')
        # Prevent setting username (Allauth tries to do this)
        if hasattr(user, 'username'):
            delattr(user, 'username')
        return user
