from django import forms

class FeedbackForm(forms.Form):
    Name=forms.CharField(label='Enter Your Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    Rating=forms.IntegerField(label='Enter Your Rating',widget=forms.NumberInput(attrs={'class':'form-control'}))
    Feedback=forms.CharField(label='Enter Your Feedback',widget=forms.Textarea(attrs={'class':'form-control'}))
