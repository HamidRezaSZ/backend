from django.db import models


class Images(models.Model):  # Image model
    image = models.ImageField(upload_to="images/")
