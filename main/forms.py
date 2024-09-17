from django.forms import ModelForm
from main.models import AdornmentsEntry

class AdornmentsEntryForm(ModelForm):
    class Meta:
        model = AdornmentsEntry
        fields = ["name", "price", "description", "size", "color", "quantity"]