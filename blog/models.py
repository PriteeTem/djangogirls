from django.db import models

from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class  Item (models.Model):
    # Fields
    request_id = models.CharField(max_length=20, help_text='Request ID')
    link_session_id = models.CharField(max_length=20, help_text='Session ID')
    plaid_access_token = models.CharField(max_length=20, help_text='Access Token')
    item_id = models.CharField(max_length=20, help_text='Item ID')
    institution_id= models.CharField(max_length=20, help_text='Insitution ID')
    created_at=models.DateTimeField(default=timezone.now)

    def create_Item (self):
        self.request_id = input
        self.save
     
    def __str__(self):
        return self.item_id

