from django.test import TestCase
from django.db import models
from django.contrib.auth import get_user_model
from main.apps.leaderboard.models import Leaderboard
from datetime import datetime

class LeaderboardModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = get_user_model().objects.create_user(username='test', password='testpword1', email='test@example.com')
        user.save()
        Leaderboard.objects.create(
            user=user,
            points=4,)

    def test_user_id(self):
        leaderboard = Leaderboard.objects.get(pk = 1)
        field_value = leaderboard.user.username
        self.assertEqual(field_value, 'test')

    def test_points_value(self):
        leaderboard = Leaderboard.objects.get(pk = 1)
        field_value = leaderboard.points
        self.assertEqual(field_value, 4)

    def test_points_value_increment(self):
        leaderboard = Leaderboard.objects.get(pk = 1)
        leaderboard.points += 1
        leaderboard.save()
        leaderboard = Leaderboard.objects.get(pk = 1)
        field_value = leaderboard.points
        self.assertEqual(field_value, 5)

    def test_points_value_decrement(self):
        leaderboard = Leaderboard.objects.get(pk = 1)
        leaderboard.points -= 1
        leaderboard.save()
        leaderboard = Leaderboard.objects.get(pk = 1)
        field_value = leaderboard.points
        self.assertEqual(field_value, 3)