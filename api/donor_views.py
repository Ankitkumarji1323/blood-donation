from rest_framework import views, status
from rest_framework.response import Response

from blood.models.donor import Donor
from .donor_serializers import DonorSerializer
from utils.custom_responses import *
from utils.validation import validate_donor_data


class DonorAPIView(views.APIView):

    def get(self, request):
        try:
            donor = Donor.objects.all()
            serializer = DonorSerializer(donor, many=True)
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        except Exception as e:
            return Response(prepare_error_response(str(e)), status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        validate_error = validate_donor_data(request.data)
        if validate_error is not None:
            return Response(prepare_error_response(validate_error), status=status.HTTP_400_BAD_REQUEST)
        serializer = DonorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
