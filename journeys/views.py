from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.db.models import Count, Prefetch
from django.contrib.auth.decorators import login_required

from journeys.models import Route, Comment
from journeys.forms import JourneyForm


def journey_list_view(request: HttpRequest) -> HttpResponse:
    journeys_list = (
        Route.objects
        .select_related("author")
        .annotate(comment_count=Count("comments"))
    )
    return render(request, "journeys/journeys-list.html", {"journeys_list": journeys_list})


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
    return render(request, "journeys/journey-detail.html", {"journey_detail": journey_detail})


@login_required
def journey_create_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = JourneyForm(request.POST)
        if form.is_valid():
            journey = form.save(commit=False)
            journey.author = request.user
            journey.save() 
            return redirect("journeys:journeys_list")
    else:
        form = JourneyForm()
    return render(request, "journeys/journey-create.html", {"form": form})


@login_required
def journey_update_view(request: HttpRequest, pk: int) -> HttpResponse:
    journey = get_object_or_404(Route, pk=pk)
    if journey.author != request.user:
        return redirect("journeys:journeys_list")

    if request.method == "POST":
        form = JourneyForm(request.POST, instance=journey)
        if form.is_valid():
            form.save()
            return redirect("journeys:journeys_list")
    else:
        form = JourneyForm(instance=journey)

    return render(request, "journeys/journey-update.html", {"form": form})


@login_required
def journey_delete_view(request: HttpRequest, pk: int) -> HttpResponse:
    if request.method == "POST":
        obj = get_object_or_404(Route, pk=pk)
        if obj.author == request.user:
            obj.delete()
        return redirect("journeys:journeys_list")
    else:
        return render(request, "journeys/journey-delete.html")
