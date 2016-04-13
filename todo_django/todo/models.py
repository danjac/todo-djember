from django.conf import settings
from django.db import models


class TodoItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    label = models.CharField(max_length=500)
    text = models.TextField(blank=True)
    done = models.BooleanField(default=False)

    class JSONAPIMeta:
        resource_name = "todos"
