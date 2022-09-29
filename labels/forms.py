from labels.models import Label
import django.forms as forms


class CreationStatusForm(forms.Form):
    class Meta:
        model = Label
        fields = ["name"]
