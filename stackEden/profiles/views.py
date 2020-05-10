from django.shortcuts import render
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from . import serializers
from .models import Job
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