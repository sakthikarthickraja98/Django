from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january":"Eat no meat",
    "february":"Walk for 20 mins",
    "march":"Learn Django",
    "april":"Eat no meat",
    "may":"Walk for 20 mins",
    "june":"Learn Django",
    "july":"Eat no meat",
    "august":"Walk for 20 mins",
    "spetember":"Learn Django",
    "october":"Eat no meat",
    "november":"Walk for 20 mins",
    "december":"Learn Django",
}
# Create your views here.

def monthly_challenge_by_number(request,month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")

