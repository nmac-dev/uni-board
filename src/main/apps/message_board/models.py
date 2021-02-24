
from django.db                  import models
from django.contrib.auth.models import User
from django.utils               import timezone

#   Models

class User_Post(models.Model):
    post_id         = models.AutoField(     primary_key=True                )
    op_user         = models.ForeignKey(    User, on_delete=models.CASCADE  )   # Remove post if op_user is deleted
    subject         = models.CharField(     max_length=127                  )
    content         = models.TextField(     max_length=2549                 )
    date_time       = models.DateTimeField( default=timezone.now            )
    last_update     = models.DateTimeField( auto_now=True                   )

    def __str__(self):
        return self.subject

# class User_Post_Replies(models.Model):
#     reply_id        = models.AutoField(     primary_key=True                )
#     or_user         = models.ForeignKey(    User, on_delete=models.CASCADE  )
#     date_time       = models.DateTimeField( default=timezone.now            )
#     comment         = models.TextField(     max_length=1000                 )