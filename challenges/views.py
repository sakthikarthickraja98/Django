from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Eat no meat"
    elif month == "february":
        challenge_text = "walk for 20 mins"
    elif month == "march":
        challenge_text = "Learn Django"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)

