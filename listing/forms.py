from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blog, Product, Inquiry


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'product_description', 'product_price', 'product_photo')

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ('title', 'question')

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog 
        fields = ('title', 'content', 'photo')