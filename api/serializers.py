from rest_framework import serializers

class DonnarSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = '__all__'
