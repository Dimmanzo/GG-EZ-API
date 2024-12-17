from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

# Get the custom user model
User = get_user_model()


class CustomRegisterSerializer(serializers.ModelSerializer):
    """
    Custom registration serializer for user sign-up.
    """
    password1 = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )
    password2 = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password1', 'password2']
        extra_kwargs = {
            'email': {'required': True},
        }

    def validate(self, data):
        """
        Validate email presence and ensure both passwords match.
        """
        if not data.get('email'):
            raise serializers.ValidationError(
                {"email": "This field is required."}
            )
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                {"password2": "Passwords must match."}
            )
        return data

    def save(self, request):
        """
        Create a new user instance after successful validation.
        """
        validated_data = self.validated_data
        validated_data.pop('password2')
        password = validated_data.pop('password1')

        # Create a new user instance
        user = User(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            role=validated_data.get('role', 'default_user'),
        )
        user.set_password(password)
        user.save()
        return user
