import datetime

from django.db import models
from django.utils import timezone


class Name(models.Model):
    name_text = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.name_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Comment(models.Model):
    name = models.ForeignKey(Name)
    comment_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.comment_text
