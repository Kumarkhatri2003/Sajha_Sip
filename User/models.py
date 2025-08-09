from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    full_name = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField(blank=True)
    city = models.CharField(max_length=50, blank=True)

    AVAILABILITY_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
    ]
    availability = models.CharField(max_length=15, choices=AVAILABILITY_CHOICES, blank=True)

    # Skills
    skills_offered = models.ManyToManyField('Skill', related_name='offered_by', blank=True)
    skills_interested = models.ManyToManyField('Skill', related_name='interested_by', blank=True)

    # Override groups and user_permissions with unique related_name
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Unique related_name here
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='custom_user'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # Unique related_name here
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='custom_user'
    )

    def __str__(self):
        return self.username  # or self.full_name


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
