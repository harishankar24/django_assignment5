from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Passenger
from .serializers import PassengerSerializer


@api_view(['GET','POST'])
def passenger_list(request):
    if request.method == 'GET':
        passengers = Passenger.objects.all()
        serializer = PassengerSerializer(passengers, many=True)
        return Response(serializer.data)    
    elif request.method == 'POST':
        serializer = PassengerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)