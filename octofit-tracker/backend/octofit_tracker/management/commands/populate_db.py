from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Daten löschen
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            User.objects.create(name='Superman', email='superman@dc.com', team=dc),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]

        # Activities
        for user in users:
            Activity.objects.create(user=user, type='Laufen', duration=30, date=timezone.now().date())
            Activity.objects.create(user=user, type='Radfahren', duration=45, date=timezone.now().date())

        # Workouts
        w1 = Workout.objects.create(name='Cardio Blast', description='Intensives Ausdauertraining')
        w2 = Workout.objects.create(name='Kraftpaket', description='Ganzkörper-Krafttraining')
        w1.suggested_for.set(users[:3])  # Marvel
        w2.suggested_for.set(users[3:])  # DC

        # Leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('Testdaten erfolgreich in octofit_db eingefügt.'))
