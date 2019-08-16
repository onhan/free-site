from allauth.account.signals import password_reset
from django.core.signals import request_finished
from django.dispatch import receiver


@receiver(request_finished)
def set_request_finished(sender, **kwargs):
    print("Request finished!")


@receiver(password_reset)
def set_password_reset(sender, **kwargs):
    print("Password has been reset!")
