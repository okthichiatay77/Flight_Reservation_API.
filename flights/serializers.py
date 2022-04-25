from .models import *
from rest_framework import serializers
import re



class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight

        fields = '__all__'

    def validate_flightNumber(self, flightNumber):
        print('validate_flightNumber')
        if(re.match('^[a-zA-Z0-9]*$', flightNumber) == None):
            raise serializers.ValidationError('Invalid flight Number. Make sure it is alpha numberic')
        return flightNumber

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger

        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation

        fields = '__all__'