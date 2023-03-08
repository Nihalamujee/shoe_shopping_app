from django.contrib.auth.forms import UserCreationForm
from .models import User,Brand,Product
from django import forms
from django.forms import ModelForm


class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Confirm Password'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class BrandForm(ModelForm):
    class Meta:
        model=Brand
        fields=('name','image','description','status')
        labels={
            'name':'',
            'image':'',
            'description':'',
            'status':'',
         }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Brand Name'}),
            'description':forms.TextInput(attrs={'class':'form-control','placeholder':'Description'}),
            'status':forms.TextInput(attrs={'class':'form-control','placeholder':'Status'}),

        }



class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields=('brand','category','name','vendor','product_image','quantity','price','description','status','trending')
        labels={
            'brand':'',
            'category':'',
            'name':'',
            'vendor':'',
            'product_image':'',
            'quantity':'',
            'price':'',
            'description':'',
            'status':'',
            'trending':'',
        }
        widgets={
            'brand':forms.Select(attrs={'class':'form-control','placeholder':'Brand Name'}),
            'category':forms.TextInput(attrs={'class':'form-control','placeholder':'Category'}),
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name of Product'}),
            'vendor':forms.TextInput(attrs={'class':'form-control','placeholder':'Vendor'}),
            'quantity':forms.TextInput(attrs={'class':'form-control','placeholder':'Quantity'}),
            'price':forms.TextInput(attrs={'class':'form-control','placeholder':'Price'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
            'status':forms.TextInput(attrs={'class':'form-control','placeholder':'Status'}),
            'trending':forms.TextInput(attrs={'class':'form-control','placeholder':'Trending'}),


}
