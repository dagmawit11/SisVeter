from django import forms
from .models import About


class AboutAdminForm(forms.ModelForm):

    features = forms.CharField(
        widget=forms.Textarea(attrs={
            "rows": 6,
            "placeholder": "Enter one feature per line"
        }),
        help_text="Enter one feature on each line."
    )

    class Meta:
        model = About
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.features:
            self.fields["features"].initial = "\n".join(
                self.instance.features
            )

    def clean_features(self):
        data = self.cleaned_data["features"]

        return [
            item.strip()
            for item in data.splitlines()
            if item.strip()
        ]