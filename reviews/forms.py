from django import forms
from .models import Reviews
from .widgets import CustomClearableFileInput


class ReviewsForm(forms.ModelForm):
    """
    Creates the Reviews form information
    """

    class Meta:
        model = Reviews
        fields = ("product_name", "product_review", "product_rating", "image")

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )
