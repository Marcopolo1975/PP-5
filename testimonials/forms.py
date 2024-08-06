from django import forms
from .models import Testimonial
from products.widgets import CustomClearableFileInput

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['product_name','body',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-gold'