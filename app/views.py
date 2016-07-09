from django.shortcuts import render
from django.http import HttpResponse

from app.forms import UserForm
from app.social import Twitter


# Create your views here.
def fetch_user(request):
    if 'username' in request.GET:
        form = UserForm(request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('username')
            twitter = Twitter(name)
            recent_tweets = twitter.save_tweets()
            context = {
                'tweets': recent_tweets,
                'username': name
            }
            return render(request, 'app/results.html', context)
    return render(request, 'app/search.html', {'form': UserForm()})
