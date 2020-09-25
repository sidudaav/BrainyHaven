from rest_framework import serializers
from home.models import Pattern, Analogy, Riddle

class PatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pattern
        fields = '__all__'


class AnalogySerializer(serializers.ModelSerializer):
    class Meta:
        model = Analogy
        fields = '__all__'


class RiddleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Riddle
        fields = '__all__'