from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label = '', max_length=100)