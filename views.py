from rest_framework.views import APIView

from .models import Deal

from .serializers import DealSerializer


class APIDeals(APIView):
    def get(self, request):
        deals = Deal.objects.all()
        serializer = DealSerializer(deals, many=True)
        return Response({"deals": serializer.data})