from django import forms

from journeys.models import Route, Comment

class JourneyForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ["title", "content"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]


class RouteTitleSearchForm(forms.Form):
    title = forms.CharField(
        max_length=63,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by title"
            }
        )
    )
