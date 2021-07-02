from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(max_length=50, min_length=3)


