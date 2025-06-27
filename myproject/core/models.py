from django.db import models

from django.db import models

class TelegramUser(models.Model):
    username = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.username

