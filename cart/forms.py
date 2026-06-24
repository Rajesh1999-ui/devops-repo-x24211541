"""Forms for cart app."""
from django import forms


class QuantityForm(forms.Form):
    """Form for selecting product quantity."""
    quantity = forms.IntegerField(
        label='',
        min_value=1,
        max_value=9,
        widget=forms.NumberInput(
            attrs={'class': 'form-control mt-1', 'placeholder': 'quantity'}
        )
    )