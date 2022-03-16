from django.db import models


class Images(models.Model):  # Image model
    title = models.CharField(default=None, max_length=20)
    url = models.ImageField(upload_to="images/")
