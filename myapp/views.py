from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from myapp import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer 
    def get(self, request, format=None):
        """Returns the list of API features list"""
        an_apiview = [
            'http methods:get, put, post, patch, delete',
            'You can aadd anything here'
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ Handle update to the objects"""
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """ Handle partial updates to the objects"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """ Handle deleting of the objects"""
        return Response({'method': 'DELETE '})




