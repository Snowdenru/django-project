from django.shortcuts import render
import requests
import calendar
from datetime import datetime


def premier_movie(request):

    dict_month = {
        "Январь": "JANUARY",
        "Февраль": "FEBRUARY",
        "Март": "MARCH",
        "Апрель": "APRIL",
        "Май": "MAY",
        "Июнь": "JUNE",
        "Июль": "JULY",
        "Август": "AUGUST",
        "Сентабрь": "SEPTEMBER",
        "Октябрь": "OCTOBER",
        "Ноябрь": "NOVEMBER",
        "Декабрь": "DECEMBER",
    }

    list_of_months = list(calendar.month_name)[1:]

    month = request.GET.get("month")
    if not month:
        month = 'Декабрь'

    URL = "https://kinopoiskapiunofficial.tech/api/v2.2/films/premieres"

    params = {"year": 2024, "month": dict_month[month]}
    headers = {"X-API-KEY": "f8d19675-2000-42f4-af9e-e78137b3f8fe"}

    movies = requests.get(url=URL, params=params, headers=headers).json()["items"]

    # list of month names using calendar module

    return render(
        request,
        "movie/list_movie.html",
        context={"movies": movies, "list_of_months": dict_month},
    )
