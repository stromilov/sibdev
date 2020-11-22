#views.py

from rest_framework.response import Response

from rest_framework.decorators import api_view

from .models import Deal

from .serializers import DealSerializer

from rest_framework.views import APIView


class APIDeals(APIView):
    def get(self, request):

        deals = Deal.objects.all().extra(order_by = ['-total'])[:5]
        serializer = DealSerializer(deals, many=True)
        return Response({"response": serializer.data})
