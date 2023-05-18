from rest_framework import serializers

from .models import User
from apps.historytransfer.serializer import HistoryTransferSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'created_at', 'age', 'balance')
        
class UsersDetaliSerializer(serializers.ModelSerializer):
    from_user = HistoryTransferSerializer(read_only=True,many=True)    
    class Meta:
        model = User
        fields = ('id', 'username', 'email',
                  'phone_number', 'age', 'balance',
                  'wallet_address', 'from_user' )


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=100, write_only=True)             
    password2 = serializers.CharField(
        max_length=100, write_only=True)
    class Meta:
        model = User
        fields = ('username', 'first_name',
                  'last_name', 'email', 'phone_number', 'age',
                  'password', 'password2')
    
        def validate(self, attrs):
            if attrs['password'] != attrs['password2']:
                raise serializers.ValidationError ({'password2': 'Пароли отличаются'})
            if '+996' not in attrs['phone_number']:      
                raise serializers.ValidationError('Номер телефона должен быть в формате +996XXXXXXXXX')

    def create(self, values):
        user = User.objects.create(
            username=values['username'], phone_number=values['phone_number'],
            # age=values['age'],
             email=values['email'], 
            )
        user.set_password(values['password'])
        user.save()
        return user