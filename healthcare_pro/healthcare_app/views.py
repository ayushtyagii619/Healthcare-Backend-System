from django.shortcuts import render
from .models import User, Patient, Doctor, PatientDoctorMapping
from .serializers import RegisterSerializer , LoginSerializer, PatientSerializer, DoctorSerializer, PatientDoctorMappingSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

def get_tokens(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh':str(refresh),
        'access':str(refresh.access_token)
    }

class RegisterApiView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message':'Registraion Success'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginApiView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email,password=password)
            if user is not None:
                token = get_tokens(user)
                return Response({'token':token,'msg':'Login Successful'},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Email or password is not valid']}},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class PatientCreateApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        patients = Patient.objects.filter(user=request.user)
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class PatientDeatilsApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        return get_object_or_404(Patient, pk=pk, user=user)
    
    def get(self, request, pk):
        patient = self.get_object(pk, request.user)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    
    def put(self, request, pk):
        patient = self.get_object(pk, request.user)
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        patient = self.get_object(pk, request.user)
        patient.delete()
        return Response({'detail': 'Patient deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
class DoctorCreateApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(slef,request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DoctorDetailsApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self,pk):
        return get_object_or_404(Doctor,pk=pk)
    
    def get(self,request,pk):
        doctor = self.get_object(pk)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    def put(self,request,pk):
        doctor = self.get_object(pk)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        doctor = self.get_object(pk)
        doctor.delete()
        return Response({'detail': 'Doctor deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
class MappingCreateApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = PatientDoctorMappingSerializer(data=request.data)

        if serializer.is_valid():
            #Check if patient & doctor exist
            patient = get_object_or_404(Patient, id=request.data.get('patient'))
            doctor = get_object_or_404(Doctor, id=request.data.get('doctor'))

            #Check for duplicates
            if PatientDoctorMapping.objects.filter(patient=patient, doctor=doctor).exists():
                return Response({'detail': 'This doctor is already assigned to the patient.'}, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        mappings = PatientDoctorMapping.objects.all()
        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class MappingByPatientApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, patient_id):
        mappings = PatientDoctorMapping.objects.filter(patient_id=patient_id)
        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MappingDeleteApiView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        mapping = get_object_or_404(PatientDoctorMapping, pk=pk)
        mapping.delete()
        return Response({'detail': 'Mapping deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# Create your views here.
