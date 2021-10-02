from rest_framework import views, status
from rest_framework.response import Response

from blood.models.donor import Donor
from .donor_serializers import DonorSerializer
from utils.custom_responses import *


class DonorAPIView(views.APIView):

    def get(self, request):
        try:
            donor = Donor.objects.all()
            serializer = DonorSerializer(donor, many=True)
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        except Exception as e:
            return Response(prepare_error_response(str(e)), status=status.HTTP_400_BAD_REQUEST)
