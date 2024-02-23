from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Api
from .serializers import ApiSerializer

class listData(APIView):
    def get(self,request):
        db_data = Api.objects.all()
        serialize_data = ApiSerializer(db_data,many=True)
        return Response(serialize_data.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serialize_data = ApiSerializer(data=request.data,many=True)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response(serialize_data.data,status=status.HTTP_201_CREATED)
        return Response(serialize_data.errors,status=status.HTTP_400_BAD_REQUEST)
    
class RetrieveData(APIView):
    def get_object(self,pk):
        try:
            return Api.objects.get(pk=pk)
        except Api.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        db_object_data = self.get_object(pk)
        serialize_data = ApiSerializer(db_object_data)
        return Response(serialize_data.data,status=status.HTTP_200_OK)
    
class UpdateData(APIView):
        def get_object(self,pk):
            try:
                return Api.objects.get(pk=pk)
            except Api.DoesNotExist:
                raise Http404
            
        def get(self,request,pk):
            db_object_data = self.get_object(pk)
            serialize_data = ApiSerializer(db_object_data)
            return Response(serialize_data.data,status=status.HTTP_200_OK)
        
        def put(self,request,pk):
            db_object_data = self.get_object(pk)
            serialize_data = ApiSerializer(db_object_data,data=request.data)
            if serialize_data.is_valid():
                serialize_data.save()
                return Response(serialize_data.data,status=status.HTTP_201_CREATED)
            return Response(serialize_data.errors,status=status.HTTP_400_BAD_REQUEST)
        
class DeleteData(APIView):
            def get_object(self,pk):
                try:
                    return Api.objects.get(pk=pk)
                except Api.DoesNotExist:
                    raise Http404
                
            def delete(self,request,pk):
                db_object_data =self.get_object(pk)
                db_object_data.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)