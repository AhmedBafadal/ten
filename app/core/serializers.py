from .models import Booking
from .rest_framework import serializers

class BookingSerializer(serializers.ModelSerializer):
    # redefining code as it is unique
    code = serializers.CharField(validators=[])
    class Meta:
        model = Booking
        fields = ('code')