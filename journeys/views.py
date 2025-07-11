from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.db.models import Count

from journeys.models import Route


def journey_view(request: HttpRequest) -> HttpResponse:
    journeys_list = (
        Route.objects
        .select_related("author")
        .annotate(comment_count=Count("comments"))
    )
    return render(request, "journeys/journeys.html", {"journeys_list": journeys_list})



def journey_detail_view(request: HttpRequest) -> HttpResponse:
    pass


def journey_create_view(request: HttpRequest) -> HttpResponse:
    pass


def journey_delete_view(request: HttpRequest) -> HttpResponse:
    pass
