from django import forms 

class CommentForm(forms.Form):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'نام شما'
            })),
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'ایمیل شما'})),
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'نظر شما درباره محصول', 'rows': 4})),
