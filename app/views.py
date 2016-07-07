from django.shortcuts import render
from django.http import HttpResponseRedirect

from app.forms import UserForm


# Create your views here.
def fetch_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('Searching...')
    return render(request, 'app/search_user.html')
