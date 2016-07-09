from django.shortcuts import render
from django.http import HttpResponse

from app.forms import UserForm


# Create your views here.
def fetch_user(request):
    if 'username' in request.GET:
        form = UserForm(request.GET)
        if form.is_valid():
            salute = 'Hi {0}!'.format(form.cleaned_data.get('username'))
            return HttpResponse(salute)
    return render(request, 'app/search_page.html', {'form': UserForm()})
