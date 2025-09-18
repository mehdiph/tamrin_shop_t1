from django import forms 

class CommentForm(forms.Form):
    # name = forms.CharField(
    #     label='Name',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-input',
    #         'placeholder': 'نام شما'
    #         })),
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'ایمیل شما'})),
    # text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'نظر شما درباره محصول', 'rows': 4})),


    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control mb-2'
    }))