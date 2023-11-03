from rest_framework import serializers
from .models import Guest, Movie, Reservation



class MovieSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


    


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['pk','guest_reservation', 'name', 'phone']



 

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'