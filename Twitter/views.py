from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


def homepage(request):
    return render(request, 'base.html')


class tf_processing(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        data = {
            "sales": 3400,
            "company": 5400
        }
        return Response(data)
