from rest_framework import serializers
from blog.models import RegisterModel


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=RegisterModel
        fields=(
            'name',
            'profile',
            'email',
            'password'
        )