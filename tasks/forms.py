from tasks.models import Task
import django.forms as forms
import django_filters
from statuses.models import Status
from django.contrib.auth.models import User
from labels.models import Label
from django.utils.translation import gettext as _


class CreationTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "status", "executor", "labels"]


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(queryset=Status.objects.all())
    executor = django_filters.ModelChoiceFilter(queryset=User.objects.all(), field_name='executor')
    labels = django_filters.ModelChoiceFilter(queryset=Label.objects.all())
    author = django_filters.BooleanFilter(widget=forms.CheckboxInput, label=_("OnlyYours"), method='get_my_tasks')

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', 'author']

    def get_my_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user.pk)
        return queryset
