from django.db import models
from statuses.models import Status
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from labels.models import Label


class Task(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("JustName"))
    description = models.TextField(verbose_name=_("Def"))
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name=_("Status"))
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author', verbose_name=_("Author"), null=True)
    executor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='executor', verbose_name=_("Executor"))
    labels = models.ManyToManyField(Label, verbose_name=_("Labels"), null=True)
    date_created = models.DateTimeField(auto_now_add=True)