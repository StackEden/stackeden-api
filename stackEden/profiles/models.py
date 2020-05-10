from django.db import models
import uuid

job_roles = [('Data Engineer', 'DATA ENGINEER'),
            ('Software Developer', 'SOFTWARE DEVELOPER'),
            ('Frontend developer', 'FRONTEND DEVELOPER'),
            ('Mobile App Developer', 'MOBILE APP DEVELOPER'),
            ('Technical analyst', 'TECHNINICAL ANALYST'),
            ('Product Manager', 'PRODUCT MANGER'),
            ('Project Manager','PROJECT MANAGER' ),
            ('Data Scientist','DATA SCIENTIST'),
            ('Data Analyst', 'DATA ANALYST'),
            ('Database Admin', 'DATABASE ADMIN'),
            ('Quality Assurance Anlayst', 'QUALITY ASSUARANCE ANALYST' ),
            ('DevOps Engineer', 'DEVOPS ENGINEER'),
            ('IT Manager', 'IT MANAGER'),
            ('IT Director', 'IT DIRECTOR')
        ]
class Job(models.Model):
    uuid = models.IntegerField(primary_key=True,  default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, editable=True)
    role_type = models.CharField(max_length=50,choices=job_roles)
    posted_by = models.CharField(max_length=100)
    date_opened = models.DateTimeField(auto_now_add=True)
    date_closed = models.DateTimeField(editable=True)

    def __str__(self):
        return self.title
    
# class 
# Create your models here.
