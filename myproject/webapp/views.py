from django.shortcuts import render
from django.http import HttpResponse
from . forms import RegistrationForm
# Create your views here.
'''
def index(request):
    return HttpResponse("<h2>Hello, world. You're at the webapp index.</h2>")

'''

def index(request):
    form = RegistrationForm()
    content={
        "myregistrationform": form
    }

    return render(request,"webapp/index.html", content)

