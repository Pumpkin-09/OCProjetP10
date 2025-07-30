from rest_framework import serializers
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'date_of_birth', 'can_be_contacted', 'can_data_be_shared', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def validate_date_of_birth(self, value):
        today = datetime.date.today()
        age = today.year - value.year - (
            (today.month, today.day) < (value.month, value.day)
        )
        
        if age < 16:
            raise serializers.ValidationError(
                "L'inscription est réservée aux personnes âgées de 16 ans ou plus."
            )
        
        return value
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user