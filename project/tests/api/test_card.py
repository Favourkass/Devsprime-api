from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from db.models.learner import LearnerProfile


class PaymentCardTest(APITestCase):
    def setUp(self):
        get_user_model().objects.create(fullname='testlearner', email='test@admin.com', password='admin1234x')
        self.sample_learner = get_user_model().objects.get(fullname='testlearner')
        LearnerProfile.objects.create(user_id=self.sample_learner)
        self.sample_learner_card = LearnerProfile.objects.get(user_id=self.sample_learner)

    def test_add_card_success(self):
        payload = {            
            'account_name': 'John Doe',
            'account_number ': '0119639776',
            'bank_name': 'Guaranty Trust Bank',            
        }
        self.client.force_authenticate(user=self.sample_learner)
        res = self.client.post('/api/v1/learner/card/', payload)
        self.assertEqual(res.status_code, 200)

    def test_view_card(self):
        self.client.force_authenticate(user=self.sample_learner)
        res = self.client.get('/api/v1/learner/card/')
        self.assertEqual(res.status_code, 200)

    def test_delete_card(self):        
        self.client.force_authenticate(user=self.sample_learner)
        res = self.client.delete(f'/api/v1/learner/card/')
        self.assertEqual(res.status_code, 200)

    def tearDown(self):
        self.sample_learner.delete()
        self.sample_learner_card.delete()
