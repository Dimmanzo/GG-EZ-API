from dj_rest_auth.serializers import UserDetailsSerializer
from django.core.validators import EmailValidator, RegexValidator
from rest_framework import serializers
from django.contrib.auth import get_user_model

# Get the custom user model
User = get_user_model()


class CustomRegisterSerializer(serializers.ModelSerializer):
    """
    Custom registration serializer for user sign-up.
    """
    username = serializers.CharField(
        min_length=3,
        max_length=30,
        required=True,
        error_messages={
            "min_length": "Username must be at least 3 characters long.",
            "max_length": "Username cannot exceed 30 characters.",
            "blank": "Username cannot be empty.",
            "required": "Username is required."
        },
    )
    email = serializers.EmailField(
        validators=[
            EmailValidator(
                message="Please enter a valid email address."
            )
        ],
        required=True,
        error_messages={
            "invalid": "The email address you entered is not valid.",
            "blank": "Email cannot be empty.",
            "required": "Email is required."
        },
    )
    password1 = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'},
        validators=[
            RegexValidator(
                regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
                message="Password must be at least 8 characters long and include an uppercase letter, "
                        "a lowercase letter, a number, and a special character."
            )
        ],
        error_messages={
            "blank": "Password cannot be empty.",
            "required": "Password is required."
        },
    )
    password2 = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'},
        error_messages={
            "blank": "Password confirmation cannot be empty.",
            "required": "Password confirmation is required."
        },
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
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                {"password2": "Passwords do not match."}
            )

        # Minimum username length in the email's local part
        local_part = data['email'].split('@')[0]
        if len(local_part) < 3:
            raise serializers.ValidationError(
                {"email": "The username part of the email (before @) must be at least 3 characters long."}
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
