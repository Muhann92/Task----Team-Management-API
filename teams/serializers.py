from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Task, Team
import re
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the Custom User model.
    Defines which user fields are exposed via the API.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model.
    Handles serialization of all fields, with specific fields set to read-only.
    """
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'assigned_to']

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150, required=True)
    password = serializers.CharField(max_length=128,style={'input_type': 'password'}, write_only=True)
    password_confirm = serializers.CharField(max_length=128,style={'input_type': 'password'}, write_only=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirm', 'email', 'first_name', 'last_name')

    def validate(self, attrs):
        errors = {}
        # 0. Username Validation
        if not attrs.get('username').isalnum():
            errors['username'] = "Username must contain only letters and numbers."
        elif len(attrs.get('username')) < 6:
            errors['username'] = "Username must be at least 6 characters long."
        elif len(attrs.get('username')) > 150:
            errors['username'] = "Username must be at most 150 characters long."


        # 1. Password Validation
        if attrs.get('password') != attrs.get('password_confirm'):
            errors['password_confirm'] = "Passwords do not match."
        elif len(attrs.get('password')) < 8:
            errors['password'] = "Password must be at least 8 characters long."
        elif len(attrs.get('password')) > 128:
            errors['password'] = "Password must be at most 128 characters long."
        elif not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', attrs.get('password')):
            errors['password'] = "Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character."
        
        # 2. Email Validation
        # if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', attrs.get('email')):
        #     errors['email'] = "Invalid email format."

        # 3. First Name Validation
        if not attrs.get('first_name').isalpha():
            errors['first_name'] = "First name must contain only letters."
        elif len(attrs.get('first_name')) < 2:
            errors['first_name'] = "First name must be at least 2 characters long."
        elif len(attrs.get('first_name')) > 150:
            errors['first_name'] = "First name must be at most 150 characters long."

        # 4. Last Name Validation
        if not attrs.get('last_name').isalpha():
            errors['last_name'] = "Last name must contain only letters."
        elif len(attrs.get('last_name')) < 2:
            errors['last_name'] = "Last name must be at least 2 characters long."
        elif len(attrs.get('last_name')) > 150:
            errors['last_name'] = "Last name must be at most 150 characters long."

        if errors:
            raise serializers.ValidationError(errors)

        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ""),
            last_name=validated_data.get('last_name', "")
        )
        return user


