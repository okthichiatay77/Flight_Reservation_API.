from .models import *
from rest_framework.serializers import ModelSerializer



class FlightSerializer(ModelSerializer):

    class Meta:
        model = Flight

        fields = '__all__'


class PassengerSerializer(ModelSerializer):
    class Meta:
        model = Passenger

        fields = '__all__'


class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation

        fields = '__all__'