from django.shortcuts import render
from . models import Vocabulary
from rest_framework.decorators import api_view, permission_classes


from .SerializersVOC import SerializersVOC
from .SerializersReading import SerializersReading
from .SerializersWriting import SerializersWriting
from .SerializersSpeaking import SerializersSpeaking
from .SerializersListening import SerializersListening
from .SerializersStatistic import SerializersStatistic
from .models import Vocabulary
from .models import Reading
from .models import Writing
from .models import Speaking
from .models import Listening
from .models import StatisticDUOLINGO
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(['GET', 'POST'])
def voc_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == "GET":
        # list view
        queryset = Vocabulary.objects.all()
        data = SerializersVOC(queryset, many=True).data
        return Response(data)

    if method == "POST":

        # create an item
        # modifiedData = {'level': request.data['level'], 'time': request.data['time'], 'total_tested': 0, 'type': 1,
        #                 'inner_type': 11, 'qa': {'q': request.data['vocList'], 'a': request.data['ansList']}}
        serializer = SerializersVOC(data=request.data)
        if serializer.is_valid(raise_exception=True):

            serializer.save()
            return Response(serializer.data)
        return Response({"invalid": 'Invaid data provided'}, status=400)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def voc_detail(request, pk):

    try:
        voc = Vocabulary.objects.get(pk=pk)
    except SerializersVOC.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SerializersVOC(voc)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # modifiedData = {'level': request.data['level'], 'time': request.data['time'], 'total_tested': 0, 'type': 1,
        #                 'inner_type': 11, 'qa': {'q': request.data['vocList'], 'a': request.data['ansList']}}
        serializer = SerializersVOC(voc, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = SerializersVOC(voc,
                                    data=request.data,
                                    partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        voc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # reding


@api_view(['GET', 'POST'])
def reading_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == "GET":
        # list view
        queryset = Reading.objects.all()
        data = SerializersReading(queryset, many=True).data
        return Response(data)

    if method == "POST":

        serializer = SerializersReading(data=request.data)
        if serializer.is_valid(raise_exception=True):

            serializer.save()
            return Response(serializer.data)
        return Response({"invalid": 'Invaid data provided'}, status=400)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def reading_detail(request, pk):

    try:
        reading = Reading.objects.get(pk=pk)
    except SerializersReading.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SerializersReading(reading)
        return Response(serializer.data)

    elif request.method == 'PUT':

        serializer = SerializersReading(reading, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = SerializersReading(reading,
                                        data=request.data,
                                        partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        reading.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Writing


@api_view(['GET', 'POST'])
def writing_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == "GET":
        # list view
        queryset = Writing.objects.all()
        data = SerializersWriting(queryset, many=True).data
        return Response(data)

    if method == "POST":

        serializer = SerializersWriting(data=request.data)
        if serializer.is_valid(raise_exception=True):

            serializer.save()
            return Response(serializer.data)
        return Response({"invalid": 'Invaid data provided'}, status=400)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def writing_detail(request, pk):

    try:
        writing = Writing.objects.get(pk=pk)
    except SerializersWriting.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SerializersWriting(writing)
        return Response(serializer.data)

    elif request.method == 'PUT':

        serializer = SerializersWriting(writing, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = SerializersWriting(writing,
                                        data=request.data,
                                        partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        writing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

   # Speaking


@api_view(['GET', 'POST'])
def speaking_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == "GET":
        # list view
        queryset = Speaking.objects.all()
        data = SerializersSpeaking(queryset, many=True).data
        return Response(data)

    if method == "POST":

        serializer = SerializersSpeaking(data=request.data)
        if serializer.is_valid(raise_exception=True):

            serializer.save()
            return Response(serializer.data)
        return Response({"invalid": 'Invaid data provided'}, status=400)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def speaking_detail(request, pk):

    try:
        speaking = Speaking.objects.get(pk=pk)
    except SerializersSpeaking.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SerializersSpeaking(speaking)
        return Response(serializer.data)

    elif request.method == 'PUT':

        serializer = SerializersSpeaking(speaking, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = SerializersSpeaking(speaking,
                                         data=request.data,
                                         partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        speaking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

   # Listening


@api_view(['GET', 'POST'])
def listening_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == "GET":
        # list view
        queryset = Listening.objects.all()
        data = SerializersListening(queryset, many=True).data
        return Response(data)

    if method == "POST":

        serializer = SerializersListening(data=request.data)
        if serializer.is_valid(raise_exception=True):

            serializer.save()
            return Response(serializer.data)
        return Response({"invalid": 'Invaid data provided'}, status=400)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def listening_detail(request, pk):

    try:
        listening = Listening.objects.get(pk=pk)
    except SerializersListening.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SerializersListening(listening)
        return Response(serializer.data)

    elif request.method == 'PUT':

        serializer = SerializersListening(listening, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = SerializersListening(listening,
                                          data=request.data,
                                          partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        listening.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

   # Statisstic Data


@api_view(['POST'])
def save_statistic(request, *args, **kwargs):
    method = request.method

    if method == "POST":

        serializer = SerializersStatistic(data=request.data)
        if serializer.is_valid(raise_exception=True):

            serializer.save()
            return Response(serializer.data)
        return Response({"invalid": 'Invaid data provided'}, status=400)


@api_view(['GET'])
def get_statistic(request, userId, type, *args, **kwargs):
    method = request.method
    if method == "GET":
        # list view
        queryset = StatisticDUOLINGO.objects.filter(user=userId, type=type)
        data = SerializersStatistic(queryset, many=True).data
        return Response(data)
