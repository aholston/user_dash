from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REG = re.compile('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$')

# Create your models here.
class UserManager(models.Manager):
    def validate(self, data):
        errors = {}
        if len(data['first_name']) < 2:
            errors['first_name'] = 'First name should be atleast 3 characters'
        if len(data['last_name']) < 2:
            errors['last_name'] = 'Last name should be atleast five characters'
        if not EMAIL_REG.match(data['email']):
            errors['email'] = 'Please enter a valid email address'
        if User.objects.get(email=data['email']):
            errors['email_use'] = 'Email already in use!'
        if data['password'] != data['pw_conf']:
            errors['password'] = 'Passwords do not match'
        if len(data['password']) < 8:
            errors['pw_length'] = 'Password should be atleast 8 characters'
        return errors



class Message(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    messages = models.ForeignKey(Message, related_name='users_message')
    comments = models.ForeignKey(Comment, related_name='users_comment')

    objects = UserManager()

class Admin(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ForeignKey(User, related_name='admins')
    messages = models.ForeignKey(Message, related_name='admins_message')
    comments = models.ForeignKey(Comment, related_name='admins_comment')




    objects = UserManager()
