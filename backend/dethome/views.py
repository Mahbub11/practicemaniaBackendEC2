from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes


from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(['GET', 'POST'])
def sample_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == "GET":
        
        return Response({"invalid": 'Invaid data provided'}, status=400)

