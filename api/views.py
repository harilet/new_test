from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import emp
from .serializers import empserializers


class emplist(APIView):
    def get(self, request):
        emp1=emp.objects.all()
        serializers=empserializers(emp1,many=True)
        return Response(serializers.data)

    def post(self):
        return 