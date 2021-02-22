> Basic attributes list for models. Will be added to and drawn  
up as a proper schema once most of the models are done.

__Post__  
title = CharField()  
body = TextField()  
date_created = DateTimeField()  
date_modified = DateTimeField()  
author = CharField()  
upvotes = IntegerField()  
downvotes = IntegerField()  

__Course__  
course = CharField()  
college = CharField()  

__Quiz__  
title = CharField()  
subject = CharField()  
num_questions = IntegerField()  
author = CharField()  
date_created = DateTimeField()  