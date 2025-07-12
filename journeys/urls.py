from django.urls import path

from journeys.views import(
    journey_list_view,
    journey_detail_view,
    journey_create_view,
    journey_update_view,
    journey_delete_view,
    add_comment_view,
)

urlpatterns = [
    path("journeys-list/", journey_list_view, name="journeys_list"),
    path("journeys/<int:pk>/", journey_detail_view, name="journey_detail"),
    path("journeys/create/", journey_create_view, name="journey_create"),
    path("journeys/<int:pk>/update/", journey_update_view, name="journey_update"),
    path("journeys/<int:pk>/delete/", journey_delete_view, name="journey_delete"),
    path("journeys/<int:pk>/add-comment", add_comment_view, name="add_comment"),
]

app_name = "journeys"
