from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Creating users (superheroes)...')
        users_data = [
            {'name': 'Tony Stark', 'email': 'tony@marvel.com', 'age': 45},
            {'name': 'Steve Rogers', 'email': 'steve@marvel.com', 'age': 105},
            {'name': 'Natasha Romanoff', 'email': 'natasha@marvel.com', 'age': 38},
            {'name': 'Thor Odinson', 'email': 'thor@marvel.com', 'age': 1500},
            {'name': 'Bruce Banner', 'email': 'bruce@marvel.com', 'age': 49},
            {'name': 'Bruce Wayne', 'email': 'bruce@dc.com', 'age': 40},
            {'name': 'Clark Kent', 'email': 'clark@dc.com', 'age': 35},
            {'name': 'Diana Prince', 'email': 'diana@dc.com', 'age': 5000},
            {'name': 'Barry Allen', 'email': 'barry@dc.com', 'age': 28},
            {'name': 'Hal Jordan', 'email': 'hal@dc.com', 'age': 34},
        ]
        users = {}
        for u in users_data:
            user = User.objects.create(**u)
            users[u['email']] = user
            self.stdout.write(f'  Created user: {user.name}')

        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(name='Team Marvel')
        team_marvel.members.set([
            users['tony@marvel.com'],
            users['steve@marvel.com'],
            users['natasha@marvel.com'],
            users['thor@marvel.com'],
            users['bruce@marvel.com'],
        ])

        team_dc = Team.objects.create(name='Team DC')
        team_dc.members.set([
            users['bruce@dc.com'],
            users['clark@dc.com'],
            users['diana@dc.com'],
            users['barry@dc.com'],
            users['hal@dc.com'],
        ])
        self.stdout.write(f'  Created team: {team_marvel.name}')
        self.stdout.write(f'  Created team: {team_dc.name}')

        self.stdout.write('Creating activities...')
        activities_data = [
            {'user': users['tony@marvel.com'], 'activity_type': 'Flying', 'duration': 60, 'date': date(2024, 1, 1)},
            {'user': users['steve@marvel.com'], 'activity_type': 'Running', 'duration': 45, 'date': date(2024, 1, 2)},
            {'user': users['natasha@marvel.com'], 'activity_type': 'Martial Arts', 'duration': 90, 'date': date(2024, 1, 3)},
            {'user': users['thor@marvel.com'], 'activity_type': 'Hammer Throw', 'duration': 30, 'date': date(2024, 1, 4)},
            {'user': users['bruce@marvel.com'], 'activity_type': 'Yoga', 'duration': 60, 'date': date(2024, 1, 5)},
            {'user': users['bruce@dc.com'], 'activity_type': 'Strength Training', 'duration': 75, 'date': date(2024, 1, 1)},
            {'user': users['clark@dc.com'], 'activity_type': 'Flying', 'duration': 120, 'date': date(2024, 1, 2)},
            {'user': users['diana@dc.com'], 'activity_type': 'Combat Training', 'duration': 90, 'date': date(2024, 1, 3)},
            {'user': users['barry@dc.com'], 'activity_type': 'Speed Running', 'duration': 15, 'date': date(2024, 1, 4)},
            {'user': users['hal@dc.com'], 'activity_type': 'Space Flight', 'duration': 180, 'date': date(2024, 1, 5)},
        ]
        for a in activities_data:
            activity = Activity.objects.create(**a)
            self.stdout.write(f'  Created activity: {activity}')

        self.stdout.write('Creating leaderboard entries...')
        leaderboard_data = [
            {'user': users['tony@marvel.com'], 'score': 950, 'rank': 2},
            {'user': users['steve@marvel.com'], 'score': 870, 'rank': 4},
            {'user': users['natasha@marvel.com'], 'score': 920, 'rank': 3},
            {'user': users['thor@marvel.com'], 'score': 1000, 'rank': 1},
            {'user': users['bruce@marvel.com'], 'score': 800, 'rank': 6},
            {'user': users['bruce@dc.com'], 'score': 840, 'rank': 5},
            {'user': users['clark@dc.com'], 'score': 990, 'rank': 2},
            {'user': users['diana@dc.com'], 'score': 960, 'rank': 3},
            {'user': users['barry@dc.com'], 'score': 880, 'rank': 4},
            {'user': users['hal@dc.com'], 'score': 750, 'rank': 7},
        ]
        for lb in leaderboard_data:
            entry = Leaderboard.objects.create(**lb)
            self.stdout.write(f'  Created leaderboard entry: {entry}')

        self.stdout.write('Creating workouts...')
        workouts_data = [
            {
                'name': 'Avengers Endurance',
                'description': 'High-intensity endurance workout inspired by the Avengers.',
                'exercises': ['100m sprint', 'Push-ups x50', 'Pull-ups x20', 'Burpees x30']
            },
            {
                'name': 'Iron Man Strength Circuit',
                'description': 'Strength-focused circuit training like Tony Stark in his workshop.',
                'exercises': ['Bench Press 5x5', 'Deadlift 5x5', 'Squat 5x5', 'Overhead Press 5x5']
            },
            {
                'name': 'Justice League HIIT',
                'description': 'High-intensity interval training for DC heroes.',
                'exercises': ['Box jumps x20', 'Battle ropes 60s', 'Kettlebell swings x25', 'Mountain climbers 60s']
            },
            {
                'name': 'Wonder Woman Warrior',
                'description': 'Combat and agility training inspired by Diana Prince.',
                'exercises': ['Agility ladder drills', 'Medicine ball throws x15', 'Lunge matrix x20', 'Core planks 3x60s']
            },
            {
                'name': 'Flash Speed Training',
                'description': 'Speed and agility workout for the Fastest Man Alive.',
                'exercises': ['Sprint intervals 10x100m', 'Plyometric jumps x20', 'High knees 4x30s', 'Lateral shuffles 4x30s']
            },
        ]
        for w in workouts_data:
            workout = Workout.objects.create(**w)
            self.stdout.write(f'  Created workout: {workout.name}')

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
