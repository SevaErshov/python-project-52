from tasks.models import Task
import django.forms as forms


class CreationTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "status", "executor"]