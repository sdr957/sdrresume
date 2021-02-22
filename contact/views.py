from django.shortcuts import render

# Create your views here.
def cont(request):
    return render(request, 'contact/contact.html ',{'contact':'active'})