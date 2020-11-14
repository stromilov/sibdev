from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Deal

class DealView(APIView):
    def get(self, request):
        deals = Deal.objects.all()
        return Response({"deals": deals})