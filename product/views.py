from django.shortcuts import render
from .forms import CommentForm

# Create your views here.
def comment_form(request):
    if request.method == 'POST':
        pass
    else:
        print(request.method)
        form = CommentForm()
        print(form.errors)
    return render(request, 'product/product_commant.html', {'form': form})