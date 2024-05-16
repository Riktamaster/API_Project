from rest_framework import serializers
from .models import *

class bookmodelSerializer(serializers.ModelSerializer):
    class Meta:
        model=book_model
        fields='__all__'