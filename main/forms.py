from django.forms import ModelForm
from main.models import AdornmentsEntry
from django.utils.html import strip_tags

class AdornmentsEntryForm(ModelForm):
    class Meta:
        model = AdornmentsEntry
        fields = ["name", "price", "description", "size", "color", "quantity"]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data.get("description")
        return strip_tags(description)

    def clean_size(self):
        size = self.cleaned_data.get("size")
        return strip_tags(size)

    def clean_color(self):
        color = self.cleaned_data.get("color")
        return strip_tags(color)