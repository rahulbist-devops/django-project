from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns the list of API features list"""
        an_apiview = [
            'http methods:get, put, post, patch, delete',
            'You can aadd anything here'
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

