from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

user = get_user_model()

class UserRegistrationsSerailizer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only = True , validators = [validate_password])
    password2 = serializers.CharField(write_only = True , validators = [validate_password])
    class Meta:
        model = user
        fields = (
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    # def validate(self, attrs):
    #     try:
    #         passwrd
    #     except:
    #         pass

    def create(self, validated_data):
        print('\033[91m'+'validated_data: ' + '\033[92m', validated_data)
        validated_data.pop("password2","")
        password1 = validated_data.pop("password1","")
        user_obj = user(**validated_data)
        user_obj.set_password(password1)
        user_obj.save()
        return user_obj
    
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only = True)

