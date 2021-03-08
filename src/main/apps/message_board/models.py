
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
    post_content    = models.TextField(     max_length=2549                 )
    post_date       = models.DateTimeField( default=timezone.now            )
    post_updated    = models.DateTimeField( auto_now=True                   )

    def __str__(self):
        return self.subject

# class User_Post_Comments(models.Model):
#     # PK
#     cmnt_id         = models.AutoField(     primary_key=True                )
#     # FK
#     cmnt_user       = models.ForeignKey(    User, on_delete=models.CASCADE  )
#     cmnt_post_id    = models.ForeignKey(    User, on_delete=models.CASCADE  )
#     # Attributes
#     cmnt_date_time  = models.DateTimeField( default=timezone.now            )
#     cmnt_details    = models.TextField(     max_length=1000                 )