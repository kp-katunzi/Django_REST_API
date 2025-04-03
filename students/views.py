from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, Subject
from .serializers import StudentSerializer, SubjectSerializer

@api_view(['GET'])
def students_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def subjects_list(request):
    subjects_by_year = {
        year: SubjectSerializer(Subject.objects.filter(year=year), many=True).data
        for year in range(1, 5)
    }
    return Response(subjects_by_year)
