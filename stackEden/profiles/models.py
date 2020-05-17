from django.db import models
import uuid

# list of job roles
job_roles = [('Data Engineer', 'DATA ENGINEER'),
            ('Software Developer', 'SOFTWARE DEVELOPER'),
            ('Frontend developer', 'FRONTEND DEVELOPER'),
            ('Mobile App Developer', 'MOBILE APP DEVELOPER'),
            ('Technical analyst', 'TECHNINICAL ANALYST'),
            ('Product Manager', 'PRODUCT MANGER'),
            ('Project Manager', 'PROJECT MANAGER'),
            ('Data Scientist', 'DATA SCIENTIST'),
            ('Data Analyst', 'DATA ANALYST'),
            ('Database Admin', 'DATABASE ADMIN'),
            ('Quality Assurance Anlayst', 'QUALITY ASSUARANCE ANALYST'),
            ('DevOps Engineer', 'DEVOPS ENGINEER'),
            ('IT Manager', 'IT MANAGER'),
            ('IT Director', 'IT DIRECTOR')
        ]


class Job(models.Model):
    """Set up the jobs data model

    Attributes:
        uuid:   Primary key linking user to job posting
        titte:   Name of the job
        role_type:  Job category
        posted_by:   String value of who job posting represents
        date_opened:  Date job was posted
        date_cosed:   Date job was taken down
    """
    uuid = models.IntegerField(
        primary_key=True,  default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, editable=True)
    role_type = models.CharField(max_length=50, choices=job_roles)
    posted_by = models.CharField(max_length=100)
    date_opened = models.DateTimeField(auto_now_add=True)
    date_closed = models.DateTimeField(editable=True)

    def __str__(self):
        return self.title

# class
# Create your models here.

class Blog(models.Model):
    """Set up the jobs data model

    Attributes:
        uuid:   Primary key for blog posting
        titte:   Name of the blog post
        status:  Status of blog post | "draft"/"active" ... more?
        blog_type:   Blog type, maybe for categorization of posts?
        date_posted:  Date blog was posted
        text:   Text content of blog post 
    """    
        
    uuid = models.IntegerField(primary_key=True,  default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, editable=True)
    status = models.CharField(max_length=100, editable=True) # maybe for saving drafts? status="draft"/"active"
    blog_type = models.CharField(max_length=100, editable=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=5000, editable=True)

    def __str__(self):
        return self.title    
        
