from rest_framework import serializers
from .models import User,Patient, Doctor, PatientDoctorMapping
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True,
                                   validators = [UniqueValidator(queryset=User.objects.all())]
                                   )
    password = serializers.CharField(write_only = True,required = True,validators = [validate_password])
    password2 = serializers.CharField(write_only = True,required = True)

    class Meta:
        model = User
        fields = ['email','password','password2','name',]
    
    def validate(self,attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password":"password field didn't match"})
        return attrs
    def create(self,validate_data):
        user = User.objects.create(
            email = validate_data['email'],
            name = validate_data['name'],
        )
        user.set_password(validate_data['password'])
        user.save()
        return user
    
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=200)
    class Meta:
        model = User
        fields = ['email','password']

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ['user', 'created_at']

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        read_only_fields = ['created_at']
    
class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'patient_name', 'doctor_name', 'assigned_at']
