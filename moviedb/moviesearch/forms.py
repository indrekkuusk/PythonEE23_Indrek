from django import forms

class MovieSearchForm(forms.Form):
    query = forms.CharField(label='Search for a Movie', max_length=100)
