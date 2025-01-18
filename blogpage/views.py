from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from .forms import ContactForm
from html.parser import HTMLParser

# Create your views here.

class HTMLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.fed = []

    def handle_data(self, data):
        self.fed.append(data)

    def get_data(self):
        return ''.join(self.fed)

def strip_html_tags(html):
    stripper = HTMLStripper()
    stripper.feed(html)
    return stripper.get_data()

def index(request):
    with open('templates/blog1.html') as f:
        html_content = f.read()
        plain_text = strip_html_tags(html_content)

        content1 = "".join(plain_text.splitlines()[17])

    with open('templates/blog2.html') as f:
        html_content = f.read()
        plain_text = strip_html_tags(html_content)

        content2 = "".join(plain_text.splitlines()[17])

    with open('templates/blog3.html') as f:
        html_content = f.read()
        plain_text = strip_html_tags(html_content)

        content3 = "".join(plain_text.splitlines()[17])

    with open('templates/blog4.html') as f:
        html_content = f.read()
        plain_text = strip_html_tags(html_content)

        content4 = "".join(plain_text.splitlines()[17])

    with open('templates/blog5.html') as f:
        html_content = f.read()
        plain_text = strip_html_tags(html_content)

        content5 = "".join(plain_text.splitlines()[17])

    with open('templates/blog6.html') as f:
        html_content = f.read()
        plain_text = strip_html_tags(html_content)

        content6 = "".join(plain_text.splitlines()[17])
    
    return render(request, 'index.html', {'content1':content1,
                                          'content2':content2,
                                          'content3':content3,
                                          'content4':content4,
                                          'content5':content5,
                                          'content6':content6,})

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

def blog5(request):
    return render(request, 'blog5.html')

def blog6(request):
    return render(request, 'blog6.html')

# def carousel_page(request):
#     return render(request, 'carousel.html')

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