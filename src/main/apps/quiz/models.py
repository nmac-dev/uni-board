from django.db                  import models
from django.contrib.auth.models import User
from django.utils               import timezone

# Quizzes
class Quiz_Model(models.Model):
    # PK
    quiz_id         = models.AutoField(     primary_key=True    )
    # FK
    creator         = models.ForeignKey(    User, on_delete=models.CASCADE  )   # Remove post if op_user is deleted
    # Attributes
    title           = models.CharField(     max_length=127,         )
    desc            = models.TextField(     max_length=2549         )
    date            = models.DateTimeField( default=timezone.now    )
    # Questions
    # Q1
    Question_1                  = models.TextField( max_length=1024, null=True )
    Question_1_Option_1         = models.CharField( max_length=2048, null=True )
    Question_1_Option_2         = models.CharField( max_length=2048, null=True )
    Question_1_Option_3         = models.CharField( max_length=2048, null=True )
    Question_1_Option_4         = models.CharField( max_length=2048, null=True )
    Question_1_Correct_Answer   = models.PositiveSmallIntegerField(  null=True )
    # Q2
    Question_2                  = models.TextField( max_length=1024, null=True )
    Question_2_Option_1         = models.CharField( max_length=2048, null=True )
    Question_2_Option_2         = models.CharField( max_length=2048, null=True )
    Question_2_Option_3         = models.CharField( max_length=2048, null=True )
    Question_2_Option_4         = models.CharField( max_length=2048, null=True )
    Question_2_Correct_Answer   = models.PositiveSmallIntegerField(  null=True )
    # Q3
    Question_3                  = models.TextField( max_length=1024, null=True )
    Question_3_Option_1         = models.CharField( max_length=2048, null=True )
    Question_3_Option_2         = models.CharField( max_length=2048, null=True )
    Question_3_Option_3         = models.CharField( max_length=2048, null=True )
    Question_3_Option_4         = models.CharField( max_length=2048, null=True )
    Question_3_Correct_Answer   = models.PositiveSmallIntegerField(  null=True )
    # Q4
    Question_4                  = models.TextField( max_length=1024, null=True )
    Question_4_Option_1         = models.CharField( max_length=2048, null=True )
    Question_4_Option_2         = models.CharField( max_length=2048, null=True )
    Question_4_Option_3         = models.CharField( max_length=2048, null=True )
    Question_4_Option_4         = models.CharField( max_length=2048, null=True )
    Question_4_Correct_Answer   = models.PositiveSmallIntegerField(  null=True )
    # Q5
    Question_5                  = models.TextField( max_length=1024, null=True )
    Question_5_Option_1         = models.CharField( max_length=2048, null=True )
    Question_5_Option_2         = models.CharField( max_length=2048, null=True )
    Question_5_Option_3         = models.CharField( max_length=2048, null=True )
    Question_5_Option_4         = models.CharField( max_length=2048, null=True )
    Question_5_Correct_Answer   = models.PositiveSmallIntegerField(  null=True )
    # Q6
    Question_6                  = models.TextField( max_length=1024, null=True )
    Question_6_Option_1         = models.CharField( max_length=2048, null=True )
    Question_6_Option_2         = models.CharField( max_length=2048, null=True )
    Question_6_Option_3         = models.CharField( max_length=2048, null=True )
    Question_6_Option_4         = models.CharField( max_length=2048, null=True )
    Question_6_Correct_Answer   = models.PositiveSmallIntegerField(  null=True )
    # Q7
    Question_7                  = models.TextField( max_length=1024, null=True )
    Question_7_Option_1         = models.CharField( max_length=2048, null=True )
    Question_7_Option_2         = models.CharField( max_length=2048, null=True )
    Question_7_Option_3         = models.CharField( max_length=2048, null=True )
    Question_7_Option_4         = models.CharField( max_length=2048, null=True )
    Question_7_Correct_Answer   = models.PositiveSmallIntegerField(  null=True )
    # Q8
    Question_8                  = models.TextField( max_length=1024, null=True )
    Question_8_Option_1         = models.CharField( max_length=2048, null=True )
    Question_8_Option_2         = models.CharField( max_length=2048, null=True )
    Question_8_Option_3         = models.CharField( max_length=2048, null=True )
    Question_8_Option_4         = models.CharField( max_length=2048, null=True )
    Question_8_Correct_Answer   = models.PositiveSmallIntegerField(  null=True )
    # Q9
    Question_9                  = models.TextField( max_length=1024, null=True )
    Question_9_Option_1         = models.CharField( max_length=2048, null=True )
    Question_9_Option_2         = models.CharField( max_length=2048, null=True )
    Question_9_Option_3         = models.CharField( max_length=2048, null=True )
    Question_9_Option_4         = models.CharField( max_length=2048, null=True )
    Question_9_Correct_Answer   = models.PositiveSmallIntegerField(  null=True )
    # Q10
    Question_10                  = models.TextField( max_length=1024, null=True )
    Question_10_Option_1         = models.CharField( max_length=2048, null=True )
    Question_10_Option_2         = models.CharField( max_length=2048, null=True )
    Question_10_Option_3         = models.CharField( max_length=2048, null=True )
    Question_10_Option_4         = models.CharField( max_length=2048, null=True )
    Question_10_Correct_Answer   = models.PositiveSmallIntegerField(  null=True )

    def __str__(self):
        return self.quiz_title