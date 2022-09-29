from django import forms

from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label='Your name',  # label automatycznie User name
#     max_length=20,
#     error_messages={
#         'required': 'Your name must not be empty',
#         'max_length': 'EEEEEEEEEEE'
#     })
#     review_text = forms.CharField(label='Your feedback', widget=forms.Textarea)
#     rating = forms.IntegerField(label='Your rating', min_value=1, max_value=5)


# Model form
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__' 
        exclude = ['owner_text']
        labels = {
            'user_name': 'Your name',
            'review_text': 'Your feedback',
            'rating': 'Your rating'
        }
        error_messages = {
            'user_name': {
                'required': 'Your name must not be empty'
            }
        }