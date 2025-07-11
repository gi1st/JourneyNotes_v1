from django.urls import path

from journeys.views import(
    journey_view,
    journey_detail_view,
    journey_create_view,
    journey_delete_view,
)

urlpatterns = [
    path("journeys/", journey_view, name="journeys"),
    path("journeys/<int:pk>/", journey_detail_view, name="journey-detail"),
    path("journeys/create/", journey_create_view, name="journey-create"),
    path("journeys/<int:pk>/delete/", journey_delete_view, name="journey-delete")
]

app_name = "journeys"
