from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.db.models import Count, Prefetch
from django.contrib.auth.decorators import login_required

from journeys.models import Route, Comment
from journeys.forms import JourneyCreateForm


def journey_view(request: HttpRequest) -> HttpResponse:
    journeys_list = (
        Route.objects
        .select_related("author")
        .annotate(comment_count=Count("comments"))
    )
    return render(request, "journeys/journeys.html", {"journeys_list": journeys_list})



def journey_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    journey_detail = (
        Route.objects
        .select_related("author")
        .annotate(comment_count=Count("comments"))
        .prefetch_related(
            Prefetch("comments", queryset=Comment.objects.select_related("author"))
        )
        .get(pk=pk)
    )
    return render(request, "journeys/journey_detail.html", {"journey_detail": journey_detail})


@login_required
def journey_create_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = JourneyCreateForm(request.POST)
        if form.is_valid():
            journey = form.save(commit=False)
            journey.author = request.user
            journey.save() 
            return redirect("journeys:journeys")
    else:
        form = JourneyCreateForm()
    return render(request, "journeys/journey_create.html", {"form": form})


def journey_delete_view(request: HttpRequest) -> HttpResponse:
    pass
