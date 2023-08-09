from django.core.exceptions import ValidationError
import re
from rest_framework import serializers

def validate_username(self, value):
    if not re.match(r'^[\w.@+-]+$', value):
        raise serializers.ValidationError('Недопустимые символы.')
    return value
