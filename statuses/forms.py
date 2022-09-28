from statuses.models import Status
import django.forms as forms


class CreationStatusForm(forms.Form):
    class Meta:
        model = Status
        fields = ["name"]
