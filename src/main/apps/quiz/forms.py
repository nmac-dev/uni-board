# forms.py
from django import forms
from django.utils.html import linebreaks
from .models import Quiz_Model

class Quiz_Model_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(Quiz_Model_Form, self).__init__(*args, **kwargs)
        # Required
        self.fields['title'].required      = True
        self.fields['desc'].required       = True
        self.fields['Question_1'].required = True
        self.fields['Question_1_Option_1'].required = True
        self.fields['Question_1_Option_2'].required = True
        self.fields['Question_1_Option_3'].required = True
        self.fields['Question_1_Option_4'].required = True
        self.fields['Question_1_Correct_Answer'].required  = True
        # Labels
            # Q1
        self.fields['Question_1'].label   = "Question 1"
        self.fields['Question_1_Option_1'].label   = "Question 1 Option 1"
        self.fields['Question_1_Option_2'].label   = "Question 1 Option 2"
        self.fields['Question_1_Option_3'].label   = "Question 1 Option 3"
        self.fields['Question_1_Option_4'].label   = "Question 1 Option 4"
        self.fields['Question_1_Correct_Answer'].label = "Question 1: Correct Answer is Option... 1, 2, 3, or 4"
            # Q2
        self.fields['Question_2'].label   = "Question 2"
        self.fields['Question_2_Option_1'].label   = "Question 2: Option 1"
        self.fields['Question_2_Option_2'].label   = "Question 2: Option 2"
        self.fields['Question_2_Option_3'].label   = "Question 2: Option 3"
        self.fields['Question_2_Option_4'].label   = "Question 2: Option 4"
        self.fields['Question_2_Correct_Answer'].label = "Question 2: Correct Answer is Option... 1, 2, 3, or 4"
            # Q3
        self.fields['Question_3'].label   = "Question 3"
        self.fields['Question_3_Option_2'].label   = "Question 3: Option 1"
        self.fields['Question_3_Option_3'].label   = "Question 3: Option 2"
        self.fields['Question_3_Option_4'].label   = "Question 3: Option 3"
        self.fields['Question_3_Option_4'].label   = "Question 3: Option 4"
        self.fields['Question_3_Correct_Answer'].label = "Question 3: Correct Answer is Option... 1, 2, 3, or 4"
            # Q4
        self.fields['Question_4'].label   = "Question 4"
        self.fields['Question_4_Option_1'].label   = "Question 4: Option 1"
        self.fields['Question_4_Option_2'].label   = "Question 4: Option 2"
        self.fields['Question_4_Option_3'].label   = "Question 4: Option 3"
        self.fields['Question_4_Option_4'].label   = "Question 4: Option 4"
        self.fields['Question_4_Correct_Answer'].label = "Question 4: Correct Answer is Option... 1, 2, 3, or 4"
            # Q5
        self.fields['Question_5'].label   = "Question 5"
        self.fields['Question_5_Option_1'].label   = "Question 5: Option 1"
        self.fields['Question_5_Option_2'].label   = "Question 5: Option 2"
        self.fields['Question_5_Option_3'].label   = "Question 5: Option 3"
        self.fields['Question_5_Option_4'].label   = "Question 5: Option 4"
        self.fields['Question_5_Correct_Answer'].label = "Question 5: Correct Answer is Option... 1, 2, 3, or 4"
            # Q6
        self.fields['Question_6'].label   = "Question 6"
        self.fields['Question_6_Option_1'].label   = "Question 6: Option 1"
        self.fields['Question_6_Option_2'].label   = "Question 6: Option 2"
        self.fields['Question_6_Option_3'].label   = "Question 6: Option 3"
        self.fields['Question_6_Option_4'].label   = "Question 6: Option 4"
        self.fields['Question_6_Correct_Answer'].label = "Question 6: Correct Answer is Option... 1, 2, 3, or 4"
            # Q7
        self.fields['Question_7'].label   = "Question 7"
        self.fields['Question_7_Option_1'].label   = "Question 7: Option 1"
        self.fields['Question_7_Option_2'].label   = "Question 7: Option 2"
        self.fields['Question_7_Option_3'].label   = "Question 7: Option 3"
        self.fields['Question_7_Option_4'].label   = "Question 7: Option 4"
        self.fields['Question_7_Correct_Answer'].label = "Question 7: Correct Answer is Option... 1, 2, 3, or 4"
            # Q8
        self.fields['Question_8'].label   = "Question 8"
        self.fields['Question_8_Option_1'].label   = "Question 8: Option 1"
        self.fields['Question_8_Option_2'].label   = "Question 8: Option 2"
        self.fields['Question_8_Option_3'].label   = "Question 8: Option 3"
        self.fields['Question_8_Option_4'].label   = "Question 8: Option 4"
        self.fields['Question_8_Correct_Answer'].label = "Question 8: Correct Answer is Option... 1, 2, 3, or 4"
            # Q9
        self.fields['Question_9'].label   = "Question 9"
        self.fields['Question_9_Option_1'].label   = "Question 9: Option 1"
        self.fields['Question_9_Option_2'].label   = "Question 9: Option 2"
        self.fields['Question_9_Option_3'].label   = "Question 9: Option 3"
        self.fields['Question_9_Option_4'].label   = "Question 9: Option 4"
        self.fields['Question_9_Correct_Answer'].label = "Question 9: Correct Answer is Option... 1, 2, 3, or 4"
            # Q10
        self.fields['Question_10'].label   = "Question 10"
        self.fields['Question_10_Option_1'].label   = "Question 10: Option 1"
        self.fields['Question_10_Option_2'].label   = "Question 10: Option 2"
        self.fields['Question_10_Option_3'].label   = "Question 10: Option 3"
        self.fields['Question_10_Option_4'].label   = "Question 10: Option 4"
        self.fields['Question_10_Correct_Answer'].label = "Question 10: Correct Answer is Option... 1, 2, 3, or 4"

    class Meta:
        model   = Quiz_Model
        exclude = ('quiz_id', 'creator', 'date')