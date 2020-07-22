from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your message has been saved')
    else:
        form = ContactForm()

    return render(request, 'tax/index.html', {'form': form})

def ads(request):
    return render(request, 'tax/app-ads.txt')

def privacy_policy(request):
    return render(request, 'tax/privacy-policy.html')

def privacy_policy2(request):
    return render(request, 'tax/privacy-policy2.html')
