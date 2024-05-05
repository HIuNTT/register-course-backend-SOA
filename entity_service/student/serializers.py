from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Student


class StudentRegisSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Student
        fields = ['id', 'username', 'password', 'password2']

    def validate(self, attrs):
        if attrs.get('password') != attrs.pop('password2'):
            raise serializers.ValidationError(
                {'password2': "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        student = Student.objects.create_user(**validated_data)
        student.set_password(validated_data['password'])
        student.save()
        return student