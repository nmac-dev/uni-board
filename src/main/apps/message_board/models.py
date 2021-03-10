
from django.db                  import models
from django.contrib.auth.models import User
from django.utils               import timezone

#   Models

class User_Post(models.Model):
    # PK
    post_id         = models.AutoField(     primary_key=True                )
    # FK
    post_user       = models.ForeignKey(    User, on_delete=models.CASCADE  )   # Remove post if op_user is deleted
    # Attributes
    post_subject    = models.CharField(     max_length=127                  )
    post_content    = models.TextField(     max_length=2048                 )
    post_date       = models.DateTimeField( default=timezone.now            )
    post_updated    = models.DateTimeField( auto_now=True                   )
    post_tags       = models.CharField(     max_length=1024, null=True, blank=True )
    likes           = models.ManyToManyField(User, related_name='post'      )

    def total_Likes(self):
        return self.likes.count()

    def __str__(self):
        return self.post_subject

class User_Comment(models.Model):
    # PK
    cmnt_id = models.AutoField(     primary_key=True    )
    # FK
    poster  = models.ForeignKey(    User, on_delete=models.CASCADE                  )
    post_id = models.ForeignKey(    User_Post, null=True, on_delete=models.CASCADE  )
    # Attributes
    date    = models.DateTimeField( default=timezone.now    )
    details = models.TextField(     max_length=1024         )