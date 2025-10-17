from django import forms
#from django.forms import CharField
#from library.usage import block
from  books.models import Book


# class BookForm(forms.Form):
#
#     title=forms.CharField()
#     author=forms.CharField()
#     pages=forms.IntegerField()
#     price=forms.IntegerField()
#     language=forms.CharField()

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields = '__all__'
