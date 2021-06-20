from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class Person(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    email_confirmed = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def update_user_person(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)
    instance.person.save()














