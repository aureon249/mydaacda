from django.db import models
from labels.models import Label


class Region(models.Model):

    def __str__(self):
        return self.question_text
