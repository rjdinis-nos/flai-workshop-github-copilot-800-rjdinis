from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import date


class UserAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(name='Tony Stark', email='tony@marvel.com', age=45)

    def test_get_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        data = {'name': 'Steve Rogers', 'email': 'steve@marvel.com', 'age': 105}
        response = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_single_user(self):
        response = self.client.get(f'/api/users/{self.user.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Tony Stark')


class TeamAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(name='Thor Odinson', email='thor@marvel.com', age=1500)
        self.team = Team.objects.create(name='Team Marvel')
        self.team.members.set([self.user])

    def test_get_teams(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_team(self):
        data = {'name': 'Team DC'}
        response = self.client.post('/api/teams/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ActivityAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(name='Natasha Romanoff', email='natasha@marvel.com', age=38)

    def test_get_activities(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_activity(self):
        data = {
            'user_id': self.user.pk,
            'activity_type': 'Martial Arts',
            'duration': 90,
            'date': str(date.today())
        }
        response = self.client.post('/api/activities/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LeaderboardAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(name='Bruce Banner', email='bruce@marvel.com', age=49)

    def test_get_leaderboard(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_leaderboard_entry(self):
        data = {'user_id': self.user.pk, 'score': 800, 'rank': 5}
        response = self.client.post('/api/leaderboard/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class WorkoutAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_workouts(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_workout(self):
        data = {
            'name': 'Avengers Endurance',
            'description': 'High-intensity endurance workout.',
            'exercises': ['Sprint 100m', 'Push-ups x50', 'Pull-ups x20']
        }
        response = self.client.post('/api/workouts/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ApiRootTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_api_root(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)

    def test_root_redirects_to_api(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
