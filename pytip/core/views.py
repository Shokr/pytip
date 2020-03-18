from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .froms import *


@login_required
def addTweet(request):
    if request.method == 'POST':
        created_Tweet_pk = None
        filled_form = TweetForm(request.POST)
        if filled_form.is_valid():
            created_Tweet = filled_form.save()
            created_Tweet_pk = created_Tweet.pk
            note = 'Tweet %s was created' % (filled_form.cleaned_data['name'])
            filled_form = TweetForm()
        else:
            note = 'Tweet was not created, please try again'
        new_form = TweetForm()

        return render(request, 'core/addTweet.html',
                      {'TweetForm': filled_form, 'note': note, 'created_Tweet_pk': created_Tweet_pk})
        # return redirect('core:list_Tweets')
    else:
        form = TweetForm()
        return render(request, 'core/addTweet.html', {'TweetForm': form})


@login_required
def editTweet(request, pk):
    tweet = Tweet.objects.get(pk=pk)
    form = TweetForm(instance=tweet)
    if request.method == 'POST':
        filled_form = TweetForm(request.POST, instance=tweet)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Your Tweet has been processed.'
            return render(request, 'core/editTweet.html', {'TweetForm': form, 'Tweet': tweet, 'note': note})
            # return redirect('core:list_Tweets')
    return render(request, 'core/editTweet.html', {'TweetForm': form, 'Tweet': tweet})


@login_required
def viewTweet(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    return render(request, 'core/viewTweet.html', {'Tweet': tweet})


@login_required
def listTweets(request):
    tweets = Tweet.objects.get_queryset()
    return render(request, 'core/home.html', {'Tweets': tweets})


@login_required
def deleteTweet(request, pk):
    tweet = Tweet.objects.get(pk=pk)
    tweet.delete()
    return redirect('core:home')
