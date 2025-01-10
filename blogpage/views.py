from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from .forms import ContactForm

# Create your views here.
def index(request):
    # return ('This is a homepage.')
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def more(request):
    return render(request, 'more.html')

def blog1(request):
    return render(request, 'blog1.html')

def blog2(request):
    return render(request, 'blog2.html')

def blog3(request):
    return render(request, 'blog3.html')

def blog4(request):
    return render(request, 'blog4.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return render(request, 'success.html')  # Redirect after successful submission
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')