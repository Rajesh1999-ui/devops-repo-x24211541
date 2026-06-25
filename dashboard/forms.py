"""Forms for dashboard app."""
from django.forms import ModelForm

from shop.models import Product, Category


class AddProductForm(ModelForm):
    """Form for adding a new product."""
    class Meta:
        """Meta class for AddProductForm."""
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class AddCategoryForm(ModelForm):
    """Form for adding a new category."""
    class Meta:
        """Meta class for AddCategoryForm."""
        model = Category
        fields = ['title', 'sub_category', 'is_sub']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_sub'].widget.attrs['class'] = 'form-check-input'
        self.fields['sub_category'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['class'] = 'form-control'


class EditProductForm(ModelForm):
    """Form for editing an existing product."""
    class Meta:
        """Meta class for EditProductForm."""
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            