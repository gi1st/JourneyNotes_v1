from django.utils import timezone
from datetime import timedelta
from django.test import TestCase
from django.contrib.auth import get_user_model
from journeys.models import Route


User = get_user_model()


class RouteModelTest(TestCase):


    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")


    def test_str_method_returns_title(self):
        route = Route.objects.create(title="Test Route", author=self.user)
        self.assertEqual(str(route), "Test Route")


    def test_route_ordering_by_updated_at(self):
        base_time = timezone.now()

        for i in range(3):
            route = Route.objects.create(
                title=f"TestTitle{i+1}",
                author=self.user,
            )
            Route.objects.filter(pk=route.pk).update(
                updated_at=base_time + timedelta(hours=i)
            )

        qs = Route.objects.all()

        self.assertEqual(qs[0].title, "TestTitle3")
        self.assertEqual(qs[1].title, "TestTitle2")
        self.assertEqual(qs[2].title, "TestTitle1")


    def test_create_route_with_required_fields(self):
        route = Route.objects.create(title="Test Route", author=self.user)
        self.assertIsNotNone(route.pk)
        self.assertEqual(route.title, "Test Route")
        self.assertEqual(route.author, self.user)
