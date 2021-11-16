from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk at least 20 minutes every day",
    "march": "Learn Django for at least 20 minutes a day",
    "april": "Eat no meat for the entire month",
    "may": "Walk at least 20 minutes every day",
    "june": "Learn Django for at least 20 minutes a day",
    "july": "Eat no meat for the entire month",
    "august": "Walk at least 20 minutes every day",
    "september": "Learn Django for at least 20 minutes a day",
    "october": "Eat no meat for the entire month",
    "november": "Walk at least 20 minutes every day",
    "december": "Learn Django for at least 20 minutes a day",
}


def monthly_list(request):
    list_items = ""
    for month in monthly_challenges.keys():
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        redirect_month = months[month - 1] # January = 1
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("This number does not translate into a month")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
