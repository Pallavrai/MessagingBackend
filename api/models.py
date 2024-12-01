from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    admin = models.ForeignKey('auth.User', related_name='admin_groups', on_delete=models.CASCADE)
    members = models.ManyToManyField('auth.User', related_name='group_members')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Message(models.Model):
    sender = models.ForeignKey('auth.User', related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey('auth.User', related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    groups=models.ManyToManyField(Group,related_name='group_messages',blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.sender} to {self.receiver} at {self.timestamp}'
    
    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['sender']),
            models.Index(fields=['receiver']),
            models.Index(fields=['timestamp']),
        ]
    @property
    def short_body(self):
        return self.body[:50]

    @property
    def sender_username(self):
        return self.sender.username

    @property
    def receiver_username(self):
        return self.receiver.username
    def __str__(self):
        return f'{self.sender.username} -> {self.receiver.username}'