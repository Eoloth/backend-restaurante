from django import forms
from products.models import Product

class ProductsAddListForm(forms.ModelForm):

    # here we only need to define the field we want to be editable
    genre = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), 
        required=False)