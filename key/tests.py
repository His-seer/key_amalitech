from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import AccessKey
from datetime import datetime, timedelta
from django.utils import timezone


class AccessKeyTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345', email='test@example.com')
        self.admin = User.objects.create_superuser(username='admin', password='12345')
        self.client.login(username='admin', password='12345')
        self.key = AccessKey.objects.create(
            user=self.user, 
            status='active', 
            expiry_date=datetime.now() + timedelta(days=30)
        )

    def test_key_list_view(self):
        response = self.client.get(reverse('key_list'))
        self.assertEqual(response.status_code, 200)

    def test_admin_key_list_view(self):
        response = self.client.get(reverse('admin_key_list'))
        self.assertEqual(response.status_code, 200)

    def test_revoke_key(self):
        response = self.client.post(reverse('revoke_key', args=[self.key.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect to admin_key_list

    def test_key_status_api_active_key(self):
        response = self.client.get(reverse('key_status', args=[self.user.email]))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'status': 'active'})

    def test_key_status_api_no_active_key(self):
        self.key.delete()  # Ensure no active key
        response = self.client.get(reverse('key_status', args=[self.user.email]))
        self.assertEqual(response.status_code, 404)
