from django.test import TestCase
from django.db import models
from django.contrib.auth import get_user_model
from main.apps.quiz.models import Quiz_Model
from datetime import datetime

class QuizModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = get_user_model().objects.create_user(username='test', password='testpword1', email='test@example.com')
        user.save()
        Quiz_Model.objects.create(
            title='Title', 
            desc='Description',
            creator=user,
            date=datetime.now(),
            Question_1='q1',
            Question_1_Option_1='option1',
            Question_1_Correct_Answer=1)

    def test_title_label(self):
        quiz = Quiz_Model.objects.get(quiz_id=1)
        field_label = quiz._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_desc_label(self):
        quiz = Quiz_Model.objects.get(quiz_id=1)
        field_label = quiz._meta.get_field('desc').verbose_name
        self.assertEqual(field_label, 'desc')

    def test_date_label(self):
        quiz = Quiz_Model.objects.get(quiz_id=1)
        field_label = quiz._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

    def test_question_label(self):
        quiz = Quiz_Model.objects.get(quiz_id=1)
        field_label = quiz._meta.get_field('Question_1').verbose_name
        self.assertEqual(field_label, 'Question 1')

    def test_option_label(self):
        quiz = Quiz_Model.objects.get(quiz_id=1)
        field_label = quiz._meta.get_field('Question_1_Option_1').verbose_name
        self.assertEqual(field_label, 'Question 1 Option 1')

    def test_question_max_length(self):
        quiz = Quiz_Model.objects.get(quiz_id=1)
        max_length = quiz._meta.get_field('Question_1').max_length
        self.assertEqual(max_length, 1024)

    def test_option_max_length(self):
        quiz = Quiz_Model.objects.get(quiz_id=1)
        max_length = quiz._meta.get_field('Question_1_Option_1').max_length
        self.assertEqual(max_length, 2048)

    def test_question_value(self):
        quiz = Quiz_Model.objects.get(quiz_id=1)
        field_value = quiz.Question_1
        self.assertEqual(field_value, 'q1')

    def test_title_value(self):
        quiz = Quiz_Model.objects.get(quiz_id=1)
        field_value = quiz.title
        self.assertEqual(field_value, 'Title')

    def test_desc_value(self):
        quiz = Quiz_Model.objects.get(quiz_id=1)
        field_value = quiz.desc
        self.assertEqual(field_value, 'Description')

    def test_answer_value(self):
        quiz = Quiz_Model.objects.get(quiz_id=1)
        field_value = quiz.Question_1_Option_1
        self.assertEqual(field_value, 'option1')

    def test_correct_answer_value(self):
        quiz = Quiz_Model.objects.get(quiz_id=1)
        field_value = quiz.Question_1_Correct_Answer
        self.assertEqual(field_value, 1)
