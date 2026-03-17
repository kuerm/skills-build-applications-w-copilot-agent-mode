from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        user1 = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        user2 = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        Activity.objects.create(user=user1, type='Running', duration=30, date='2023-01-01')
        Workout.objects.create(name='Pushups', description='Do 20 pushups')
        Leaderboard.objects.create(team=marvel, points=100)

    def test_user_team(self):
        user = User.objects.get(name='Iron Man')
        self.assertEqual(user.team.name, 'Marvel')

    def test_leaderboard(self):
        marvel = Team.objects.get(name='Marvel')
        leaderboard = Leaderboard.objects.get(team=marvel)
        self.assertEqual(leaderboard.points, 100)
