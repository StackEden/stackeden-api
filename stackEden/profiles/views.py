from django.shortcuts import render
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from . import serializers
from .models import Job
from .models import Blog
from rest_framework import status
# Create your views here.


class Jobs(APIView):
    def get(self, request):
        """ Get all jobs record
        """
        jobs = Job.objects.all()
        serializer =serializers.jobSerializer(jobs, many=True)
        return Response(serializer.data)


    def post(self, request):
        """ Post new jobs 
        """
        serializer = serializers.jobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class JobsDetail(APIView):
    def get(self, request, uuid):
        """ Get call for specific job posting
        """
        try:
            job = Job.objects.get(pk = uuid)
        except Job.DoesNotExist:
            raise HTTP404
        serializer=serializers.jobSerializer(job)
        return Response(serializer.data)


    def delete(self, request, uuid):
        """Delete individual job
        """
        try: 
            job=Job.objects.get(pk=uuid)
        except Job.DoesNotExist:
            raise Http404
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

""" 
    Endpoint for Blog posts 
    path: /blogs
    HTTP methods: GET, POST
"""
class Blogs(APIView):
    # Get all blog records
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = serializers.blogSerializer(blogs, many=True)
        return Response(serializer.data)

    # Post new blog entry
    def post(self, request): 
        serializer = serializers.blogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

""" 
    Endpoint for Blog posts 
    path: /blogs/{uuid}
    HTTP methods: GET, DELETE
"""
class JobsDetail(APIView):
    # GET call for specific blog posting
    def get(self, request, uuid):
        try:
            blog = Blog.objects.get(pk = uuid)
        except Blog.DoesNotExist:
            raise HTTP404
        serializer = serializers.blogSerializer(blog)
        return Response(serializer.data)

    # PUT update blog entry
    def put(self, request, uuid): 
        serializer = serializers.blogSerializer(data=request.data)
        try:
            # TODO: this needs work. Do I need to loop through the attributes 
            # and update them based on the request object?
            blog = Blog.objects.update(pk = uuid)
        except:
            raise Http404
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    
    # DELETE individual blog
    def delete(self, request, uuid):
        try: 
            blog = Blog.objects.get(pk=uuid)
        except Blog.DoesNotExist:
            raise Http404
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)