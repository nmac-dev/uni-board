from django.test import TestCase
from django.db import models
from django.contrib.auth import get_user_model
from main.apps.message_board.models import User_Post
from datetime import datetime

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = get_user_model().objects.create_user(username='test', password='testpword1', email='test@example.com')
        user.save()
        User_Post.objects.create(
            post_subject='Title', 
            post_content='Body',
            post_user=user,
            post_date=datetime.now(),
            post_tags='tag1')

    def test_subject_label(self):
        post = User_Post.objects.get(post_id=1)
        field_label = post._meta.get_field('post_subject').verbose_name
        self.assertEqual(field_label, 'post subject')

    def test_body_label(self):
        post = User_Post.objects.get(post_id=1)
        field_label = post._meta.get_field('post_content').verbose_name
        self.assertEqual(field_label, 'post content')

    def test_date_label(self):
        post = User_Post.objects.get(post_id=1)
        field_label = post._meta.get_field('post_date').verbose_name
        self.assertEqual(field_label, 'post date')

    def test_updated_label(self):
        post = User_Post.objects.get(post_id=1)
        field_label = post._meta.get_field('post_updated').verbose_name
        self.assertEqual(field_label, 'post updated')

    def test_tags_label(self):
        post = User_Post.objects.get(post_id=1)
        field_label = post._meta.get_field('post_tags').verbose_name
        self.assertEqual(field_label, 'post tags')

    def test_subject_max_length(self):
        post = User_Post.objects.get(post_id=1)
        max_length = post._meta.get_field('post_subject').max_length
        self.assertEqual(max_length, 127)

    def test_body_max_length(self):
        post = User_Post.objects.get(post_id=1)
        max_length = post._meta.get_field('post_content').max_length
        self.assertEqual(max_length, 2048)