from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class JobSeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeekerTbl
        fields = "__all__"


class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruiterTbl
        fields = "__all__"
