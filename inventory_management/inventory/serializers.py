from rest_framework import serializers
from .models import InventoryItem, InventoryChangeLog
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id','username','email','password','confirm_password']
        write_only_fields = 'password'

    def validate(self, data):
        """Checks if the two paswords are the same"""
        if data.get('password') =! data.get('confirm_password')

    
    def create(self, validated_data):
        user = User.objects.create_user(*validated_data)
        return user



class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'
        read_only_fields = ('user', 'date_added', 'last_updated')

    def validate(self, data):
        """Object level validation to validate quantity and price"""
        if data['quantity'] < 0:
            raise serializers.ValidationError("Quantity cannot be negative")
        if data['price'] <= 0:
            raise serializers.ValidationError("Price must be greater than zero")
        return data
    

class InventoryChangeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryChangeLog
        fields = '__all__'