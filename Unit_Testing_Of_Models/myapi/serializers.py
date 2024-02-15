from rest_framework import serializers  
from rest_framework_simplejwt.tokens import RefreshToken  
from .models import Employee, Attendance, Accounts  # Importing models from current package

# Serializer for Employee model
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        # Model to serialize
        model = Employee
        # Include all fields in the serialization
        fields = '__all__'

# Serializer for Attendance model
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        # Model to serialize
        model = Attendance
        # Include all fields in the serialization
        fields = '__all__'

# Serializer for Accounts model
class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        # Model to serialize
        model = Accounts
        # Include all fields in the serialization
        fields = '__all__'

# Serializer for token obtain
class TokenObtainPairSerializer(serializers.Serializer):
    """
    Serializer for token obtain (login)
    """
    # Fields for token obtain
    username = serializers.CharField()  # Field for username
    password = serializers.CharField(  # Field for password
        style={'input_type': 'password'},  # Rendering as password input
        trim_whitespace=False  # Do not trim whitespace
    )

    def validate(self, attrs):  # Method to validate input
        username = attrs.get('username')  # Getting username from input
        password = attrs.get('password')  # Getting password from input

        if username and password:  # If both username and password are provided
            if Employee.objects.filter(username=username).exists():  # If user with provided username exists
                user = Employee.objects.get(username=username)  # Retrieve user object

                if user.check_password(password):  # If password matches with user's password
                    refresh = RefreshToken.for_user(user)  # Generate refresh token for user

                    return {  # Returning tokens
                        'refresh': str(refresh),  # Refresh token
                        'access': str(refresh.access_token),  # Access token
                    }
            else:  # If user with provided username does not exist
                msg = 'Unable to log in with provided credentials.'  # Error message
                raise serializers.ValidationError(msg)  # Raise validation error
        else:  # If either username or password is missing
            msg = 'Must include "username" and "password".'  # Error message
            raise serializers.ValidationError(msg)  # Raise validation error

# Serializer for token refresh
class TokenRefreshSerializer(serializers.Serializer):
    """
    Serializer for token refresh
    """
    # Field for token refresh
    refresh = serializers.CharField()  # Field for refresh token

    def validate(self, attrs):  # Method to validate input
        refresh = attrs.get('refresh')  # Getting refresh token from input

        if refresh:  # If refresh token is provided
            try:
                RefreshToken(refresh)  # Check if refresh token is valid
            except Exception:  # If refresh token is invalid
                msg = 'Invalid refresh token.'  # Error message
                raise serializers.ValidationError(msg)  # Raise validation error

            return attrs  # Return validated data
        else:  # If refresh token is missing
            msg = 'Must include "refresh" token.'  # Error message
            raise serializers.ValidationError(msg)  # Raise validation error
