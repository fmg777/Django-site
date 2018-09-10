from django.shortcuts import render

# Create your views here.



def str_home (request):
    return render(request, 'homepage/Home_Page.html')

def home (request):
    return render(request, 'homepage/Home_Page.html')


def contact (request):
    return render(request,'homepage/contact.html',{'value': ['Test information for address and telephone number']})
