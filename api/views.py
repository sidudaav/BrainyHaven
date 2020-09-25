from rest_framework import viewsets
from home.models import Pattern, Analogy, Riddle
from .serializers import PatternSerializer, AnalogySerializer, RiddleSerializer

class PatternViewSet(viewsets.ModelViewSet):
    queryset = Pattern.objects.filter(is_active=True)
    serializer_class = PatternSerializer

class AnalogyViewSet(viewsets.ModelViewSet):
    queryset = Analogy.objects.filter(is_active=True)
    serializer_class = AnalogySerializer

class RiddleViewSet(viewsets.ModelViewSet):
    queryset = Riddle.objects.filter(is_active=True)
    serializer_class = RiddleSerializer