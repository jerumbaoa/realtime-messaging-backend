from django.db import models

# Create your models here.
class Chat(models.Model):
    """ Model which chat
    """
    sender = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name="sent_chats")
    receiver = models.ForeignKey(
        'users.User',
        models.CASCADE,
        related_name="received_chats")
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}'