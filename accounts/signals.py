from allauth.socialaccount.models import SocialAccount
from .models import Account
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile
from django.contrib.auth.models import User
from allauth.account.signals import user_logged_in
from allauth.account.signals import user_signed_up
"""@receiver(post_save, sender=Account,)
def create_user_profile(sender, instance, created, **kwargs):
   
    if created:
       
        
        
            
        
        user= Account.objects.all()
        user.is_active = True
        
        UserProfile.objects.create(user=instance)"""


@receiver(user_signed_up)
def retrieve_social_data(request, user, **kwargs):
    """Signal, that gets extra data from sociallogin and put it to profile."""
    # get the profile where i want to store the extra_data
    profile = UserProfile(user=user)
    profile.save()
    user.is_active = True
    user.save()
    # in this signal I can retrieve the obj from SocialAccount
    data = SocialAccount.objects.filter(user=user, provider='google')
    # check if the user has signed up via social media
    print(data)
        
        




