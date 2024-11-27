from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SimpleGetAPI(APIView):
    def get(self, request):
        data = [
            {
                "id": 1,
                "name": "Example Configuration",
                "value": "example_value"
            }
        ]
        return Response(data, status=status.HTTP_200_OK)
    
    