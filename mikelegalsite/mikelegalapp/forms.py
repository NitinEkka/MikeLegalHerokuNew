from django import forms
from .models import Movie_List

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie_List
        fields = ('Title', 'Release_Date', 'Genre', 'Price', 'Rating')

    def __init__(self, *args, **kwargs):
        super(MovieForm, self).__init__(*args, **kwargs)
        self.fields['Genre'].empty_label = 'Select'
        self.fields['Title'].required = False