from rest_framework import serializers
from . models import Account, CounselorEducation, CounselorExperience, CounselorProfile
from rest_framework.validators import ValidationError


class CounselorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }


class CounselorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CounselorProfile
        fields = ['fee', 'specialization', 'state']


class CounselorExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CounselorExperience
        fields = '__all__'


class CounselorEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CounselorEducation
        fields = '__all__'
