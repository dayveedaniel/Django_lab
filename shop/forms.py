from django import forms

from shop.models import Review


# class ReviewForm(forms.Form):
#     review = forms.CharField(widget=forms.Textarea, label='')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment']
        widgets = {
            "comment": forms.Textarea(),
        }
        labels = {
            "comment": "What do you think about this product",
        }
