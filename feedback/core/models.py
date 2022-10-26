from colorfield.fields import ColorField
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Feature(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)
    color = ColorField(default="#FF0000")

    def __str__(self):
        return self.name


class TaggedFeature(models.Model):
    tag = models.ForeignKey(Tag, models.CASCADE)
    feature = models.ForeignKey(Feature, models.CASCADE, related_name="linked_tags")


class Feedback(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, models.CASCADE, related_name="user_feedbacks")
    feature = models.ForeignKey(Feature, models.CASCADE, related_name="feedbacks")
