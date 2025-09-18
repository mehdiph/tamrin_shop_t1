from django import forms 

class CommentForm(forms.ModelForm):
    name = forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'نام شما'}),
    email = forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'ایمیل شما'}),
    text = forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'نظر شما درباره محصول', 'rows': 4}),



