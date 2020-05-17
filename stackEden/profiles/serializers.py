from rest_framework import serializers
from . import models
import base64
from django.conf import settings
import os

class jobSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Job
        fields = ['uuid', 'title', 'role_type', 'posted_by', 'date_opened', 'date_closed']

class blogSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Blog
        fields = ['uuid', 'title', 'status', 'blog_type', 'date_posted', 'text']
