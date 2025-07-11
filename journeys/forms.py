from django import forms

from journeys.models import Route

class JourneyCreateForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ["title", "content"]
