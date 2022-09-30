from tasks.models import Task
import django.forms as forms
import django_filters
from statuses.models import Status
from django.contrib.auth.models import User
from labels.models import Label
from django.utils.translation import gettext as _


def get_full_names():
        full_names = ()
        users = User.objects.filter(is_staff=False)
        for user in users:
            full_names += (user.id, user.get_full_name),
        return full_names


class CustomModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.get_full_name()


class CreationTaskForm(forms.ModelForm):
    executor = CustomModelChoiceField(queryset=User.objects.all(), label=_("Executor"))
    class Meta:
        model = Task
        fields = ["name", "description", "status", "executor", "labels"]


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(queryset=Status.objects.all())
    executor = django_filters.ChoiceFilter(field_name='executor', choices=get_full_names)
    labels = django_filters.ModelChoiceFilter(queryset=Label.objects.all(), label=_('Label'))
    author = django_filters.BooleanFilter(widget=forms.CheckboxInput, label=_("OnlyYours"), method='get_my_tasks')

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', 'author']

    def get_my_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user.pk)
        return queryset
