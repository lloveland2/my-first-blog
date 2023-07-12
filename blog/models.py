'''This module contains the definitions of any model subclasses used within the project.'''
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    '''Post is a child of the import class, \"Model\".
    It defines the data fields used to create and populate our database.py'''
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        '''The publish function assigns the current time to the published_date variable.
        It then calls the save function inherited from the parent \"Model\" class.'''
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        # Function docstring goes here.
        # pylint: disable=invalid-str-returned

        return self.title
    